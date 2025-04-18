import streamlit as st
from prediction import prediction,feature_names

st.title("Breast Cancer Prediction App (Random Forest)")
st.write("Enter the tumor's measurements below:")

input_data = []

with st.form("prediction_form"):
    for feature in feature_names:
        val = st.number_input(f"{feature.replace('_', ' ').title()}", min_value=0.0)
        input_data.append(val)
    submitted = st.form_submit_button("Predict")

if submitted:
    result = prediction(input_data)
    st.success(f"The model predicts: **{result}**")


