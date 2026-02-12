# 🧑‍💼 Employee Attrition Prediction

## 🧭 1. Overview
A Streamlit-based machine learning app that predicts employee attrition risk from key HR attributes. It provides a clean dashboard and a probability-driven risk signal to help HR teams identify employees who may be at risk of leaving. The current model achieves 0.86 accuracy on the test split.

## ✨ 2. Features
- Real-time attrition risk probability with low/high risk label
- Streamlit dashboard with sidebar controls and a predict action
- Inputs: age, monthly income, job level, total working years, overtime, and job role
- Employee overview table for the selected inputs
- Modern UI styling with custom theme and layout

## 🎬 3. Demo Clips

### 3.1 High Attrition Risk Example
This example shows an employee with high risk of attrition:

![High Attrition Risk](/screenshots/HIGH%20ATTRITION%20RISK.png)

### 3.2 Low Attrition Risk Example
This example shows an employee with low attrition risk:

![Low Attrition Risk](/screenshots/LOW%20ATTRITION%20RISK.png)

## ⚡ 4. Model Information
The prediction pipeline uses a trained classification model with one-hot encoded role and overtime features. The UI collects the core attributes used by the model to compute a risk probability and classify the profile as low or high risk.

### 4.1 Features Used by the App
- Age
- MonthlyIncome
- JobLevel
- TotalWorkingYears
- OverTime
- JobRole

## 📈 5. Performance Metrics
XGBoost classification report (test split):

- Accuracy: 0.86
- Macro avg (precision/recall/F1): 0.74 / 0.64 / 0.67
- Weighted avg (precision/recall/F1): 0.84 / 0.86 / 0.84
- Non-attrition (False) precision/recall/F1: 0.88 / 0.96 / 0.92
- Attrition (True) precision/recall/F1: 0.60 / 0.32 / 0.42

## 🗂️ 6. Dataset Link
This project uses the IBM HR Analytics Employee Attrition dataset (CSV in this repo). Original source:
- https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

## ⚙️ 7. Installation and Setup

### 7.1 Prerequisites
- Python 3.8+
- pip package manager

### 7.2 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Subhajyoti-Maity/Employee-Attrition-Prediction.git
   cd Employee-Attrition-Prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

### 7.3 Access
- Local URL: http://localhost:8501
- Network URL: http://<your-network-ip>:8501

## 📁 8. Project Structure
```
Employee-Attrition-Prediction/
├── app.py                              # Streamlit app
├── Employee_Attrition_Prediction.ipynb # EDA/training notebook
├── assets/                             # UI assets (logo)
├── best_attrition_model.pkl            # Trained model
├── best_model_columns.pkl              # Model feature list
├── requirements.txt                    # Python dependencies
├── WA_Fn-UseC_-HR-Employee-Attrition.csv  # Dataset
└── screenshots/                        # App screenshots
```

## 🧰 9. Tech Stack
- Streamlit (Web Interface)
- Scikit-learn & XGBoost (Machine Learning)
- Pandas & NumPy (Data Processing)

## 👤 10. Author
- Subhajyoti Maity

## 💬 11. Support and Feedback
If you have questions, issues, or suggestions, please open an issue in the repository or reach out via GitHub discussions.

## 📝 12. Notes
- The app expects best_attrition_model.pkl and best_model_columns.pkl to be present in the project root.
- Use the notebook to explore data or retrain the model if needed.
