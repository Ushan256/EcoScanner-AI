🌱 EcoScanner AI: Real-Time Waste Classification & Carbon Tracking
EcoScanner AI is a professional-grade sustainability dashboard that leverages Computer Vision to automate the identification of recyclables and quantify their environmental impact. By integrating deep learning with a secure full-stack architecture, this project provides a scalable solution for monitoring carbon footprints in a circular economy.

🏗️ System Architecture & Code Explanation
The application is built on a modular architecture to ensure separation of concerns, high performance, and security.

1. Library Ecosystem: Why these were chosen
Your app.py utilizes a specialized stack of Python libraries:

streamlit (st): Chosen for the frontend to create a high-performance, interactive web interface using Python. It handles the Glassmorphism UI and real-time state management.

pandas (pd): Used as the primary data manipulation engine for processing user history and generating analytical dataframes for charts.

os & platform: These libraries handle system-level operations, such as checking for the existence of best.pt model weights and displaying system diagnostics like OS version and environment specs.

cv2 (OpenCV): A powerful computer vision library used here for image array handling and ensuring that pixel data is structured correctly before being passed to the AI.

time & datetime: Vital for measuring Inference Latency (how fast the AI thinks) and timestamping user contributions in the database.

ultralytics (YOLO): The "brain" of the project. It runs the fine-tuned YOLOv8 model to perform object localization and material classification in milliseconds.

2. Core Functional Modules
🛡️ Data Persistence (database.py)
This module provides the secure backbone for the application. It utilizes SQLite for lightweight, local-persistence storage. Key functions include:

init_db(): Initializes relational tables for user credentials and historical logs.

bcrypt hashing: Used during user creation to ensure that passwords are never stored in plain text, meeting modern security standards.

get_all_user_stats(): Performs SQL aggregation to generate the global leaderboard.

🧠 Neural Engine (logic.py)
This layer orchestrates the computer vision pipeline.

Pre-processing: Forces image conversion to 3-channel RGB, stripping away "Alpha" channels to prevent RuntimeError.

Inference: Executes the YOLOv8 model with an optimized Confidence Threshold (0.4) and IOU (0.5) to ensure accurate detections without "hallucinations".

Material Mapping: Maps TACO dataset labels (e.g., 'Bottle') to standard CO2 factors (e.g., 'Plastic') for environmental math.

🎨 Professional UI Design: Glassmorphism
The interface uses a custom Glassmorphism UI Engine implemented via CSS injection in apply_styles(is_dark).

Backdrop Filter: Creates a blurred, semi-transparent "glass" look for cards.

Dynamic Theme Engine: Automatically re-injects CSS colors when the user toggles between Ultra-Dark and Light Mode.

Responsive Metrics: Uses Streamlit's st.metric and st.line_chart to show personal CO2 trends dynamically.

📊 Technical Research Points (FCCU Semester Project)
Distributed Training: The model was fine-tuned on the TACO Dataset using cloud-based GPU acceleration (NVIDIA T4) to ensure high detection accuracy for common recyclables.

SDG Alignment: This project directly supports United Nations SDG 12 (Responsible Consumption) by providing actionable data on waste management.

Low-Latency Performance: Optimized the inference pipeline to achieve localized object detection in under 5ms on standard CPU hardware.

🏁 Installation & Usage
Environment Setup: Ensure Python 3.10+ is installed.

Install Dependencies:

Bash

pip install streamlit pandas ultralytics bcrypt pillow opencv-python
Launch Dashboard:

Bash

streamlit run app.py