import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# diabetes_model = pickle.load(
#     open(
#         'D:/Programming/disease_detector/Disease_predictor_webapp/saved files/diabetes_model.sav',
#         'rb'
#     )
# )
diabetes_model = pickle.load(
    open(
        'saved_files/diabetes_model.sav',
        'rb'
    )
)

# slide bar for navigation
with st.sidebar:
    selected = option_menu(
        "Disease you want to check",
        ["Diabetes prediction", "Heart Disease Prediction", "Cancer prediction"],
        icons = ["droplet half", "bandaid", "activity"],
        menu_icon="heart pulse fill",
        default_index=0,
    )

# Diabetis prediction page navigation
if selected == "Diabetes prediction":
    st.title("Diabetes prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies")
        if(Pregnancies<0):
            st.warning('please enter positive numerical value ',icon="⚠️")
            
    with col2:
        Glucose = st.number_input("Glucose Level")
        if(Glucose<0):
            st.warning('please enter positive numerical value ',icon="⚠️")

    with col3:
        BloodPressure = st.number_input("Blood Pressure value")
        if(BloodPressure<0):
            st.warning('please enter positive numerical value ',icon="⚠️")

    with col1:
        SkinThickness = st.number_input("Skin Thickness value")
        if(SkinThickness<0):
            st.warning('please enter positive numerical value ',icon="⚠️")

    with col2:
        Insulin = st.number_input("Insulin Level")
        if(Insulin<0):
            st.warning('please enter positive numerical value ',icon="⚠️")

    with col3:
        BMI = st.number_input("BMI value")
        if(BMI<0):
            st.warning('please enter positive numerical value ',icon="⚠️")

    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value")
        if(DiabetesPedigreeFunction<0):
            st.warning('please enter positive numerical value ',icon="⚠️")

    with col2:
        Age = st.number_input("Age of the Person")
        if(Age<0):
            st.warning('please enter positive numerical value ',icon="⚠️")

    # at first create vacant result
    diabetis_result = ''

    if(Pregnancies == 0 and Glucose == 0 and BloodPressure == 0 and SkinThickness == 0 and Insulin ==0 and BMI==0 and DiabetesPedigreeFunction == 0 and Age == 0):
        diabetis_result = " you did not give any input !!!"
    else:    
        try:
            # create a button for predicton submit
            if st.button("Diabetes Test Result"):
                diabetis_prediction = diabetes_model.predict(
                    [
                        [
                            Pregnancies,
                            Glucose,
                            BloodPressure,
                            SkinThickness,
                            Insulin,
                            BMI,
                            DiabetesPedigreeFunction,
                            Age
                        ]
                    ]
                )
                if diabetis_prediction[0] == 1:
                    diabetis_result = "you are diabetic , consult to a doctor "
                else:
                    diabetis_result = "you are not diabetic , your health is good"
        except:
            diabetis_result = " some error occured please try again later !!!!"

    st.success(diabetis_result)


if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")
    
if selected == "Cancer_prediction":
    st.title("Cancer_prediction")
    
