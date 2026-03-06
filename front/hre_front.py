import streamlit as st
import requests

def check_hre():

    st.title('HRE Attrition')

    api_url = 'http://127.0.0.1:8000/hre_predict/'

    Age = st.number_input('Age', 18, 100, 30)
    BusinessTravel = st.selectbox('BusinessTravel', ['Travel_Frequently', 'Travel_Rarely', 'Non-Travel'])
    DailyRate = st.number_input('DailyRate', 0)
    Department = st.selectbox('Department', ['Research & Development', 'Sales', 'Human Resources'])
    DistanceFromHome = st.number_input('DistanceFromHome', 0)
    Education = st.number_input('Education', 1, 5, 3)
    EducationField = st.selectbox('EducationField',
                                  ['Life Sciences', 'Marketing', 'Medical', 'Other', 'Technical Degree'])
    EnvironmentSatisfaction = st.number_input('EnvironmentSatisfaction', 1, 4, 2)
    Gender = st.selectbox('Gender', ['Male', 'Female'])
    HourlyRate = st.number_input('HourlyRate', 0)
    JobInvolvement = st.number_input('JobInvolvement', 1, 4, 2)
    JobLevel = st.number_input('JobLevel', 1, 5, 1)
    JobRole = st.selectbox('JobRole', ['Human Resources', 'Laboratory Technician', 'Manager', 'Manufacturing Director',
                                       'Research Director', 'Research Scientist', 'Sales Executive',
                                       'Sales Representative'])
    JobSatisfaction = st.number_input('JobSatisfaction', 1, 4, 2)
    MaritalStatus = st.selectbox('MaritalStatus', ['Married', 'Single', 'Divorced'])
    MonthlyIncome = st.number_input('MonthlyIncome', 0)
    MonthlyRate = st.number_input('MonthlyRate', 0)
    NumCompaniesWorked = st.number_input('NumCompaniesWorked', 0)
    OverTime = st.selectbox('OverTime', ['Yes', 'No'])
    PercentSalaryHike = st.number_input('PercentSalaryHike', 0)
    PerformanceRating = st.number_input('PerformanceRating', 1, 4, 3)
    RelationshipSatisfaction = st.number_input('RelationshipSatisfaction', 1, 4, 2)
    StockOptionLevel = st.number_input('StockOptionLevel', 0)
    TotalWorkingYears = st.number_input('TotalWorkingYears', 0)
    TrainingTimesLastYear = st.number_input('TrainingTimesLastYear', 0)
    WorkLifeBalance = st.number_input('WorkLifeBalance', 1, 4, 2)
    YearsAtCompany = st.number_input('YearsAtCompany', 0)
    YearsInCurrentRole = st.number_input('YearsInCurrentRole', 0)
    YearsSinceLastPromotion = st.number_input('YearsSinceLastPromotion', 0)
    YearsWithCurrManager = st.number_input('YearsWithCurrManager', 0)

    hre_data = {
        'Age': Age,
        'BusinessTravel': BusinessTravel,
        'DailyRate': DailyRate,
        'Department': Department,
        'DistanceFromHome': DistanceFromHome,
        'Education': Education,
        'EducationField': EducationField,
        'EnvironmentSatisfaction': EnvironmentSatisfaction,
        'Gender': Gender,
        'HourlyRate': HourlyRate,
        'JobInvolvement': JobInvolvement,
        'JobLevel': JobLevel,
        'JobRole': JobRole,
        'JobSatisfaction': JobSatisfaction,
        'MaritalStatus': MaritalStatus,
        'MonthlyIncome': MonthlyIncome,
        'MonthlyRate': MonthlyRate,
        'NumCompaniesWorked': NumCompaniesWorked,
        'OverTime': OverTime,
        'PercentSalaryHike': PercentSalaryHike,
        'PerformanceRating': PerformanceRating,
        'RelationshipSatisfaction': RelationshipSatisfaction,
        'StockOptionLevel': StockOptionLevel,
        'TotalWorkingYears': TotalWorkingYears,
        'TrainingTimesLastYear': TrainingTimesLastYear,
        'WorkLifeBalance': WorkLifeBalance,
        'YearsAtCompany': YearsAtCompany,
        'YearsInCurrentRole': YearsInCurrentRole,
        'YearsSinceLastPromotion': YearsSinceLastPromotion,
        'YearsWithCurrManager': YearsWithCurrManager
    }

    if st.button('Check'):
        try:
            answer = requests.post(api_url, json=hre_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(result['hre_label'])
                st.write(result['probability'])
                st.write(result['risk_level'])
                st.write(result['message'])
            else:
                st.error('Error API')
        except requests.exceptions.RequestException:
            st.error('No Connection!')