# ===========================
# Flight Delay Prediction Challenge model deployment
# Author: Oluwaseyi Gbadamosi
# Last Modified: 9 June 2022
# ===========================
# Command to execute script locally: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# Command to run Docker image: docker run -d -p 8000:8000 <fastapi-app-name>:latest


import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import uvicorn

# Create FastAPI instance
app = FastAPI()

# Load trained Pipeline
model = load_model('./model/model_2x')

@app.get("/")
async def main():
    content = """
    <body>
    <h2> Welcome to the End to End Flight Delay Prediction Challenge</h2>
    <p> The pycaret model and FastAPI instances have been set up successfully </p>
    <p> You can view the FastAPI UI by heading to localhost:8000 </p>
    <p> Proceed to initialize the Streamlit UI (frontend/app.py) to submit prediction requests </p>
    </body>
    """
    return HTMLResponse(content=content)


# Create POST endpoint with path '/predict'
@app.post('/predict')
def predict(year, month, day, flight_id, departure_point_new, arrival_point_new, departure_hour, departure_minute, arrival_hour, arrival_minute, flight_status, aircraft_code):
    data = pd.DataFrame([[year, month, day, flight_id, departure_point_new, arrival_point_new, departure_hour, departure_minute, arrival_hour, arrival_minute, flight_status, aircraft_code]])
    data.columns = ['year', 'month', 'day', 'flight_id', 'departure_point_new', 'arrival_point_new', 'departure_hour', 'departure_minute', 'arrival_hour', 'arrival_minute', 'flight_status', 'aircraft_code']
    predictions = predict_model(model, data=data) 
    return {'prediction': list(predictions['Label'])}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
