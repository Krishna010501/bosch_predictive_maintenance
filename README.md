# 🛠️ Bosch-Style Predictive Maintenance System

![Header Image - CNC AI Project](https://via.placeholder.com/1200x300.png?text=Bosch+Predictive+Maintenance+System+%7C+AI+%2B+Mechanical)

> 🚀 An AI-powered real-time dashboard that predicts CNC machine failures based on sensor data — inspired by Bosch Industry 4.0 smart factory systems.

---

## 📚 Table of Contents
- [📌 Project Summary](#-project-summary)
- [🧰 Tech Stack](#-tech-stack)
- [⚙️ Setup Instructions](#️-setup-instructions)
- [🌐 Live Streamlit Demo](#-live-streamlit-demo)
- [📊 Live Screenshot](#-live-screenshot)
- [💼 Resume-Ready Bullet Points](#-resume-ready-bullet-points)
- [🧪 Sample Sensor Data](#-sample-sensor-data)
- [🏷️ GitHub Badges](#️-github-badges)
- [🙌 Acknowledgements](#-acknowledgements)
- [🔗 Connect with Me](#-connect-with-me)
- [🤖 EDA + AI/ML for Mechanical Systems](#-exploratory-data-analysis-eda--aiml-for-mechanical-systems)
- [🧠 Project Highlights (Mechanical + AI Blend)](#-project-highlights-mechanical--ai-blend)
- [📈 System Architecture](#-system-architecture)

---

## 📌 Project Summary

This project simulates a predictive maintenance system for CNC machines using real-time sensor data such as **temperature**, **vibration**, and **RPM**. It uses a **Random Forest Classifier** to detect potential machine failures and displays the results on an interactive **Streamlit dashboard**.

Designed for hybrid **Mechanical + Computer Science** engineers aiming to work in smart manufacturing, industrial automation, and AI-driven maintenance.

---

## 🧰 Tech Stack

| Area               | Tools / Libraries                       |
|--------------------|------------------------------------------|
| Language           | Python                                   |
| ML/AI              | Scikit-learn, Joblib                     |
| Data Handling      | Pandas, NumPy                            |
| Dashboard          | Streamlit                               |
| Visualization      | Matplotlib, Seaborn                      |
| Version Control    | Git + GitHub                             |

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/Krishna010501/bosch_predictive_maintenance.git
cd bosch_predictive_maintenance

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model
python src/model_trainer.py

# 4. Launch the Streamlit dashboard
streamlit run src/dashboard_app.py
```

---

## 🌐 Live Streamlit Demo

🚀 **Experience the full app live**:  
🔗 [Click here to open the dashboard](https://krishna010501-bosch-predictive-maintena-srcdashboard-app-gsewsm.streamlit.app/)

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live--App-brightgreen?logo=streamlit)](https://krishna010501-bosch-predictive-maintena-srcdashboard-app-gsewsm.streamlit.app/)

---

## 📊 Live Screenshot

> *(Insert your dashboard screenshot or GIF below once ready)*

![Dashboard Preview](https://via.placeholder.com/800x400.png?text=Live+Dashboard+Demo)

---

## 💼 Resume-Ready Bullet Points

- Developed a real-time predictive maintenance system using Python and machine learning, targeting CNC machines in smart factory settings.
- Built a Streamlit dashboard that simulates sensor input and visually predicts equipment failure.
- Trained a Random Forest model on simulated data to classify normal vs. failure states, achieving 100% accuracy on test data.
- Integrated Exploratory Data Analysis (EDA) to understand the impact of temperature, vibration, and RPM on failure likelihood.
- Inspired by Bosch's Industry 4.0 strategy, integrating AI in mechanical systems.

---

## 🧪 Sample Sensor Data

| Timestamp           | Temp (°C) | Vibration RMS | RPM  | Failure |
|---------------------|-----------|----------------|------|---------|
| 2025-04-01 10:00:00 | 65        | 0.3            | 1500 | 0       |
| 2025-04-01 10:01:00 | 68        | 0.4            | 1490 | 0       |
| 2025-04-01 10:02:00 | 72        | 0.8            | 1450 | 1       |

---

## 🏷️ GitHub Badges

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest-success)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/Krishna010501/bosch_predictive_maintenance)
![Repo Size](https://img.shields.io/github/repo-size/Krishna010501/bosch_predictive_maintenance)

---

## 🙌 Acknowledgements

Inspired by **Bosch’s predictive maintenance AI systems** in industrial automation and smart factories.

---

## 🔗 Connect with Me

📧 inturipavankalyan2001@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kinturi) | [GitHub](https://github.com/Krishna010501)

---

## 🤖 Exploratory Data Analysis (EDA) + AI/ML for Mechanical Systems

This project bridges my **Mechanical Engineering background** with my current journey in **Artificial Intelligence & Machine Learning**.

Through EDA on CNC machine sensor data (temperature, vibration, RPM), I analyzed patterns and trends that often indicate failure conditions. I then trained a Random Forest model to **predict machine failure**, bringing **real-world AI to mechanical systems**.

📈 View the full analysis in this notebook:  
👉 [🧪 EDA Notebook](notebooks/eda_model_building.ipynb)

---

## 🧠 Project Highlights (Mechanical + AI Blend)

- Applied AI/ML to **realistic mechanical sensor data** for failure prediction.
- Modeled **machine behavior** through temperature, vibration, and speed data.
- Created an interactive tool that mimics Bosch’s **smart manufacturing insights**.

---

## 📈 System Architecture

```plaintext
┌─────────────────────┐
│ Simulated Sensor Data│
│ (Temp, Vibration, RPM)│
└─────────────┬───────┘
              ↓
     ┌─────────────────┐
     │ Data Cleaning   │
     └─────────────────┘
              ↓
     ┌─────────────────┐
     │ EDA + Analysis  │
     └─────────────────┘
              ↓
     ┌────────────────────────────┐
     │ Random Forest Classifier  │
     └────────────────────────────┘
              ↓
     ┌────────────────────────────┐
     │ Streamlit Dashboard Output │
     └────────────────────────────┘
```
