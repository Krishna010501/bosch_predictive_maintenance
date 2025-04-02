import streamlit as st
import pandas as pd
import joblib

st.title('CNC Machine Failure Prediction Dashboard')

df = pd.read_csv('data/simulated_sensor_data.csv')
model = joblib.load('src/failure_predictor.pkl')

st.write('### Latest Sensor Data')
st.dataframe(df.tail())

st.write('### Predict New Data')
temp = st.slider('Temperature (°C)', 50, 100, 70)
vibration = st.slider('Vibration RMS', 0.0, 1.5, 0.5)
rpm = st.slider('RPM', 1000, 1600, 1450)

input_df = pd.DataFrame([[temp, vibration, rpm]], columns=['temp_c', 'vibration_rms', 'rpm'])
prediction = model.predict(input_df)[0]
st.write('### Failure Prediction:', '🔴 Failure' if prediction else '🟢 Normal')
