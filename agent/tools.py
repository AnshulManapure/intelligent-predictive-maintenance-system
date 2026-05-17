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

def summarise_history(history_data):
    if not history_data:
        return {
            "record_count": 0,
            "latest_probability": None,
            "highest_probability": None,
            "risk_trend": "NO_HISTORY"
        }
    
    probabilities = [float(record['failure_probability']) for record in history_data if record.get("failure_probability") is not None]

    if not probabilities:
        return {
            "record_count": len(history_data),
            "latest_probability": None,
            "highest_probability": None,
            "risk_trend": "NO_PROBABILITY_DATA"
        }
    
    latest_prob = probabilities[0]
    highest_prob = max(probabilities)

    if len(probabilities) < 2:
        risk_trend = "INSUFFICIENT_HISTORY"
    else:
        prev_prob = probabilities[1]
        if latest_prob > prev_prob:
            risk_trend = "INCREASING"
        elif latest_prob < prev_prob:
            risk_trend = "DECREASING"
        else:
            risk_trend = "STABLE"
    
    return {
            "record_count": len(history_data),
            "latest_probability": latest_prob,
            "highest_probability": highest_prob,
            "risk_trend": risk_trend
        }

def generate_fallback_report(summary):
    history = summary["history_summary"]
    top_features = summary["top_features"]

    feature_lines = "\n".join(
        [
            f"- {x['feature']} had a SHAP impact of {x['impact']}, which tends to {x['effect']}."
            for x in top_features
        ]
    )

    if summary["prediction"] == "HIGH_RISK":
        urgency = "High"
        action = "Schedule inspection and maintenance review as soon as possible."
    else:
        urgency = "Low"
        action = "Continue monitoring under normal operating conditions."

    return f"""
1. Current Risk Assessment
Engine {summary['engine_id']} is classified as {summary['prediction']} with a failure probability of {summary['failure_probability_percent']}%.

2. Key Sensor Drivers
{feature_lines}

3. Historical Trend
Records found: {history['record_count']}
Latest stored probability: {history['latest_probability']}
Highest stored probability: {history['highest_probability']}
Risk trend: {history['risk_trend']}

4. Recommended Maintenance Action
{action}

5. Urgency Level
{urgency}
"""