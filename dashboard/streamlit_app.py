import streamlit as st
import requests

# Read API URL from environment variable, or default to localhost
API_URL = os.environ.get("API_URL", "http://localhost:5000")

st.title("Diabetes Prediction App")

# Input form
st.header("Enter Patient Details")
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

if st.button("Predict"):
    features = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    try:
        #response = requests.post("http://localhost:5000/predict", json=features)
        #response = requests.post(f"{API_URL}/predict", json=features)
        response = requests.post("https://diabetes-ai-agent.onrender.com", json=features)
        result = response.json().get('prediction')
        st.success(f"Prediction: {result}")
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to the prediction API. Please ensure the Flask server is running.")
