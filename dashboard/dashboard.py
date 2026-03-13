import streamlit as st
import requests

st.title("Smart Factory Predictive Maintenance")

temperature = st.slider("temperature", 50, 100)
vibration = st.slider("vibration", 0.1, 1.0)
pressure = st.slider("pressure", 20, 50)
humidity = st.slider("humidity", 30, 70)

if st.button("Predict"):

    res = requests.post(
        "http://localhost:5000/predict",
        json={
            "temperature": temperature,
            "vibration": vibration,
            "pressure": pressure,
            "humidity": humidity
        }
    )

    st.write(res.json())