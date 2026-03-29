"""
database.py — EcoScanner AI persistence layer.

IMPORTANT NOTE ON STREAMLIT CLOUD PERSISTENCE:
Streamlit Community Cloud uses an ephemeral filesystem.
Any file written to the default working directory (/app/...)
is wiped on every redeployment or restart.

To keep user accounts and history across restarts:
  - Option A (this file): Store the DB in /tmp. Accounts
    survive normal restarts but are wiped on full redeployment.
    Good enough for a research prototype / demo.
  - Option B (production): Use an external DB (PostgreSQL via
    st.secrets, Supabase, PlanetScale, etc.).

For this research prototype, we use /tmp which persists across
Streamlit's soft restarts (triggered by code changes in the
sidebar) but is reset on full server redeployment.
"""

import sqlite3
import bcrypt
import os

# ------------------------------------------------------------------
# DB PATH
# Use an absolute /tmp path so the file is NOT wiped on soft restart.
# Change this to a Supabase/Postgres URL for production.
# ------------------------------------------------------------------
DB_PATH = os.path.join("/tmp", "ecoscanner.db")


def _get_conn():
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create tables if they do not already exist."""
    with _get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT    UNIQUE NOT NULL,
                password TEXT    NOT NULL,
                email    TEXT    NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                username  TEXT    NOT NULL,
                material  TEXT    NOT NULL,
                co2_saved REAL    NOT NULL,
                timestamp DATETIME DEFAULT (datetime('now'))
            )
        """)
        conn.commit()


def create_user(username: str, password: str, email: str) -> bool:
    """
    Create a new user. Password is hashed with bcrypt before storage.
    Returns True on success, False if the username already exists.
    """
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    try:
        with _get_conn() as conn:
            conn.execute(
                "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                (username, hashed.decode("utf-8"), email)
            )
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Username already exists (UNIQUE constraint)
        return False


def verify_user(username: str, password: str) -> bool:
    """
    Verify login credentials.
    Returns True if username exists and password matches the stored hash.
    """
    with _get_conn() as conn:
        row = conn.execute(
            "SELECT password FROM users WHERE username = ?",
            (username,)
        ).fetchone()

    if row is None:
        return False

    stored_hash = row["password"]
    try:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            stored_hash.encode("utf-8")
        )
    except Exception:
        return False


def add_history(username: str, material: str, co2_saved: float):
    """Log a recycling event for the given user."""
    with _get_conn() as conn:
        conn.execute(
            "INSERT INTO history (username, material, co2_saved) "
            "VALUES (?, ?, ?)",
            (username, material, co2_saved)
        )
        conn.commit()


def get_history(username: str):
    """
    Return all history rows for a user, ordered by most recent first.
    Each row is (material, co2_saved, timestamp).
    """
    with _get_conn() as conn:
        rows = conn.execute(
            "SELECT material, co2_saved, timestamp "
            "FROM history WHERE username = ? "
            "ORDER BY timestamp DESC",
            (username,)
        ).fetchall()
    return [tuple(r) for r in rows]


def get_all_user_stats():
    """
    Return aggregated (username, total_co2_saved) for the leaderboard,
    ordered by highest total first.
    """
    with _get_conn() as conn:
        rows = conn.execute(
            "SELECT username, SUM(co2_saved) AS total "
            "FROM history "
            "GROUP BY username "
            "ORDER BY total DESC"
        ).fetchall()
    return [(r["username"], r["total"]) for r in rows]
