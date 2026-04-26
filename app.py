import streamlit as st
from predict import evaluate_student

st.title("🎓 Student Performance Evaluator")

attendance = st.number_input("Attendance (%)", 0, 100)
assignment = st.number_input("Assignment Marks", 0, 100)
quiz = st.number_input("Quiz Marks", 0, 100)
mid = st.number_input("Mid Exam Marks", 0, 100)
study_hours = st.number_input("Study Hours", 0, 24)

if st.button("Evaluate"):
    result = evaluate_student(attendance, assignment, quiz, mid, study_hours)
    st.success(f"Predicted Result: {result}")