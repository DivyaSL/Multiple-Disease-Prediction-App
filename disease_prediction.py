import joblib
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models
# Load Diabetes Model
with open("diabetes_model.sav", "rb") as f:
    diabetes_model = joblib.load(f)

# Load Heart Disease Model
with open("heart_disease_model.sav", "rb") as f:
    heart_disease_model = joblib.load(f)

# sidebar for navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
                           ["Diabetes Prediction",
                            "Heart Disease Prediction"],
                            icons = ["activity", "heart"],
                            default_index = 0)

# Diabetes Prediction Page
if (selected == "Diabetes Prediction"):
    # page title
    st.title("Diabetes Prediction using ML")

    # getting inputs from user
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level")

    with col1:
        BloodPressure = st.text_input("Blood Pressure Value")

    with col2:
        SkinThickness = st.text_input("Skin Thickness Value")

    with col1:
        Insulin = st.text_input("Insulin Level")

    with col2:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes PedigreeFunction Value")

    with col2:
        Age = st.text_input("Age")    


    # Prediction
    diab_diagnosis = ""

    # button for result
    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = "The person is Diabetic"
        else:
            diab_diagnosis = "The person is Not Diabetic"

    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == "Heart Disease Prediction"):
    # page title
    st.title("Heart Disease Prediction using ML")

     # getting inputs from user
    col1, col2 = st.columns(2)

    with col1:
        Age = st.text_input("Age")

    with col2:
        Sex = st.text_input("Sex")

    with col1:
        ChestPainType = st.text_input("Chest Pain Type (4 values)")

    with col2:
        RestingBloodPressure = st.text_input("Resting Blood Pressure")

    with col1:
        SerumCholestoral = st.text_input("Serum Cholestoral in mg/dl")

    with col2:
        FastingBloodSugar = st.text_input("Fasting Blood Sugar > 120 mg/dl")

    with col1:
        RestingElectrocardiographicResults = st.text_input("Resting Electrocardiographic Results (values 0, 1, 2)")

    with col2:
        MaximumHeartRateAchieved = st.text_input("Maximum Heart Rate achieved")    

    with col1:
        ExerciseInducedAngina = st.text_input("Exercise Induced Angina")

    with col2:
        Oldpeak = st.text_input("Oldpeak")    

    with col1:
        PeakExercise = st.text_input("Slope of the peak exercise ST segment")

    with col2:
        VesselsNumber = st.text_input("Number of major vessels (0-3) colored by Flourosopy")    

    with col1:
        Thal = st.text_input("Thal")    


    # Prediction
    heart_diagnosis = ""

    # button for result
    if st.button("Heart Disease Test Result"):
        heart_prediction = heart_disease_model.predict([[Age, Sex, ChestPainType, RestingBloodPressure, SerumCholestoral, FastingBloodSugar, RestingElectrocardiographicResults, MaximumHeartRateAchieved, ExerciseInducedAngina, Oldpeak, PeakExercise, VesselsNumber, Thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = "The person has Heart Disease"
        else:
            heart_diagnosis = "The person does not have Heart Disease"

    st.success(heart_diagnosis)