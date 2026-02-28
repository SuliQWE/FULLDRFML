import streamlit as st
import requests

def check_avocado():
    st.title('Avocado Project')

    api_url = 'http://127.0.0.1:8000/avocado_predict/'

    firmness = st.number_input('Firmness: ', min_value=0.0, step=1.0)
    hue = st.number_input('Hue: ', min_value=0, step=1)
    saturation = st.number_input('Saturation: ', min_value=0, step=1)
    brightness = st.number_input('Brightness: ', min_value=0, step=1)
    sound_db = st.number_input('Sound db: ', min_value=0, step=1)
    weight_g = st.number_input('Weight g: ', min_value=0, step=1)
    size_cm3 = st.number_input('Size cm3: ', min_value=0, step=1)
    color_category = st.selectbox('Color category: ', ['black', 'dark green', 'green', 'purple'])

    avocado_data = {
        "firmness": firmness,
        "hue": hue,
        "saturation": saturation,
        "brightness": brightness,
        "sound_db": sound_db,
        "weight_g": weight_g,
        "size_cm3": size_cm3,
        "color_category": color_category
    }

    if st.button('Send'):
        try:
            answer = requests.post(api_url, json=avocado_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f"Error: {answer.status_code}")
        except requests.exceptions.RequestException:
            st.error('Fail to connection')
