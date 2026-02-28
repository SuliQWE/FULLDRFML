import streamlit as st
import requests

def check_titanic():
    st.title('Titanic Project')

    api_url = 'http://127.0.0.1:8000/titanic_predict/'

    pclass = st.number_input('Pclass: ', min_value=0, step=1)
    sex = st.selectbox('Sex: ', ['male', 'female'])
    age = st.number_input('Age: ', min_value=0, step=1)
    sib_sp = st.number_input('Sib SP: ', min_value=0, step=1)
    parch = st.number_input('Parch: ', min_value=0, step=1)
    fare = st.number_input('Fare: ', min_value=0.0, step=1.0)
    sib_parch = st.number_input('Sib Parch: ', min_value=0, step=1)
    embarked = st.selectbox('Embarked: ', ['C', 'Q', 'S'])

    titanic_data = {
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sib_sp,
        "Parch": parch,
        "Fare": fare,
        "SibParch": sib_parch,
        "Embarked": embarked
    }

    if st.button('Send'):
        try:
            answer = requests.post(api_url, json=titanic_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(f"Result: {result.get('Predict')}")
            else:
                st.error(f"Error: {answer.status_code}")
        except requests.exceptions.RequestException:
            st.error(f"Fail to connection")
