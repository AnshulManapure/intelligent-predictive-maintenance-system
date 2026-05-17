from typing import TypedDict

class MaintenanceState(TypedDict, total=False):
    engine_id: int
    prediction_payload: dict
    explanation_data: dict
    history_data: list
    maintenance_report: str