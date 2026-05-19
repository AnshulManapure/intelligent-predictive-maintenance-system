# Synthetic Turbofan Maintenance Knowledge Base

This document is a synthetic maintenance knowledge base created for an AI predictive maintenance portfolio project. It is not an official aircraft maintenance manual.

---

## Sensor 2 — Fan Inlet Temperature

Sensor 2 is treated as a temperature-related indicator in the predictive maintenance system.

Potential concern:
- Sustained abnormal temperature trends may indicate inlet airflow variation, sensor drift, or operating condition changes.

Recommended checks:
- Verify sensor calibration.
- Inspect inlet airflow path for obstruction.
- Compare readings against recent operating settings.
- Monitor whether the trend persists across multiple cycles.

---

## Sensor 3 — Compressor Outlet Temperature

Sensor 3 is treated as a compressor temperature indicator.

Potential concern:
- Rising compressor outlet temperature trends may indicate reduced compressor efficiency or abnormal thermal loading.

Recommended checks:
- Inspect compressor performance trends.
- Compare temperature changes with pressure-related sensor behavior.
- Check for abnormal increases across rolling mean features.
- Escalate if temperature trends increase together with failure probability.

---

## Sensor 4 — Turbine Inlet Temperature

Sensor 4 is treated as a turbine temperature indicator.

Potential concern:
- Elevated turbine inlet temperature trends may indicate thermal stress, combustion inefficiency, or turbine section degradation.

Recommended checks:
- Inspect turbine temperature trend history.
- Compare against compressor and fuel-flow-related indicators.
- Review whether the increase is sustained over multiple cycles.
- Prioritize inspection if SHAP impact increases failure risk.

---

## Sensor 7 — Compressor Pressure Indicator

Sensor 7 is treated as a pressure-related compressor indicator.

Potential concern:
- Abnormal pressure trends may indicate compressor degradation, airflow restriction, or efficiency loss.

Recommended checks:
- Compare pressure trends with compressor temperature sensors.
- Inspect for sustained pressure deviation.
- Monitor rolling mean and lag features for trend persistence.
- Escalate if pressure deviation coincides with increasing failure probability.

---

## Sensor 11 — High-Pressure Compressor Health Indicator

Sensor 11 is treated as a high-pressure compressor health indicator.

Potential concern:
- Changes in this sensor may indicate compressor efficiency degradation or abnormal operating stress.

Recommended checks:
- Review rolling mean trends.
- Compare current readings against recent history.
- Inspect related compressor temperature and pressure indicators.
- If SHAP impact increases failure risk, schedule compressor-focused inspection.

---

## Sensor 12 — Bypass or Cooling Flow Indicator

Sensor 12 is treated as a flow-related health indicator.

Potential concern:
- Abnormal flow trends may indicate cooling inefficiency, bypass variation, or airflow imbalance.

Recommended checks:
- Inspect airflow-related sensor groups.
- Compare with pressure and temperature indicators.
- Monitor for persistent rolling mean deviation.
- Escalate if multiple flow-related sensors contribute positively to failure risk.

---

## Sensor 15 — Engine Pressure Ratio Indicator

Sensor 15 is treated as an engine pressure ratio or efficiency-related indicator.

Potential concern:
- Abnormal trends may indicate reduced engine efficiency or pressure imbalance.

Recommended checks:
- Compare with compressor and turbine sensor trends.
- Review rolling mean behavior across recent cycles.
- Inspect for simultaneous changes in temperature and pressure sensors.
- Prioritize if SHAP contribution increases failure probability.

---

## Sensor 17 — Physical Speed or Core Rotation Indicator

Sensor 17 is treated as a speed or rotational health indicator.

Potential concern:
- Abnormal rotational behavior may indicate load imbalance, control issues, or degradation.

Recommended checks:
- Compare speed-related readings with operating settings.
- Monitor for abrupt changes or persistent deviations.
- Inspect if rotational indicators align with rising failure probability.
- Continue monitoring if contribution reduces failure risk.

---

## Sensor 20 — Cooling or Flow Health Indicator

Sensor 20 is treated as a cooling or flow-related health indicator.

Potential concern:
- Deviation may indicate cooling flow reduction or airflow imbalance.

Recommended checks:
- Compare with sensor 21 and other flow-related features.
- Monitor rolling averages for persistent drift.
- Inspect cooling-related subsystems if failure risk increases.
- Continue routine monitoring if contribution reduces risk.

---

## Sensor 21 — Cooling or Flow Health Indicator

Sensor 21 is treated as a cooling or flow-related health indicator.

Potential concern:
- Abnormal readings may indicate airflow or cooling performance degradation.

Recommended checks:
- Compare with sensor 20 and pressure-related indicators.
- Review rolling mean and lag features.
- Inspect for persistent drift across cycles.
- Escalate if combined with increasing failure probability.