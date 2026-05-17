from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from agent.prompts import DIAGNOSTIC_REPORT_PROMPT

from agent.state import *
from agent.tools import *

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

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

def generate_diagnostic_summary_node(state:MaintenanceState):
    payload = state['prediction_payload']
    engine_id = int(payload['engine_id'])

    explanation = state['explanation_data']
    history_data = state.get('history_data', [])
    history_summary = summarise_history(history_data)
    state['history_summary'] = history_summary

    fail_prob = explanation['failure_probability']
    pred = explanation['prediction']
    top_features = explanation['top_features']

    feature_list = [
        {
            "feature": x['feature'],
            "impact": x['impact'],
            "effect": "increase_failure_risk" if x['impact'] > 0 else "reduce_failure_risk"
        }
        for x in top_features
    ]

    diagnostic_summary = {
        "engine_id": engine_id,
        "prediction": pred,
        "failure_probability": fail_prob,
        "failure_probability_percent": round(fail_prob*100, 6),
        "history_summary": history_summary,
        "top_features": feature_list
    }

    state['diagnostic_summary'] = diagnostic_summary
    return state

def generate_llm_report_node(state:MaintenanceState):
    summary = state['diagnostic_summary']
    history = summary['history_summary']
    top_features = summary['top_features']

    top_features_text = "\n".join(
        [
            f"- {x['feature']} | impact: {x['impact']} | effect: {x['effect']}" for x in top_features
        ]
    )

    latest_prob = history['latest_probability']
    highest_prob = history['highest_probability']

    latest_prob_percent = (round(latest_prob*100, 4) if latest_prob is not None else "N/A")
    highest_prob_percent = (round(highest_prob*100, 4) if highest_prob is not None else "N/A")

    prompt = DIAGNOSTIC_REPORT_PROMPT.format(
        engine_id=summary['engine_id'],
        prediction=summary['prediction'],
        failure_probability_percent=summary['failure_probability_percent'],
        record_count=history['record_count'],
        latest_probability_percent=latest_prob_percent,
        highest_probability_percent=highest_prob_percent,
        risk_trend=history['risk_trend'],
        top_features=top_features_text
    )

    try:
        response = llm.invoke(prompt)
        state['maintenance_report'] = response.content
    except Exception as e:
        state['maintenance_report'] = generate_fallback_report(summary)

    return state
