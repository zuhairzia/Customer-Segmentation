# segmentation.py
import streamlit as st
import pandas as pd
import joblib

# Load trained models
kmeans = joblib.load("kmeans_model.pkl")  # Your trained KMeans model
scaler = joblib.load("scaler.pkl")        # Your trained StandardScaler

# Streamlit app title
st.title("Customer Segmentation App")
st.write("Enter customer details to predict the customer segment.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=35)
income = st.number_input("Income", min_value=0, max_value=200000, value=50000)
total_spending = st.number_input("Total Spending (sum of purchases)", min_value=0, max_value=5000, value=1000)
num_web_purchases = st.number_input("Number of Web Purchases", min_value=0, max_value=100, value=10)
num_store_purchases = st.number_input("Number of Store Purchases", min_value=0, max_value=100, value=10)
num_web_visits = st.number_input("Number of Web Visits per Month", min_value=0, max_value=50, value=3)
recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=365, value=30)

# Create DataFrame from input (column names must match training)
input_data = pd.DataFrame({
    "age": [age],
    "income": [income],
    "total_spending": [total_spending],
    "numwebpurchases": [num_web_purchases],
    "numstorepurchases": [num_store_purchases],
    "numwebvisitsmonth": [num_web_visits],
    "recency": [recency]
})

# Scale the input data
input_scaled = scaler.transform(input_data)

# Prediction button
if st.button("Predict Segment"):
    cluster = kmeans.predict(input_scaled)[0]
    st.success(f"Predicted Segment: Cluster {cluster}")