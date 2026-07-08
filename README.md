# 🧠 Insight AutoML

> AI-Powered AutoML & Data Analytics Platform built with **Streamlit**, **FastAPI**, **Scikit-learn**, **Ollama**, and **Docker**.


## 🚀 Overview

Insight AutoML is an end-to-end machine learning platform that allows users to upload datasets, automatically train multiple machine learning models, compare their performance, perform Exploratory Data Analysis (EDA), and interact with an AI-powered dataset assistant using Ollama.

The project is designed to simplify the machine learning workflow while providing an intuitive interface for students, researchers, and data analysts.


# ✨ Features

- 📂 Upload CSV datasets
- 🔍 Automatic Dataset Preview
- 📊 Exploratory Data Analysis (EDA)
- 📉 Correlation Heatmap
- 🎯 Target Column Selection
- 🤖 Train Multiple Machine Learning Models
- 🏆 Automatic Best Model Selection
- 📈 Model Performance Comparison
- 📊 Accuracy Visualization
- 💬 AI Dataset Assistant (Powered by Ollama)
- 📥 Download Model Performance as CSV
- ⚡ FastAPI Backend
- 🎨 Interactive Streamlit Interface
- 🐳 Docker Support


# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI

## Machine Learning
- Scikit-learn
- Pandas
- NumPy
- SciPy

## Data Visualization
- Plotly
- Matplotlib
- Seaborn

## AI
- Ollama (Llama 3)

## DevOps
- Docker
- Docker Compose

## Version Control
- Git
- GitHub



# 📂 Project Structure


InsightAI-AutoML
│
├── backend/
│
├── frontend/
│
├── datasets/
│
├── models/
│
├── reports/
│
├── screenshots/
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── .dockerignore
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore



## 🤖 AI Dataset Assistant

The AI assistant uses **Ollama (Llama 3)**.

### Install Ollama

https://ollama.com

### Start Ollama

```bash
ollama serve
```

### Download the model

```bash
ollama pull llama3
```

> **Note:** The AI Assistant requires Ollama to be running locally. Other features of Insight AutoML work independently of Ollama.


## ⚙️ Installation

# Clone Repository

```bash
git clone https://github.com/nikhilbhargav8887/InsightAI-AutoML.git

cd InsightAI-AutoML
```

# Create Virtual Environment

```bash
python -m venv venv
```

# Activate Environment

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

# Install Dependencies

```bash
pip install -r requirements.txt
```


# ▶️ Run Backend

```bash
uvicorn backend.main:app --reload
```


# ▶️ Run Frontend

```bash
streamlit run frontend/app.py
```

# 🐳 Docker

Build and run the project:

```bash
docker compose up --build
```

Backend:

```
http://localhost:8000
```

Frontend:

```
http://localhost:8501
```

> **Note:** The AI Dataset Assistant requires Ollama to be installed and running locally.


# 🔄 Workflow


Upload Dataset
        │
        ▼
Dataset Preview
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Train Multiple ML Models
        │
        ▼
Compare Performance
        │
        ▼
Select Best Model
        │
        ▼
Ask AI Dataset Assistant
        │
        ▼
Download Results





## 🤖 AI Dataset Assistant

The application integrates **Ollama** to provide an intelligent AI assistant capable of answering questions related to:

- Dataset structure
- Missing values
- Feature engineering
- Model performance
- Machine Learning concepts
- Preprocessing recommendations



## 📊 Machine Learning Models

The platform currently supports:

- Logistic Regression
- Random Forest
- Decision Tree
- KNN
- Support Vector Machine (SVM)



## 📸 Screenshots



## 🏠 Home Page

![Home](screenshots/home.png)

---

## 📊 Exploratory Data Analysis

![EDA](screenshots/eda.png)

---

## 🏆 Model Training & Comparison

![Training](screenshots/training.png)

---

## 🤖 AI Dataset Assistant

![AI Assistant](screenshots/ai_assistant.png)

---

## 📈 Accuracy Comparison

![Comparison](screenshots/comparison.png)




# 🎯 Future Improvements

- XGBoost & LightGBM integration
- Hyperparameter tuning
- SHAP Explainability
- Power BI Dashboard Integration
- Tableau Dashboard Integration
- Cloud Deployment
- User Authentication
- Model Persistence