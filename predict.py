import joblib
import numpy as np

# Load saved files
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

def evaluate_student(attendance, assignment, quiz, mid, study_hours):
    data = np.array([[attendance, assignment, quiz, mid, study_hours]])
    data = scaler.transform(data)
    prediction = model.predict(data)
    return prediction[0]