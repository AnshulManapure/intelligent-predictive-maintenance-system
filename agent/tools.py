import requests
import os
import pandas as pd

def get_prediction_history(engine_id):
    response = requests.get(
        f"http://127.0.0.1:8000/predictions/{engine_id}"
    )
    response.raise_for_status()
    data = response.json()
    return data

def get_explanation(payload):
    response = requests.post(
        url=f"http://127.0.0.1:8000/explain",
        json=payload
    )
    response.raise_for_status()
    return response.json()

def get_payload():
    #Load processed dataset and separate into training and testing
    DATA_DIR = os.path.join(r"D:\Upskill\Mini_Projects\intelligent-predictive-maintenance-system\CMAPSS_Data")
    test_df = pd.read_csv(os.path.join(DATA_DIR, "processed", "test_features.csv"))
    return test_df