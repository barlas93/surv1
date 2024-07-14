# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: siddhardhan
"""

import pickle
import streamlit as st


loaded = pickle.load(open('model.save','rb'))

st.title('Survival Prediction at 12 months')


# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Age = st.text_input('Age')
    
with col2:
    Sex = st.text_input('Sex')

with col3:
    BMI = st.text_input('BMI')

with col1:
    Diagnosis = st.text_input('Diagnosis')

with col2:
    Location = st.text_input('Location')

with col3:
    Resection = st.text_input('Resection Length (mm)')

with col1:
    Infection = st.text_input('History of Infection')

with col2:
    CT = st.text_input('Chemotherapy')

with col3:
    RT = st.text_input('Radiation')
    
with col1:
    Revision = st.text_input('Total number of surgeries')
    
# code for Prediction
survival_diagnosis = ''

# creating a button for Prediction

if st.button('Diabetes Test Result'):
    survival_prediction = loaded.predict([[Age, Sex, BMI, Diagnosis, Location, Resection, Infection, CT, RT, Revision]])
    
    if (survival_prediction[0] == 1):
      survival_diagnosis = 'The implant is more likely to survive'
    else:
      survival_diagnosis = 'The implant is more likely to fail'
    
st.success(survival_diagnosis)



















