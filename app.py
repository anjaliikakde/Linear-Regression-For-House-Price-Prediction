import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("House Price Prediction App")

# User inputs
area = st.number_input("Area (sq ft)", min_value=0)
bedrooms = st.slider("Bedrooms", 1, 10)
bathrooms = st.slider("Bathrooms", 1, 10)
stories = st.slider("Stories", 1, 5)
mainroad = st.selectbox("Main Road", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
parking = st.slider("Parking Spaces", 0, 3)
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])
furnishingstatus = st.selectbox("Furnishing", ["Furnished", "Semi-furnished", "Unfurnished"])

# Encoding inputs
mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0
furnishing_map = {"Furnished": 0, "Semi-furnished": 1, "Unfurnished": 2}
furnishingstatus = furnishing_map[furnishingstatus]

# Prediction
if st.button("Predict"):
    input_data = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
                            hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    st.success(f"Estimated Price: ₹{prediction[0]:,.2f} Lakhs")