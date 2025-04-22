import streamlit as st
import numpy as np
import pickle
import os

# Load trained model with reliable path for Streamlit Cloud
model_path = os.path.join(os.path.dirname(__file__), 'crop_model.pkl')
model = pickle.load(open(model_path, 'rb'))

# Page config
st.set_page_config(page_title="🌾 Crop Recommendation", page_icon="🌿")

# Title and description
st.title("🌿 AI-Powered Crop Recommendation System")
st.markdown("Enter soil and environmental data to get the best crop recommendation.")

# Input features
n = st.slider("Nitrogen (N)", 0, 140, 50)
p = st.slider("Phosphorous (P)", 5, 145, 50)
k = st.slider("Potassium (K)", 5, 205, 50)
temperature = st.slider("Temperature (°C)", 10.0, 40.0, 25.0)
humidity = st.slider("Humidity (%)", 10.0, 90.0, 50.0)
ph = st.slider("pH", 3.5, 9.5, 6.5)
rainfall = st.slider("Rainfall (mm)", 20.0, 300.0, 100.0)

# Predict button
if st.button("🌱 Recommend Crop"):
    input_data = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"✅ Recommended Crop: **{prediction[0].capitalize()}**")
