from fastapi import FastAPI
import mlflow
from mlflow import MlflowClient
import pandas as pd
import shap


from api import schemas
from api import utils
from api import database

#Load Model
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("Predictive_Maintenance_FD001")
model = mlflow.sklearn.load_model("models:/predictive_maintenance_model@champion")

# Load threshold from MLflow
client = MlflowClient()
model_version = client.get_model_version_by_alias(
    "predictive_maintenance_model",
    "champion"
)
run_id = model_version.run_id
run = client.get_run(run_id)
threshold = float(run.data.params["threshold"])

#Initialise SHAP
explainer = shap.TreeExplainer(model=model)

#Creating app
app = FastAPI()

#Initialise Database on startup only
def startup():
    database.init_db()

app.add_event_handler(event_type="startup", func=startup)

@app.post('/predict', response_model=schemas.PredictionResponse)
def predict(readings: schemas.Readings):
    features = pd.DataFrame([readings.features])
    
    # Predict
    y_prob = model.predict_proba(features)[:,1]
    y_pred = (y_prob >= threshold).astype(int) #If probability > threshold, predict as failure.

    values = {
        "engine_id": readings.engine_id,
        "failure_probability": round(float(y_prob[0]), 6),
        "prediction": "HIGH_RISK" if y_pred[0] else "LOW_RISK",
        "threshold": threshold,
        "model_version": f"v{model_version.version}"
    }

    database.save_prediction(values=values)

    return values


@app.get('/predictions')
def get_predictions():
    return database.get_predictions()

@app.get('/predictions/{engine_id}')
def get_predictions_by_engine_id(engine_id: int):
    return database.get_predictions_by_engine_id(engine_id)


@app.post('/explain', response_model=schemas.ExplainResponse)
def explain(readings: schemas.Readings):
    features = pd.DataFrame([readings.features])

    # Predict
    y_prob = model.predict_proba(features)[:,1]
    y_pred = (y_prob >= threshold).astype(int) #If probability > threshold, predict as failure.

    #Generate SHAP values and extract the top 10 features contributing to failure
    shap_values = explainer(features)    
    values = shap_values.values[0, :, 1]
    
    feature_impacts = []
    for feature, impact in zip(features.columns, values):
        feature_impacts.append({
            "feature": feature,
            "impact": impact,
            "effect": "reduces_failure_risk" if impact < 0 else "increases_failure_risk",
            "abs_impact": abs(float(impact))
        })
    feature_impacts = sorted(feature_impacts, key=lambda x:x["abs_impact"], reverse=True)
    top_impacts = feature_impacts[:10]

    res = {
        "failure_probability": round(float(y_prob[0]), 6),
        "prediction": "HIGH_RISK" if y_pred[0] else "LOW_RISK",
        "top_features": [{"feature": top_impacts[i]["feature"], "impact": top_impacts[i]["impact"], "effect":top_impacts[i]["effect"]} for i in range(len(top_impacts))]
    }

    return res

