import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import requests
from all_projects.front.student_front import check_student
from all_projects.front.titanic_front import check_titanic
from all_projects.front.house_front import check_house
from all_projects.front.bank_front import check_bank
from all_projects.front.diabetes_front import check_diabetes
from all_projects.front.avocado_front import check_avocado
from all_projects.front.mushroom_front import check_mushroom
from all_projects.front.telecom_front import check_telecom



with st.sidebar:
    name = st.radio(label='Models: ', options=['Info', 'Student Django', 'Titanic Django', 'House Django', 'Bank Django',
                                               'Diabetes Django', 'Avocado Django', 'Mushroom, Django', 'Telecom Django',
                                               'HR Django'])

if name == 'Info':
    st.title('Welcome')
    st.write('Student — предсказание успеваемости студентов')
    st.write('Titanic — предсказание выживаемости на Титанике')
    st.write('House - предсказание стоимости недвижимости')
    st.write('Bank - банковская аналитика')
    st.write('Diabetes — диагностика диабета')
    st.write('Avocado — предсказание цен на авокадо')
    st.write('Mushroom — классификация грибов')
    st.write('Telecom — отток клиентов телекома')
elif name == 'Student Django':
    check_student()
elif name == 'Titanic Django':
    check_titanic()
elif name == 'House Django':
    check_house()
elif name == 'Bank Django':
    check_bank()
elif name == 'Diabetes Django':
    check_diabetes()
elif name == 'Avocado Django':
    check_avocado()
elif name == 'Mushroom Django':
    check_mushroom()
elif name == 'Telecom Django':
    check_telecom()

