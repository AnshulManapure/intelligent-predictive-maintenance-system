# Intelligent Predictive Maintenance System

An end-to-end ML engineering and agentic AI system for predictive maintenance using the NASA C-MAPSS turbofan engine dataset.

The project combines:

* Time-series feature engineering using PySpark
* Failure prediction using RandomForest/XGBoost
* MLflow experiment tracking and model registry
* FastAPI model serving
* SQLite persistence layer
* SHAP explainability
* LangGraph-powered diagnostic workflows
* RAG-based maintenance reasoning using ChromaDB

---

# System Architecture

```text
NASA C-MAPSS Sensor Data
            ↓
PySpark Feature Engineering
            ↓
Model Training (RF / XGBoost)
            ↓
MLflow Experiment Tracking
            ↓
MLflow Model Registry
            ↓
FastAPI Prediction Service
     ├── /predict
     ├── /explain
     └── /predictions/{engine_id}
            ↓
SQLite Prediction Store
            ↓
LangGraph Diagnostic Agent
     ├── Prediction History Tool
     ├── SHAP Explainability Tool
     ├── Maintenance Manual Retrieval (RAG)
     └── Maintenance Report Generator
            ↓
Structured Maintenance Recommendations
```

---

# Features

## Predictive Maintenance Modeling

* Time-series feature engineering using rolling statistics and lag features
* Remaining Useful Life (RUL) computation
* Failure risk classification
* Logistic Regression, RandomForest, and XGBoost experimentation
* Threshold tuning for recall-sensitive maintenance workflows

## MLflow MLOps Pipeline

* Experiment tracking
* Parameter logging
* Metric comparison
* Artifact logging
* Model registry with Champion alias deployment workflow

## Explainable AI

* SHAP-based local and global explainability
* Top contributing sensor analysis
* Failure reasoning support for maintenance workflows

## FastAPI Inference Service

* Real-time prediction APIs
* Explainability endpoint
* Historical prediction retrieval
* SQLite persistence layer

## LangGraph Agentic Workflow

* Multi-step orchestration using LangGraph
* Tool-based reasoning architecture
* Historical trend analysis
* Explainability-driven maintenance reporting
* Retrieval-Augmented Generation (RAG) using ChromaDB

---

# Tech Stack

## Machine Learning

* Scikit-learn
* XGBoost
* SHAP

## Data Engineering

* PySpark
* Pandas
* NumPy

## MLOps

* MLflow
* Model Registry

## Backend

* FastAPI
* Uvicorn
* REST APIs

## Databases

* SQLite
* ChromaDB

## Agentic AI

* LangChain
* LangGraph
* RAG Pipelines

---

# Dataset

Dataset used:

NASA C-MAPSS Turbofan Engine Degradation Simulation Dataset

The dataset contains:

* Multivariate sensor telemetry
* Engine operational settings
* Progressive degradation patterns
* Remaining useful life labels

Source:
[https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)

---

<!--
# Project Structure

```text
project/
│
├── api/
│   ├── app.py
│   ├── database.py
│   ├── schemas.py
│   └── utils.py
│
├── agent/
│   ├── main.py
│   ├── state.py
│   ├── nodes.py
│   ├── tools.py
│   └── prompts.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── feature_engineering.ipynb
│   ├── model_training.ipynb
│   ├── shap_explainability.ipynb
│   └── rag_pipeline.ipynb
│
├── mlruns/
├── requirements.txt
└── README.md
```
-->
---

# ML Pipeline

## Feature Engineering

Implemented using PySpark:

* Lag features
* Rolling mean statistics
* Rolling standard deviation
* Sensor trend analysis

Example features:

```text
sensor_11_lag1
sensor_11_lag2
sensor_11_mean5
sensor_11_std5
```

---

# Model Training

Models evaluated:

* Logistic Regression
* RandomForestClassifier
* XGBoostClassifier

Metrics tracked:

* Precision
* Recall
* F1-score
* ROC-AUC

Threshold optimization performed to balance:

* false positives
* missed failures

---

# MLflow Workflow

Tracked:

* Model parameters
* Metrics
* Confusion matrices
* Feature importance artifacts
* SHAP artifacts
* Model versions

Production model deployment uses:

```text
Champion Alias
```

for dynamic model loading.

---

# FastAPI Endpoints

## Predict Failure Risk

```http
POST /predict
```

Returns:

* failure probability
* prediction label
* model threshold

---

## Explain Predictions

```http
POST /explain
```

Returns:

* prediction
* SHAP feature contributions
* top contributing sensors

---

## Retrieve Prediction History

```http
GET /predictions/{engine_id}
```

Returns:

* historical predictions
* timestamps
* model versions

---

# LangGraph Diagnostic Workflow

The LangGraph agent orchestrates:

1. Historical prediction retrieval
2. SHAP explainability retrieval
3. Maintenance trend analysis
4. RAG-based maintenance manual lookup
5. Structured maintenance report generation

Workflow:

```text
START
  ↓
Fetch Prediction History
  ↓
Fetch SHAP Explanations
  ↓
Retrieve Maintenance Manual Context
  ↓
Generate Maintenance Report
  ↓
END
```

---

# Explainability

SHAP is used for:

* Global feature importance
* Local prediction explanations
* Sensor contribution analysis

Example output:

```json
{
  "feature": "sensor_11_mean5",
  "impact": -0.039
}
```

---

# Future Improvements

* LSTM-based sequence modeling
* Real-time streaming ingestion
* Dockerized deployment
* Kubernetes orchestration
* Grafana monitoring dashboard
* Online inference pipeline
* Human-in-the-loop maintenance workflows

---
<!--
# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start MLflow

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

---

## Start FastAPI Service

```bash
uvicorn api.app:app --reload
```

Swagger docs:

```text
http://127.0.0.1:8000/docs
```

---

## Run LangGraph Agent

```bash
python agent/main.py
```

---
-->
# Key Learning Outcomes

This project demonstrates:

* Time-series ML engineering
* Feature engineering using PySpark
* MLOps workflows using MLflow
* Explainable AI with SHAP
* Production-style FastAPI serving
* SQLite persistence and auditability
* Agentic AI orchestration using LangGraph
* RAG pipelines using ChromaDB
* End-to-end AI system integration

---

# Lice
