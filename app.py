import streamlit as st
import joblib
import numpy as np

model = joblib.load("diabetes_model.pkl")

st.title("Diabetes Prediction App")

st.header("Pateint Details")

preg = st.number_input("Pregnancies",0,20)
glucose = st.number_input("Glucose Level",0,300)
bp = st.number_input("Blood Pressure",0,180)
skin = st.number_input("Skin Thickness",0,100)
insulin =st.number_input("Insulin",0,900)
bmi = st.number_input("BMI",0,70,0)
dpf = st.number_input("Diabetes Pedigree Function",0.0,3.0)
age = st.number_input("Age",1,120)

if st.button("Predict"):
    input_data = np.array([[preg,glucose,bp,skin,insulin,bmi,dpf,age]])
    prediction = model.predict(input_data)
    result = "Diabetic" if prediction[0]==1 else "Not Diabetic"
    st.success(f"prediction Result:{result}")
