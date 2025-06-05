

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('model/diabetes_model.pkl')

@app.route('/')
def home():
    return "Diabetes Prediction API is running."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([data['Pregnancies'], data['Glucose'], data['BloodPressure'],
                         data['SkinThickness'], data['Insulin'], data['BMI'],
                         data['DiabetesPedigreeFunction'], data['Age']]).reshape(1, -1)

    prediction = model.predict(features)[0]
    result = 'Diabetic' if prediction == 1 else 'Non-Diabetic'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host = "0.0.0.0", port = 5000)
