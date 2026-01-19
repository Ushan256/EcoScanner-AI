# 🌍 EcoScanner AI: Computer Vision for Resource Recovery
**Research-Grade AI Platform for Real-Time Waste Classification & Carbon Mitigation**

**Live Demo:** https://ecoscanner-aigit-fqbbxw2gv8qurqhowr6a3r.streamlit.app/
**EcoScanner AI** is a professional-grade research platform that leverages advanced Computer Vision to automate the identification of recyclables and quantify their environmental impact. By integrating deep learning with a secure full-stack architecture, this project provides a scalable solution for monitoring carbon footprints within a circular economy.

---

## 🏗️ System Architecture

### 1. Research-Grade Neural Engine
The system's core is a fine-tuned **YOLOv8** architecture. It utilizes a specialized inference pipeline optimized for high-speed object localization and material classification.
* **Model ID**: `YOLOv8s_FineTuned_TACO_v1`
* **Dataset**: Trained on the **TACO (Trash Annotations in Context)** dataset for superior detection accuracy in diverse lighting conditions.

### 2. Core Functional Modules
* **AI Vision Scanner**: Supports dual-interface ingestion via **Live Webcam Feed** or high-resolution **Local File Upload**.
* **Carbon Mitigation Engine**: Implements a logic-driven mathematical model to calculate **CO2 savings** based on international recycling standards for plastic, metal, and glass.
* **Impact Portfolio**: Features a robust user authentication system with **Bcrypt hashing** and persistent **SQLite** storage for long-term tracking.
* **Global Insights**: A real-time **Leaderboard** that aggregates data across all users to visualize community-level sustainability contributions.

---

## 🛠️ Technical Excellence

### ⚡ Neural Inference Optimization
The inference pipeline is engineered for efficiency and reliability:
* **RGB Standardization**: Forces 3-channel conversion on all input frames to prevent `RuntimeError` during inference.
* **Hyperparameter Tuning**: Operates at a **0.4 Confidence Threshold** and **0.5 IOU** to minimize "hallucinations" and false positives.
* **Resource Caching**: Utilizes `@st.cache_resource` to ensure the model is only loaded once, reducing system overhead during high-frequency scans.

### 📈 Business Intelligence & Analytics
The dashboard provides deep insights into environmental contribution through automated views:
* **Personal Metrics**: Automated calculation of Total CO2 Mitigated vs. Items Audited.
* **Distribution Analytics**: Visualizes material recycling habits using dynamic bar and line charts.
* **Inference Diagnostics**: Real-time tracking of hardware performance and neural weight integrity.

---

## 🎨 Design Philosophy: Glassmorphism UI
The interface features a premium **Glassmorphism UI Engine** implemented via custom CSS injection to provide a modern research aesthetic:
* **Glass Cards**: Semi-transparent containers with `backdrop-filter: blur(20px)` for a sophisticated look.
* **Dynamic Theme Engine**: Automatically re-injects CSS styles when toggling between **Ultra-Dark** and **Light Mode**.
* **Micro-Animations**: Custom button transitions and interactive metrics provide a responsive user experience.

---

## 📊 Environmental Impact & Use Cases
* **Urban Waste Management**: Automate the sorting process in high-traffic commercial or residential zones.
* **Supply Chain Sustainability**: Track the lifecycle of packaging materials and verify carbon credit claims.
* **SDG Implementation**: Directly supports **UN Sustainable Development Goal 12** by digitizing responsible consumption patterns.

---

## ⚙️ Technical Specifications
* **DBMS**: SQLite 3.0 (Local-Persistence Engine)
* **Python Version**: 3.10+
* **Security**: Bcrypt password encryption (Salt-based hashing)
* **Performance**: < 5ms object localization on standard CPU hardware

---

## 🚀 Getting Started
1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Ushan256/EcoScanner-AI.git](https://github.com/Ushan256/EcoScanner-AI.git)
    ```
2.  **Install Dependencies**
    ```bash
    pip install streamlit pandas ultralytics bcrypt pillow opencv-python-headless
    ```
3.  **Launch the Dashboard**
    ```bash
    streamlit run app.py
    ```
---

**Developed by:** Ushan
**Last Updated:** January 2026

---

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/Ushan256/EcoScanner-AI.git](https://github.com/Ushan256/EcoScanner-AI.git)
