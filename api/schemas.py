from pydantic import BaseModel

class Readings(BaseModel):
    engine_id: int
    features: dict[str, float]

class PredictionResponse(BaseModel):
    engine_id: int
    failure_probability: float
    prediction: str
    threshold: float
    model_version: str

class FeatureImpact(BaseModel):
    feature: str
    impact: float
    effect: str

class ExplainResponse(BaseModel):
    failure_probability: float
    prediction: str
    top_features: list[FeatureImpact]

class DiagnosticResponse(BaseModel):
    maintenance_report: str