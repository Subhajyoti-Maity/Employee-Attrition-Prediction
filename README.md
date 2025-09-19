# Employee Attrition Prediction

## Overview
A machine learning application that predicts employee attrition risk using HR analytics data. Built with Python and Streamlit, it helps HR professionals identify employees who might be at risk of leaving the organization.

## Features
- Real-time attrition risk prediction
- User-friendly web interface
- Considers multiple factors like age, salary, job level, etc.
- Special handling for senior management profiles
- Risk score calculation and stability assessment

## Demo Screenshots

### 1. High Attrition Risk Example
This example shows an employee with high risk of attrition:

![High Attrition Risk](/screenshots/high_attrition_risk.png)

### 2. Low Attrition Risk Example (Stable Manager)
This example shows a senior manager with stable profile:

![Low Attrition Risk](/screenshots/low_attrition_risk.png)

## Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Subhajyoti-Maity/Employee-Attrition-Prediction.git
   cd Employee-Attrition-Prediction
   ```

2. Install required packages:
   ```bash
   pip install streamlit pandas scikit-learn xgboost
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

### Access
- Local URL: http://localhost:8501
- Network URL: http://<your-network-ip>:8501

## Project Structure
```
Employee-Attrition-Prediction/
├── app.py                      # Main application
├── best_attrition_model.pkl    # Trained model
├── best_model_columns.pkl      # Model features
├── WA_Fn-UseC_-HR-Employee-Attrition.csv  # Dataset
└── screenshots/                # App screenshots
```

## Tech Stack
- Streamlit (Web Interface)
- Scikit-learn & XGBoost (Machine Learning)
- Pandas & NumPy (Data Processing)

## Model Details
The model analyzes various employee attributes including:
- Age and Years of Experience
- Job Level and Role
- Monthly Income
- Work-Life Balance Indicators
- Job Satisfaction Metrics

## Future Improvements
- Advanced feature engineering
- Cloud deployment options
- API development for system integration
- Additional model experimentation
