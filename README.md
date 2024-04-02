# Multiple-Disease-Prediction
To view this project : https://multiple-disease-prediction-f3cvshkav5ugmoqlybm6qp.streamlit.app/

## Multi-Disease Diagnosis Assistant
This Streamlit-based web application leverages machine learning models to predict the likelihood of diseases such as diabetes, heart disease, breast cancer, and stroke. Designed with an intuitive user interface, the application provides a seamless experience for users to input their medical parameters and receive instant predictions.

## Features
* Disease Predictions: Offers predictions for four major diseases:

  1. Diabetes: Uses patient data like Glucose Level, Blood Pressure, BMI, etc., to predict diabetes.
  2. Heart Disease: Predicts the presence of heart disease using features such as Age, Sex, Cholesterol levels, and more.
  3. Breast Cancer: Determines whether breast cancer is malignant or benign based on attributes like Mean Radius, Texture, Perimeter, and others.
  4. Stroke: Assesses the risk of stroke through parameters such as Age, BMI, Hypertension status, etc.
* User-Friendly Interface: With Streamlit, the app presents a straightforward navigation sidebar for disease selection and input fields optimized for an efficient user experience.

## How It Works
1. Model Loading: At startup, the application loads pre-trained machine learning models for each disease using pickle.
2. Navigation and Input: Users select the disease prediction they need from the sidebar. They are then prompted to enter relevant health metrics into designated input fields.
3. Prediction: Upon submitting their data, the application utilizes the appropriate machine learning model to predict the likelihood of the disease and displays the results to the user.

## Technologies Used

1. Streamlit: For building and deploying the web application.
2. Pickle: To load pre-trained machine learning models.
3. Streamlit Option Menu: To enhance the sidebar with a navigable menu.

This project showcases the potential of combining machine learning with web applications to provide valuable health insights to users, potentially aiding in early disease detection and awareness.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
