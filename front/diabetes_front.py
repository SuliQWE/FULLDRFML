import streamlit as st
import requests

def check_diabetes():
    st.title('Diabetes Project')

    api_url = 'http://127.0.0.1:8000/diabetes_predict/'

    pregnancies = st.number_input('Pregnancies: ', min_value=0, step=1)
    glucose = st.number_input('Glucose: ', min_value=0, step=1)
    blood_pressure = st.number_input('Blood Pressure: ', min_value=0, step=1)
    skin_thickness = st.number_input('Skin Thickness: ', min_value=0, step=1)
    insulin = st.number_input('Insulin: ', min_value=0, step=1)
    bmi = st.number_input('BMI: ', min_value=0.0, step=1.0)
    diabetes_pedigree = st.number_input('Diabetes Pedigree Function: ', min_value=0.0, step=1.0)
    age = st.number_input('Age: ', min_value=0, step=1)

    diabetes_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree,
        "Age": age
    }

    if st.button('Send'):
        try:
            answer = requests.post(api_url, json=diabetes_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f"Error: {answer.status_code}")
        except requests.exceptions.RequestException:
            st.error(f"Fail to connection")
