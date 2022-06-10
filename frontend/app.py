# =========================================
# Flight Delay Prediction Challenge model deployment
# Author: Oluwaseyi Gbadamosi
# Last Modified: 9 June 2022
# =========================================
# Command to execute script locally: streamlit run app.py
# Command to run Docker image: docker run -d -p 8501:8501 <streamlit-app-name>:latest

import streamlit as st
import requests
import json

def run():
    # Set FastAPI endpoint 
    endpoint = 'http://localhost:8000/predict'
    # endpoint = 'http://host.docker.internal:8000/predict' # Specify this path for Dockerization to work
    
    st.title("Flight Delay Prediction Challenge model deployment")
    st.write("Features")
    year  = st.number_input('Year')
    month = st.number_input('Month')
    day=st.number_input('Day')
    flight_id = st.selectbox("Flight Id", ['TU' ,'UG', 'AT', 'WKL' ,'AOG' ,'INT' ,'A', 'SGT', '6YE' ,'PRO', '20M', '12Y', 'C','AUI', 'D4', 'DAT' ,'UH', 'GJT', 'X9'])
    departure_point_new=st.selectbox("Departure Point", ['TUN','DJE','ORY','MIR','OTHERS'])
    arrival_point_new=st.selectbox("Arrival Point", ['TUN','DJE','ORY','MIR','OTHERS'])
    departure_hour=st.number_input('Departure Hour')
    departure_minute=st.number_input('Departure Minute')
    arrival_hour=st.number_input('Arrival Hour')
    arrival_minute=st.number_input('Arrival Minute')
    flight_status=st.selectbox("Flight Status", ['ATA', 'DEP' ,'RTR', 'SCH', 'DEL'])
    aircraft_code=st.selectbox("Aircraft Code", ['TU', '5M','UG', '5K', 'BJ', 'GJ', 'QS', 'PS', 'D4', 'UJ', 'GW', '6P', 'OL' ,'X9'])
        
    data = {
        'year':year,
        'month':month,
        'day':day,
        'flight_id':flight_id,
        'departure_point_new':departure_point_new,
        'arrival_point_new':arrival_point_new,
        'departure_hour':departure_hour,
        'departure_minute':departure_minute,
        'arrival_hour':arrival_hour,
        'arrival_minute':arrival_minute,
        'flight_status':flight_status,
        'aircraft_code':aircraft_code
        }
        # Every form must have a submit button.
    if st.button("Predict..."):
        with st.spinner('Prediction in Progress. Please Wait...'):
            prediction = requests.post(
                endpoint, json=data)
            st.success(f"The prediction from model: {prediction}")


if __name__ == '__main__':
    #by default it will run at 8501 port
    run()
