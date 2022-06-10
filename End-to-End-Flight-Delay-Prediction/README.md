# End-to-End Flight Delay Prediction Challenge model deployment with pycaret, streamlit and fastapi

command to run docker compose:
- Run this Docker compose file using: docker-compose up -d --build

command to run backend:
- Command to execute script locally: streamlit run app.py
- Command to run Docker image: docker run -d -p 8501:8501  fastapi-backend:latest

Command to run frontend
- Command to execute script locally: uvicorn main:app  --reload
- Command to run Docker image: docker run -d -p 8000:8000 Streamlit-frontend:latest

## Overview 
- Flight delays not only irritates air passengers and disrupt their schedules but also causes :

- decreased efficiency
- increased capital costs, reallocation of flight crews and aircraft
- additional crew expenses
- Most passengers choose air travel due to its relative safety and timeliness. This means that delays would most likely have a negative impact on passenger demand for air travel.

- This solution proposes to build a flight delay predictive model using Machine Learning techniques. The accurate prediction of flight delays will help all players in the air travel ecosystem to set up effective action plans to reduce the impact of the delays and avoid loss of time, capital and resources.
___
## Objective
-This project aims to predict the estimated duration of flight delays per flight using dataset gotten from the zindi flight delay prediction challenge..

___
## Pipeline Components
- Data Acquisition and Preprocessing
- Pycaret model training
- Deployment of model via FastAPI
- Streamlit user interface to post test data to FastAPI endpoint

___
## UI Demo
![alt text]()

___
## Project Files and Folders
- `/backend` - Folder to contain the files needed to setup the backend aspects of project ()
    - `main.py` - Python script for deploying (and serving) it as FastAPI endpoint. Run with this command: `uvicorn main:app --host 0.0.0.0 --port 8000`
    - `Dockerfile` - Dockerfile to build backend service  
- `/frontend` - Folder containining the frontend user interface (UI) aspect of project (i.e. Streamlit)
    - `app.py` - Python script for the Streamlit web app, connected with FastAPI endpoint for model inference. Run in CLI with `streamlit run app.py`
    - `Dockerfile` - Dockerfile to build frontend service     
- `/notebooks` - Folder containing Jupyter notebooks for pycaret experiments
  - `Flight_Delay_Prediction_Challenge_model_deployment.ipynb` - Notebook detailing the data acquisition, data cleaning and feature engineering and modelling steps

___
## References
