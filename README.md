# Fraud Detection System

A full-stack fraud detection system designed for banking applications.  
This system detects suspicious transactions using a hybrid rule-based and ML-assisted approach, with a real-time monitoring dashboard.

## Features

- JWT Authentication (Admin / User roles)
- Transaction processing API
- Fraud detection (Rule-based + ML-assisted)
- Admin dashboard with live data
- Performance metrics (Accuracy, Precision, Recall)
- Real-time monitoring (auto-refresh UI)
- Explainable fraud decisions

## Tech Stack

- Backend: FastAPI (Python)
- Database: Supabase (PostgreSQL)
- ML Model: Isolation Forest
- Frontend: HTML, CSS, JavaScript
- Charts: Chart.js

## System Architecture

User Transaction → Fraud Engine → Risk Scoring → Alerts → Dashboard

## Key Highlights

- Hybrid fraud detection system (rules + ML)
- Role-based secure API access
- Real-time dashboard with alerts
- Explainable fraud decisions
- Full-stack implementation

## Setup Instructions

### 1. Clone Repository
# Fraud Detection System

A full-stack fraud detection system designed for banking applications.  
This system detects suspicious transactions using a hybrid rule-based and ML-assisted approach, with a real-time monitoring dashboard.

## Features

- JWT Authentication (Admin / User roles)
- Transaction processing API
- Fraud detection (Rule-based + ML-assisted)
- Admin dashboard with live data
- Performance metrics (Accuracy, Precision, Recall)
- Real-time monitoring (auto-refresh UI)
- Explainable fraud decisions

## Tech Stack

- Backend: FastAPI (Python)
- Database: Supabase (PostgreSQL)
- ML Model: Isolation Forest
- Frontend: HTML, CSS, JavaScript
- Charts: Chart.js

## System Architecture

User Transaction → Fraud Engine → Risk Scoring → Alerts → Dashboard

## Key Highlights

- Hybrid fraud detection system (rules + ML)
- Role-based secure API access
- Real-time dashboard with alerts
- Explainable fraud decisions
- Full-stack implementation

## Setup Instructions

### 1. Clone Repository
git clone https://github.com/eshaaa18/fraud-detection-system.git
cd fraud-detection-system

### 2. Create `.env` file
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SECRET_KEY=your_secret_key

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run backend
uvicorn main:app --reload

### 5. Run frontend

Open:
frontend/index.html


## Example Features

- High-risk transaction detection
- Fraud vs Safe transaction visualization
- Performance metrics (precision, recall)
- Alert generation for suspicious activity

## Future Improvements

- Real-time streaming (Kafka)
- Advanced ML models (XGBoost)
- Explainable AI (SHAP)
- Cloud deployment

## Why this project?

This project demonstrates:

- Backend engineering (APIs, authentication, database)
- System design thinking
- Real-world fintech application
- Data-driven decision systems


## IF U LIKE IT PLEASE GIVE IT A STAR
And even if you dont do tell me what i can improve.

