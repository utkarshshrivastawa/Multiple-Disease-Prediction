# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:15:01 2024

@author: utkar
"""
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


# loding the saved model 

diabetes_model = pickle.load(open("diabetes_model.sav",'rb'))

heart_disease_model = pickle.load(open("heart_model.sav",'rb'))

breast_cancer_model = pickle.load(open("breast_model.sav",'rb'))

stroke_model = pickle.load(open("stroke_model.sav",'rb'))

# Navigation 

with st.sidebar:
    
    selected = option_menu("Multi-disease Diagnosis Assistant",
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction',
                            'Stroke Prediction'],
                           
                           icons =['clipboard2-pulse','heart-pulse','hospital','person-dash'],
                           
                           default_index = 0 )
    
# Diabetes Prediction Page 
if (selected == 'Diabetes Prediction'):
    
    # page title 
    st.title('Diabetes Prediction Using ML')
    
    # getting the input data from the user 
    col1,col2,col3 = st.columns(3)
    with col1:	
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('BloodPressure value')
    with col1:
        SkinThickness = st.text_input('SkinThickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value' ) 
    with col2:
        Age = st.text_input('Age of the Person')
      
    
    
    # code for prediction 
    diab_diagnosis = ''
    # creating a button for prediction 
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction == 1):
            diab_diagnosis= "The person is diabetes"
        else :
            diab_diagnosis="The person is non-diabetes"
            
    st.success(diab_diagnosis)
   
if (selected == 'Heart Disease Prediction'):
    
    # page title 
    st.title('Heart Disease Prediction Using ML')
    # getting the input data from the user 
    col1,col2,col3 = st.columns(3)
    with col1:	
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
       trestbps  = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results' ) 
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
       exang  = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST')
    with col3:
        ca = st.text_input('No. of major vessels (0-3) colored by flourosopy')
    with col1:
        thal = st.text_input('0 = Normal; 1 = Fixed defect; 2 = Reversable defect')
    
    # Convert all inputs to numeric values. Use float or int as appropriate
    age = int(age)
    sex = int(sex)
    cp = int(cp)
    trestbps = int(trestbps)
    chol = int(chol)
    fbs = int(fbs)
    restecg = int(restecg)
    thalach = int(thalach)
    exang = int(exang)
    oldpeak = float(oldpeak)
    slope = int(slope)
    ca = int(ca)
    thal = int(thal)
    
    
    # code for prediction 
    heart_diagnosis = ''
    # creating a button for prediction 
    if st.button('Heart Test Result'):
        
        heart_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = "The person have heart disease"
        else :
            heart_diagnosis="The person does not have heart disease"
            
    st.success(heart_diagnosis)
    
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction Using ML')
    
    # getting the input data from the user 
    col1, col2, col3 = st.columns(3)
    
    with col1:    
        mean_radius = st.text_input('Radius of Lobes')
    with col2:
        mean_texture = st.text_input('Mean of Surface Texture')
    with col3:
        mean_perimeter = st.text_input('Outer Perimeter of Lobes')
    with col1:
         mean_area = st.text_input('Mean Area of Lobes')
    with col2:
         mean_smoothness = st.text_input('Mean of Smoothness Levels')
    with col3:
        mean_compactness = st.text_input('Mean of Compactness')
    with col1:
        mean_concavity = st.text_input('Mean of Concavity') 
    with col2:
        mean_concave_points = st.text_input('Mean of Concave Points')
    with col3:
        mean_symmetry = st.text_input('Mean of Symmetry')
    with col1:    
        mean_fractal_dimension = st.text_input('Mean of Fractal Dimension')
    with col2:
        radius_error = st.text_input('SE of Radius')
    with col3:
        texture_error = st.text_input('SE of Texture')
    with col1:
         perimeter_error = st.text_input('SE of Perimeter')
    with col2:
         area_error = st.text_input('SE of Area')
    with col3:
        smoothness_error = st.text_input('SE of Smoothness')
    with col1:
         compactness_error = st.text_input('SE of Compactness') 
    with col2:
         concavity_error = st.text_input('SE of Concavity')
    with col3:
        concave_points_error = st.text_input('SE of Concave Points')
    with col1:    
         symmetry_error = st.text_input('SE of Symmetry')
    with col2:
        fractal_dimension_error = st.text_input('SE of Fractal Dimension')
    with col3:
        worst_radius = st.text_input('Worst Radius')
    with col1:
         worst_texture = st.text_input('Worst Texture')
    with col2:
         worst_perimeter = st.text_input('Worst Perimeter')
    with col3:
        worst_area = st.text_input('Worst Area')
    with col1:
         worst_smoothness = st.text_input('Worst Smoothness') 
    with col2:
         worst_compactness = st.text_input('Worst Compactness')
    with col3:
        worst_concavity = st.text_input('Worst Concavity')
    with col1:
         worst_concave_points = st.text_input('Worst Concave Points') 
    with col2:
         worst_symmetry = st.text_input('Worst Symmetry')
    with col3:
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')

    # Assuming all your input variables are already defined and received as strings from Streamlit's text_input

    mean_radius = float(mean_radius)
    mean_texture = float(mean_texture)
    mean_perimeter = float(mean_perimeter)
    mean_area = float(mean_area)
    mean_smoothness = float(mean_smoothness)
    mean_compactness = float(mean_compactness)
    mean_concavity = float(mean_concavity)
    mean_concave_points = float(mean_concave_points)
    mean_symmetry = float(mean_symmetry)
    mean_fractal_dimension = float(mean_fractal_dimension)
    radius_error = float(radius_error)
    texture_error = float(texture_error)
    perimeter_error = float(perimeter_error)
    area_error = float(area_error)
    smoothness_error = float(smoothness_error)
    compactness_error = float(compactness_error)
    concavity_error = float(concavity_error)
    concave_points_error = float(concave_points_error)
    symmetry_error = float(symmetry_error)
    fractal_dimension_error = float(fractal_dimension_error)
    worst_radius = float(worst_radius)
    worst_texture = float(worst_texture)
    worst_perimeter = float(worst_perimeter)
    worst_area = float(worst_area)
    worst_smoothness = float(worst_smoothness)
    worst_compactness = float(worst_compactness)
    worst_concavity = float(worst_concavity)
    worst_concave_points = float(worst_concave_points)
    worst_symmetry = float(worst_symmetry)
    worst_fractal_dimension = float(worst_fractal_dimension)

    
    # code for prediction 
    cancer_diagnosis = ''
    # creating a button for prediction 
    if st.button('Breast Cancer Test Result'):
        cancer_prediction = breast_cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
        
        if (cancer_prediction[0] == 0):
            cancer_diagnosis= "The Breast cancer is Malignant"
        else :
            cancer_diagnosis="The Breast Cancer is Benign"
            
    st.success(cancer_diagnosis)
    
    
if (selected== 'Stroke Prediction'):
    
    # page title 
    st.title('Stroke Prediction Using ML')
    
    # getting the input data from the user 
    col1,col2,col3 = st.columns(3)
    with col1:	
        age = st.text_input('Age')
    with col2:
        avg_glucose_level = st.text_input('Average Glucose Level')
    with col3:
        bmi = st.text_input('Body mass index')
    with col1:
       gender_Male  = st.text_input('Gender')
    with col2:
        hypertension_1 = st.text_input('Patient has hypertension or Not')
    with col3:
        heart_disease_1 = st.text_input('Patient has heart disease or Not ')
    with col1:
        ever_married_Yes = st.text_input('Married' ) 
    with col2:
        work_type_Never_worked = st.text_input('Never Worked')
    with col3:
       work_type_Private = st.text_input('Private')
    with col1:
        work_type_Self_employed = st.text_input('Self Employed')
    with col2:
        work_type_children = st.text_input('Children')
    with col3:
        Residence_type_Urban = st.text_input('Residence type')
    with col1:
        smoking_status_formerly_smoked = st.text_input('Formerly Smoked')
    with col2:
        smoking_status_never_smoked = st.text_input('Never Smoked')
    with col3:
        smoking_status_smokes = st.text_input('Status Smokes')
    
   
    
    
    # code for prediction 
    stroke_diagnosis = ''
    # creating a button for prediction 
    if st.button('Stroke Test Result'):
        
        stroke_prediction =stroke_model.predict([[age,avg_glucose_level,bmi,gender_Male,hypertension_1,heart_disease_1,ever_married_Yes,work_type_Never_worked,work_type_Private,work_type_Self_employed,work_type_children,Residence_type_Urban,smoking_status_formerly_smoked,smoking_status_never_smoked,smoking_status_smokes]])
        
        if (stroke_prediction == True):
            stroke_diagnosis = "The person is suffering from Stroke"
        else :
            stroke_diagnosis="The peoson is normal"
            
    st.success(stroke_diagnosis)