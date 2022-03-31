# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:38:41 2022

@author: somil.mehta
"""

import pandas as pd
import streamlit as st
import pickle 
from PIL import Image

pickle_in = open("model.sav","rb")
model = pickle.load(pickle_in)  




def welcome():
    return "Welcome All"

def heart_attack_prediction(Age,Anaemia,CreatininePhosphokinase,Diabetes,EjectionFraction,HighBloodPressure,Platelets,SerumCreatinine,SerumSodium,Sex,Smoking,Time):
    
    prediction = model.predict([[Age,Anaemia,CreatininePhosphokinase,Diabetes,EjectionFraction,HighBloodPressure,Platelets,SerumCreatinine,SerumSodium,Sex,Smoking,Time]])
    print(prediction)
    return prediction

    #name = st.text_input(label = "Enter Patient Name")
    #submit = st.form_submit_button(label = "Submit this Name")
def main():
    #st.title("Heart Attack Prediction")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;"> Heart Attacks Prediction Web App </h2>
    </div>
    """
    
    
    st.markdown(html_temp,unsafe_allow_html = True)
    Age = st.text_input("Patient Age")
    Anaemia = st.radio("Patient Suffering from Anaemia [YES : 1 & NO : 0]",(1,0))
    CreatininePhosphokinase = st.slider("Creatinine Phosphokinase level",min_value=25.0,max_value=1250.0)
    Diabetes = st.radio("Patient having Diabetes [YES : 1 & NO : 0]",(1,0))
    EjectionFraction = st.slider("Ejection Fraction Percentage",min_value=12.0,max_value=70.0)   
    HighBloodPressure = st.radio("Patient having High Blood Pressure [YES : 1 & NO : 0]",(1,0))
    Platelets = st.slider("Platelets in the blood [kiloplatelets/mL]",min_value=122000.0,max_value=427000.0)
    SerumCreatinine = st.slider("SerumCreatinine",min_value=0.5, max_value=2.5)
    SerumSodium = st.slider("SerumSodium",min_value=125.0,max_value=150.0)
    Sex = st.radio("Sex [MALE : 1 & FEMALE : 0]",(1,0))
    Smoking = st.radio("Does the Patient Smoke [YES : 1 & NO : 0]",(1,0))
    Time = st.slider("Enter Follow-up period (days)",min_value=0,max_value=285)
                          
    result = ""
    if st.button("Predict"):
        result = heart_attack_prediction(Age,Anaemia,CreatininePhosphokinase,Diabetes,EjectionFraction,HighBloodPressure,Platelets,SerumCreatinine,SerumSodium,Sex,Smoking,Time) 
    st.success("Chances of Heart Attack : {}".format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")
        
if __name__=='__main__':
    main()        











