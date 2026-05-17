from typing import TypedDict

class MaintenanceState(TypedDict, total=False):
    engine_id: int
    prediction_payload: dict
    explanation_data: dict
    history_data: list
    history_summary: dict
    diagnostic_summary: dict
    maintenance_report: str