import streamlit as st
import pandas as pd
import joblib
model=joblib.load("cancer_model.pkl")
scaler=joblib.load("scaler.pkl")
cols=joblib.load("columns.pkl")
st.title("Cancer Predictor by Krrish")
st.markdown("Please Provide the following details")
age=st.slider("AGE",18,100,40)
gender=st.selectbox("GENDER",['M','F'])
bmi=st.slider("BMI",10,50,25)
smoking=st.selectbox("SMOKING",["YES","NO"])
genetic=st.selectbox("GENETIC_RISK_HISTORY",["LOW","MEDIUM","HIGH"])
physical_activity=st.number_input("NUMBER OF HOURS OF PHYSICAL ACTIVITY PER WEEK",0.0,10.0,5.0,step=0.1)
alcohol=st.number_input("ALCHOL UNITS PER WEEK",0.0,5.0,0.0,step=0.1)
cancer_history=st.selectbox("DO YOU HAVE CANCER HISTORY",["YES","NO"])
gender_map = {'F':0, 'M':1}
smoking_map = {'NO':0, 'YES':1}
genetic_map = {'LOW':0, 'MEDIUM':1, 'HIGH':2}
cancer_map = {'NO':0, 'YES':1}

if(st.button("Predict")):
    raw_input={
        'Age':age,
        'Gender':gender_map[gender],
        'BMI':bmi,
        'Smoking':smoking_map[smoking],
        "GeneticRisk":genetic_map[genetic],
        "PhysicalActivity":physical_activity,
        "AlcoholIntake":alcohol,
        "CancerHistory":cancer_map[cancer_history]

    }
    input_df=pd.DataFrame([raw_input])
    scaled_input=scaler.transform(input_df)
    prediction=model.predict(scaled_input)[0]
    if(prediction==1):
        st.error("Cancer Diagnosis Required")
    
    else:
        st.success("Cancer Diagnosis Not Required")