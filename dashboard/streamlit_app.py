import streamlit as st
import requests
import os
import numpy as np

# 🔁 Read the API base URL from an environment variable (default to localhost)
API_URL = os.environ.get("API_URL", "http://localhost:5000")

st.title("🧠 Diabetes Prediction")

# Collect user inputs
preg = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1)

if st.button("Predict"):
    features = {
        "pregnancies": preg,
        "glucose": glucose,
        "blood_pressure": bp,
        "skin_thickness": skin,
        "insulin": insulin,
        "bmi": bmi,
        "diabetes_pedigree_function": dpf,
        "age": age
    }

    try:
        #response = requests.post(f"{API_URL}/predict", json=features)
        response = requests.post(f"https://diabetes-ai-agent.onrender.com/predict", json=features)
        https://diabetes-ai-agent.onrender.com
        prediction = response.json().get("prediction")

        if prediction == 1:
            st.error("⚠️ You have diabetes.**")
        else:
            st.success("✅ You do not have diabetes.**")
    except requests.exceptions.RequestException as e:
        st.error("Failed to connect to the prediction API.")
        st.text(f"Error details: {e}")
