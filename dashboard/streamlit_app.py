

import streamlit as st
import requests

st.title("Diabetes Prediction")

# User inputs
features = {
    "Pregnancies": st.number_input("Pregnancies", 0),
    "Glucose": st.number_input("Glucose", 0),
    "BloodPressure": st.number_input("Blood Pressure", 0),
    "SkinThickness": st.number_input("Skin Thickness", 0),
    "Insulin": st.number_input("Insulin", 0),
    "BMI": st.number_input("BMI", 0.0),
    "DiabetesPedigreeFunction": st.number_input("Diabetes Pedigree Function", 0.0),
    "Age": st.number_input("Age", 1),
}

if st.button("Predict"):
    response = requests.post("http://localhost:5000/predict", json=features)
    prediction = response.json()['prediction']
    st.success(f"Prediction: {prediction}")
