import pickle
import streamlit as st
from streamlit_option_menu import option_menu

primaryColor="green"
backgroundColor="#0E1117"
secondaryBackgroundColor="#262730"
textColor="#FAFAFA"
font="sans serif"


diabetes_model = pickle.load(
    open(
        'D:/Programming/disease_detector/Disease_predictor_webapp/saved_files/diabetes_model.sav',
        'rb'
    )
)

heart_disease_model=pickle.load(open('D:/Programming/disease_detector/Disease_predictor_webapp/saved_files/heart_disease_model.sav',
        'rb'))


# diabetes_model = pickle.load(
#     open(
#         'saved_files/diabetes_model.sav',
#         'rb'
#     )
# )

# heart_disease_model = pickle.load(
#     open(
#         'saved_files/heart_disease_model.sav',
#         'rb'
#     )
# )

# slide bar for navigation
with st.sidebar:
    selected = option_menu(
        "Disease you want to check",
        ["Diabetes Prediction", "Heart Disease Prediction", "Cancer Prediction"],
        icons = ["droplet half", "bandaid", "activity"],
        menu_icon="heart pulse fill",
        default_index=0,
    )





# Diabetis prediction page navigation
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies",0,30,1)
            
    with col2:
        Glucose = st.number_input("Glucose Level",0,1000,1)

    with col3:
        BloodPressure = st.number_input("Blood Pressure value",0,300,1)

    with col1:
        SkinThickness = st.number_input("Skin Thickness value",0,200,1)

    with col2:
        Insulin = st.number_input("Insulin Level",0,2000,1)

    with col3:
        BMI = st.number_input("BMI value")
        if(BMI<0):
            st.warning('please enter positive numerical value ',icon="⚠️")

    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value")
        if(DiabetesPedigreeFunction<0):
            st.warning('please enter positive numerical value ',icon="⚠️")

    with col2:
        Age = st.number_input("Age of the Person",0,150,1)

    # at first create vacant result
    diabetis_result = ''

    if(BMI == 0 and DiabetesPedigreeFunction == 0):
        diabetis_result = " you did not give all required inputs !!!"
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








# Heart Disease prediction page navigation
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age",0,150,1)
            
    
    with col2:
        cp = st.number_input("Chest pain types",0,3,1)

    with col3:
        sex = st.radio("Sex",["Male","Female"])
        if(sex == "Male"):
            sex=1
        else:
            sex=0

    with col1:
        trestbps = st.number_input("Resting Blood Pressure mm Hg",0,500,1)

    with col2:
        chol = st.number_input("Serum Cholestoral in mg/dl",0,1000,1)

    with col3:
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl",["Yes","No"])
        if(fbs =="Yes"):
            fbs = 1
        else:
            fbs = 0

    with col1:
        restecg = st.number_input("Resting Electrocardiography results",0,2,1)

    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved",0,500,1)

    with col3:
        exang = st.radio("Exercise Induced Angina",["Yes","No"])
        if(exang=="Yes"):
            exang=1
        else:
            exang=0

    with col1:
        oldpeak = st.number_input("ST depression induced by exercise")
        if(oldpeak<0):
            st.warning('please enter positive numerical value ',icon="⚠️")
            
    with col2:
        slope = st.number_input("Slope of the peak exercise ST segment ",0,2,1)

    with col3:
        thal=st.radio("Thal",["Normal","Fixed defect","Reversable defect"])
        if(thal == "Normal"):
            thal = 0
        elif(thal == "Fixed defect"):
            thal = 1
        else:
            thal = 2

    with col1:
        ca = st.number_input("Major vessels colored by fluoroscopy",0,3,1)

    # at first create vacant result
    heart_disease_result = ''

    if(age == 0 and sex == 0 and cp == 0 and trestbps == 0 and chol ==0 and fbs ==0 and restecg == 0 and thalach == 0 and exang == 0 and oldpeak == 0 and slope == 0 and ca ==0 and thal == 0):
        heart_disease_result = " you did not give any input !!!"
    else:    
        try:
            # create a button for predicton submit
            if st.button("Heart Disease Result"):
                heart_disease_prediction = heart_disease_model.predict(
                    [
                        [
                            age,
                            sex,
                            cp,
                            trestbps,
                            chol,
                            fbs,
                            restecg,
                            thalach,
                            exang,
                            oldpeak,
                            slope,
                            ca,
                            thal
                        ]
                    ]
                )
                if heart_disease_prediction[0] == 1:
                    heart_disease_result = "your Heart is not good!! , consult to a doctor "
                else:
                    heart_disease_result = "your Heart is good , Enjoy!!"
        except:
            heart_disease_result = " some error occured please try again later !!!!"

    st.success(heart_disease_result)
    
if selected == "Cancer Prediction":
    st.title("Cancer Prediction")
    
