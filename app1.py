import streamlit as st
import pandas as pd
import pickle


pickle_in = open("E:/rf1.pkl", "rb") 
classifier = pickle.load(pickle_in)

def predict_note_authentication(Age, BMI, Level_of_Hemoglobin ,Genetic_Pedigree_Coefficient, Physical_activity, salt_content_in_the_diet, alcohol_consumption_per_day, Chronic_kidney_disease, Adrenal_and_thyroid_disorders):
    prediction = classifier.predict([[Age, BMI, Level_of_Hemoglobin ,Genetic_Pedigree_Coefficient, Physical_activity, salt_content_in_the_diet, alcohol_consumption_per_day, Chronic_kidney_disease, Adrenal_and_thyroid_disorders]])
    print(prediction)
    return prediction


def main():

    st.title("Blood Pressure Disease Predictor")

    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">The Smart Way To Handle Your Pressure </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    Age  =  st.number_input("Age")

    BMI = st.number_input("BMI")

    Genetic_Pedigree_Coefficient = st.number_input("Genetic_Pedigree_Coefficient")

    Physical_activity = st.number_input("Physical_activity")

    salt_content_in_the_diet = st.number_input("salt_content_in_the_diet")

    alcohol_consumption_per_day = st.number_input("alcohol_consumption_per_day")

    Chronic_kidney_disease = st.number_input("Chronic_kidney_disease")

    Adrenal_and_thyroid_disorders = st.number_input("Adrenal_and_thyroid_disorders")

    Level_of_Hemoglobin = st.number_input("Level_of_Hemoglobin")

    result= ""

    if st.button("Predict"):
        result = predict_note_authentication(Age, BMI, Level_of_Hemoglobin, Genetic_Pedigree_Coefficient, Physical_activity, salt_content_in_the_diet, alcohol_consumption_per_day, Chronic_kidney_disease, Adrenal_and_thyroid_disorders)
    st.success('The Blood Pressure Prediction is {}'.format(result))



if __name__=='__main__':
    main()