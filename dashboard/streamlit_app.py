import streamlit as st
import numpy as np
import joblib

# Load model directly
model = joblib.load("model/diabetes_model.pkl")

st.title("🧠 Diabetes Prediction App")

# Input fields
preg = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1)

if st.button("Predict"):
    
    features = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("⚠️ You have diabetes.")
    else:
        st.success("✅ You do not have diabetes.")