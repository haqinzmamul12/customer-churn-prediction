import streamlit as st
from datetime import datetime
import pandas as pd


from src.train import predict

st.title("Customer Churn Prediction")

st.markdown("### Enter Customer Details")

# Form for input
with st.form(key='churn_form'):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=100, step=1)
    total_purchase = st.number_input("Total Purchase", min_value=0.0, format="%.2f")
    account_manager = st.checkbox("Has Account Manager?")
    years = st.number_input("Years as Customer", min_value=0.0, format="%.1f")
    num_sites = st.number_input("Number of Sites", min_value=0, step=1)
    onboard_date = st.date_input("Onboard Date")
    onboard_time = st.time_input("Onboard Time", value=datetime.now().time())
    location = st.text_input("Location")
    company = st.text_input("Company")

    submit = st.form_submit_button(label='Predict Churn')

if submit:
    # Combine date and time
    onboard_datetime = datetime.combine(onboard_date, onboard_time)

    # Prepare data
    input_data = {
        "Names": name,
        "Age": age,
        "Total_Purchase": total_purchase,
        "Account_Manager": int(account_manager),  # convert bool to 0/1
        "Years": years,
        "Num_Sites": num_sites,
        "Onboard_date": onboard_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        "Location": location,
        "Company": company
    }

    # Optional: convert to DataFrame row if predict_from_input expects it
    input_df = pd.DataFrame([input_data])

    # Get prediction
    prediction = predict(input_df)
    customer_status ="Customer will leave." if int(prediction[0]) else "Customer will continue."

    # Display result
    st.subheader("Prediction Result")
    st.write("Churn Prediction:", customer_status)
