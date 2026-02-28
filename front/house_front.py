import streamlit as st
import requests

def check_house():
    api_url = 'http://127.0.0.1:8000/house_predict/'

    st.title('House Project')

    gr_liv_area = st.number_input('GrLivArea: ', min_value=0, step=1)
    year_built = st.number_input('Year Built: ', min_value=0, step=1)
    garage_cars = st.number_input('Garage Cars: ', min_value=0, step=1)
    total_bsmt_sf = st.number_input('Total Bsmt: ', min_value=0, step=1)
    full_bath = st.number_input('Full Bath: ', min_value=0, step=1)
    overall_qual = st.number_input('Overall Qual: ', min_value=0, step=1)
    neighborhood = st.selectbox('Neighborhood: ', ['Blmngtn', 'Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr',
                                                   'Crawfor', 'Edwards', 'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel',
                                                   'NAmes', 'NPkVill', 'NWAmes', 'NoRidge', 'NridgHt', 'OldTown',
                                                   'SWISU', 'Sawyer', 'SawyerW', 'Somerst', 'StoneBr', 'Timber',
                                                   'Veenker'])

    house_data = {
        "GrLivArea": gr_liv_area,
        "YearBuilt": year_built,
        "GarageCars": garage_cars,
        "TotalBsmtSF": total_bsmt_sf,
        "FullBath": full_bath,
        "OverallQual": overall_qual,
        "Neighborhood": neighborhood
    }

    if st.button('Send'):
        try:
            answer = requests.post(api_url, json=house_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f"Error: {answer.status_code}")
        except requests.exceptions.RequestException:
            st.error('Fail to connection')
