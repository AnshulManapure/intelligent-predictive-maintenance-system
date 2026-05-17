from agent.state import *
from agent.tools import *

def fetch_history_node(state:MaintenanceState):
    engine_id = int(state['engine_id'])
    result = get_prediction_history(engine_id)
    state['history_data'] = result
    return state

def fetch_explanation_node(state:MaintenanceState):
    payload = state['prediction_payload']
    result = get_explanation(payload)
    state['explanation_data'] = result
    return state

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

def generate_report_node(state:MaintenanceState):
    payload = state['prediction_payload']
    engine_id = int(payload['engine_id'])

    explanation = state['explanation_data']
    history_data = state.get('history_data', [])
    history_summary = summarise_history(history_data)

    fail_prob = explanation['failure_probability']
    pred = explanation['prediction']
    top_features = explanation['top_features']

    feature_list = "\n".join(
        [f"- {x['feature']} ({x['impact']})" for x in top_features]
    )

    if history_summary["latest_probability"] is None:
        history_text = "No usable prediction history found for this engine."
    else:
        latest_percent = round(history_summary["latest_probability"] * 100, 4)
        highest_percent = round(history_summary["highest_probability"] * 100, 4)

        history_text = f"""Recent prediction history:
    - Records found: {history_summary["record_count"]}
    - Latest stored probability: {latest_percent}%
    - Highest stored probability: {highest_percent}%
    - Risk trend: {history_summary["risk_trend"]}"""

    out = f"""\nEngine with ID {engine_id} currently has a {round(fail_prob*100, 6)}% probability of failure.
It is currently a {pred} engine.

{history_text}

The top contributing features are:
{feature_list}
"""
    
    state['maintenance_report'] = out
    return state