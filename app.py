import streamlit as st
import pandas as pd
import joblib
import os

# --- GET THE ABSOLUTE PATH TO THE DIRECTORY OF THIS SCRIPT ---
# This makes the app work no matter where you run it from
_this_dir = os.path.dirname(os.path.abspath(__file__))

# --- CONSTRUCT THE FULL, ABSOLUTE PATHS FOR YOUR BEST .pkl FILES ---
model_path = os.path.join(_this_dir, 'best_attrition_model.pkl')
columns_path = os.path.join(_this_dir, 'best_model_columns.pkl')


# --- LOAD YOUR SAVED FILES USING THE FULL PATHS ---
try:
    model = joblib.load(model_path)
    model_columns = joblib.load(columns_path)
except FileNotFoundError:
    st.error("Error: Improved model or column file not found. Make sure 'best_attrition_model.pkl' and 'best_model_columns.pkl' are in the same folder as app.py.")
    st.stop()


st.title('Employee Attrition Prediction 🔮')
st.sidebar.header("Enter Employee Details")

# Function to collect user input from the sidebar
def user_input_features():
    age = st.sidebar.slider('Age', 18, 60, 50)
    monthly_income = st.sidebar.slider('Monthly Income ($)', 1000, 20000, 18500)
    job_level = st.sidebar.slider('Job Level', 1, 5, 5)
    total_working_years = st.sidebar.slider('Total Working Years', 0, 40, 25)
    overtime = st.sidebar.selectbox('Works OverTime?', ('No', 'Yes'))
    job_role = st.sidebar.selectbox('Job Role', ('Manager', 'Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director',
                                                 'Healthcare Representative', 'Sales Representative', 'Research Director', 'Human Resources'))

    # Create a dictionary for the input data
    data = {
        'Age': age,
        'MonthlyIncome': monthly_income,
        'JobLevel': job_level,
        'TotalWorkingYears': total_working_years,
        'OverTime': overtime,
        'JobRole': job_role
    }
    
    # Convert the dictionary to a pandas DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display the user's selections
st.subheader("Employee Input Details")
st.write(input_df)

# Prepare the input for the model
input_encoded = pd.get_dummies(input_df)
input_aligned = input_encoded.reindex(columns=model_columns, fill_value=0)


# Create a button to make a prediction
if st.button("Predict Attrition"):
    prediction_input = input_aligned[model_columns]
    
    prediction_proba = model.predict_proba(prediction_input)

    # --- FINAL LOGIC: Apply a business rule on top of the model's prediction ---
    is_stable_manager = (input_df['OverTime'][0] == 'No' and 
                         input_df['JobRole'][0] == 'Manager' and 
                         input_df['JobLevel'][0] >= 4)

    prediction_threshold = 0.75 
    
    st.subheader("Prediction Result")

    # If the employee is a stable manager, classify them as low risk.
    # Otherwise, use the model's prediction with our threshold.
    if is_stable_manager:
        st.success(f"Prediction: Low Attrition Risk")
        st.info("This is a senior manager with a stable profile.")
        st.write(f"Stability Score: {prediction_proba[0][0]*100:.2f}%")
    elif prediction_proba[0][1] > prediction_threshold:
        st.warning(f"Prediction: Potential Attrition Risk Detected")
        st.write(f"Risk Score: {prediction_proba[0][1]*100:.2f}%")
    else:
        st.success(f"Prediction: Low Attrition Risk")
        st.write(f"Stability Score: {prediction_proba[0][0]*100:.2f}%")

