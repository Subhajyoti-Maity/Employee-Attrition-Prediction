## Accessing the App

After running the Streamlit application, you will see output in your terminal similar to:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://<your-network-ip>:8501
```

- **Local URL**: Open [http://localhost:8501](http://localhost:8501) in your web browser to use the app on your machine.
- **Network URL**: Use the network URL to access the app from another device on the same network (replace `<your-network-ip>` with your actual IP address).

# Employee Attrition Prediction

## Demo Screenshots

Below are screenshots of the Employee Attrition Prediction app in action:

### 1. High Attrition Risk Prediction
![High Attrition Risk](/screenshots/high_attrition_risk.png)

### 2. Low Attrition Risk Prediction (Stable Manager)
![Low Attrition Risk](/screenshots/low_attrition_risk.png)

# Employee Attrition Prediction

## Project Structure

```
EMPLOYEE-ATTRITION-PREDICTION/
│
├── app.py                   # Streamlit web application
├── best_attrition_model.pkl # Trained XGBoost model for prediction
├── best_model_columns.pkl   # Feature columns used by the model
└── README.md                # Project documentation
```

Each file serves the following purpose:
- `app.py`: Main application file to run the Streamlit web app.
- `best_attrition_model.pkl`: Serialized machine learning model for attrition prediction.
- `best_model_columns.pkl`: List of feature columns expected by the model.
- `README.md`: Documentation and instructions for the project.

# Employee Attrition Prediction

## Project Overview
This project is an end-to-end machine learning solution designed to predict employee attrition within a company. By analyzing various employee attributes from the IBM HR Analytics dataset, the model identifies individuals who are at a high risk of leaving their jobs. The final output is an interactive web application built with Streamlit that allows HR personnel to input employee details and receive a real-time risk assessment.

The project covers the complete machine learning lifecycle, from data exploration and preprocessing to model training, hyperparameter tuning, and deployment as a user-friendly tool.

## Problem Statement
Voluntary employee turnover is a significant cost for companies, leading to loss of talent, recruitment expenses, and reduced productivity. The HR department needs a data-driven tool to proactively identify employees who are likely to leave. This project aims to solve this by building a predictive model that can serve as an early warning system, enabling management to implement retention strategies for high-risk employees.

## Dataset
The project utilizes the IBM HR Analytics Employee Attrition & Performance dataset, which is publicly available on Kaggle.

**Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

**Description:** The dataset contains 1,470 employee records with 35 diverse features, including demographic information, job satisfaction scores, compensation details, and work history. The target variable is Attrition (Yes/No).

## Tech Stack & Libraries
- **Programming Language:** Python 3.12
- **Data Analysis & Manipulation:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost
- **Imbalanced Data Handling:** Imbalanced-learn (for SMOTE)
- **Web Application:** Streamlit
- **Development Environment:** Google Colab (for model training), VS Code (for app development)

## Project Workflow & Methodology
The project followed a structured machine learning workflow:

**Exploratory Data Analysis (EDA):** The dataset was analyzed to understand its structure and uncover initial insights. The most critical finding was a significant class imbalance, with only 16% of employees having left the company.

**Data Preprocessing:**
- Removed irrelevant columns (EmployeeNumber, StandardHours, etc.).
- Converted all categorical features (e.g., JobRole, Department) into a numerical format using one-hot encoding.

**Handling Class Imbalance:**
The SMOTE (Synthetic Minority Over-sampling Technique) was applied to the training data. This created synthetic examples of the minority class (employees who left) to create a balanced 50/50 dataset for the model to learn from.

**Model Training & Tuning:**
- A baseline RandomForestClassifier was initially trained.
- An XGBClassifier was then trained, which showed improved performance.
- A key challenge emerged: the model was overly sensitive and produced too many "false alarms" (predicting "leave" for stable employees). To solve this, Hyperparameter Tuning was performed using GridSearchCV. The search was optimized for precision to make the model more careful and reduce false positives.

**Final App Logic:**
Even after tuning, the model struggled with certain high-stability profiles. A final "business rule" was added to the application logic to override the model's prediction for senior managers (Job Level >= 4) who do not work overtime, classifying them as "Low Attrition Risk." This combines machine learning with domain knowledge for a more practical and reliable tool.

## How to Run the Project Locally
To run the Streamlit application on your local machine, follow these steps:

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository (or Create a Project Folder)
Create a new folder on your computer and place the following files inside it:
- `app.py`
- `best_attrition_model.pkl`
- `best_model_columns.pkl`

### Step 2: Create a Virtual Environment (Recommended)
Open a terminal in your project folder and create a virtual environment:
```bash
python -m venv .venv
```

Activate the environment:
- On Windows:
  ```bash
  .\.venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### Step 3: Install the Required Libraries
In the same terminal, install all the necessary packages:
```bash
pip install streamlit pandas scikit-learn xgboost
```

### Step 4: Run the Streamlit Application
Launch the application with the following command:
```bash
streamlit run app.py
```

The application will automatically open in a new tab in your web browser.

## Results & Key Findings
The final, tuned XGBoost model, combined with the business rule, provides a reliable tool for assessing attrition risk.

The project highlighted the critical challenge of class imbalance and the trade-off between precision and recall. Optimizing for precision proved essential for creating a practical tool that minimizes false alarms.

Key predictors of attrition in the dataset were found to be OverTime, Job Level, and Monthly Income.

## Future Improvements
- **Advanced Feature Engineering:** Create more complex features, such as the ratio of an employee's income to the average income for their job role.
- **Experiment with Other Models:** Test other classification algorithms like LightGBM or CatBoost.
- **Deploy to the Cloud:** Deploy the Streamlit application to a cloud service like Streamlit Community Cloud or Heroku to make it accessible online.

## License
This project is for educational purposes.
