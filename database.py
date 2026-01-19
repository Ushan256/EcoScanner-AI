import sqlite3
import bcrypt

def init_db():
    """Initializes the database schema for users and their recycling history."""
    conn = sqlite3.connect('eco_scanner.db')
    c = conn.cursor()
    # User table for authentication
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (username TEXT PRIMARY KEY, password TEXT, email TEXT)''')
    # History table for tracking environmental impact
    c.execute('''CREATE TABLE IF NOT EXISTS history 
                 (username TEXT, material TEXT, co2_saved REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def create_user(username, password, email):
    """Hashes passwords and registers a new researcher in the system."""
    try:
        conn = sqlite3.connect('eco_scanner.db')
        c = conn.cursor()
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, hashed, email))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def verify_user(username, password):
    """Verifies credentials using bcrypt hashing."""
    conn = sqlite3.connect('eco_scanner.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        return True
    return False

def add_history(username, material, co2_saved):
    """Logs a successful recycling detection to the user's portfolio."""
    conn = sqlite3.connect('eco_scanner.db')
    c = conn.cursor()
    c.execute("INSERT INTO history (username, material, co2_saved) VALUES (?, ?, ?)", 
              (username, material, co2_saved))
    conn.commit()
    conn.close()

def get_history(username):
    """Retrieves all historical data for a specific user."""
    conn = sqlite3.connect('eco_scanner.db')
    c = conn.cursor()
    c.execute("SELECT material, co2_saved, timestamp FROM history WHERE username=? ORDER BY timestamp DESC", (username,))
    data = c.fetchall()
    conn.close()
    return data

def get_all_user_stats():
    """
    REQUIRED FIX: Aggregates CO2 mitigation data across all users for the leaderboard.
    Demonstrates SQL aggregation (GROUP BY and SUM) for research documentation.
    """
    try:
        conn = sqlite3.connect('eco_scanner.db')
        c = conn.cursor()
        # Groups records by user to calculate total impact per person
        c.execute("SELECT username, SUM(co2_saved) FROM history GROUP BY username ORDER BY SUM(co2_saved) DESC")
        data = c.fetchall()
        conn.close()
        return data
    except Exception as e:
        print(f"Database Aggregation Error: {e}")
        return []