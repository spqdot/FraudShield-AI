# FraudShield AI
### Multi-Agent Financial Fraud Detection and Investigation System

FraudShield AI is an AI-powered financial fraud detection system that combines machine learning and multi-agent orchestration to identify potentially fraudulent transactions and assess transaction risk.

The project uses XGBoost for fraud prediction and LangGraph to coordinate specialized agents. A FastAPI backend exposes the system through REST API endpoints.

## Project Objectives

- Detect potentially fraudulent financial transactions.
- Estimate fraud probability using machine learning.
- Assess transaction risk using additional business rules.
- Coordinate multiple specialized agents using LangGraph.
- Provide an API for transaction analysis.
- Build a foundation for explainable AI-based fraud investigation.

## Architecture

The current implementation contains two agents coordinated through a LangGraph workflow.

**1. Fraud Detection Agent**
- Uses a trained machine learning model.
- Currently uses XGBoost as the default model.
- Calculates fraud probability.
- Compares the probability against a decision threshold.
- Returns a fraud prediction and risk classification.

**2. Risk Assessment Agent**
- Receives the fraud detection result.
- Considers the transaction amount.
- Calculates an illustrative risk score.
- Assigns a Low, Medium, or High risk level.

**LangGraph Workflow**

Transaction Input → Fraud Detection Agent → Risk Assessment Agent → Investigation Result

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Machine Learning | Scikit-learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Agent Orchestration | LangGraph |
| AI Frameworks | LangChain |
| API Development | FastAPI |
| API Documentation | Swagger UI |
| Model Persistence | Joblib |
| Containerization | Docker |
| Cloud Deployment | AWS (planned) |

## Machine Learning Models

Three models were developed and evaluated:

- Logistic Regression
- Random Forest
- XGBoost

XGBoost is currently selected as the default model for the fraud detection workflow.

### Evaluation Results

The following results were obtained on the held-out test split, using thresholds selected on validation data.

| Metric | Logistic Regression | Random Forest | XGBoost |
|---|---:|---:|---:|
| Precision | 14.94% | 11.63% | 18.45% |
| Recall | 89.80% | 91.84% | 89.80% |
| F1-score | 0.26 | 0.21 | 0.31 |
| PR-AUC | 0.719 | 0.863 | 0.855 |

XGBoost currently provides the best precision and F1-score at its selected operating threshold. Random Forest achieves the highest PR-AUC.

The dataset is highly imbalanced, so precision-recall metrics are particularly relevant.

## Dataset

The project uses the Credit Card Fraud Detection dataset from Kaggle.

Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Dataset characteristics:
- 284,807 transactions
- 30 input features
- 492 fraudulent transactions
- Highly imbalanced target classes

The data is split into training and test sets using stratified sampling.

Raw and processed datasets are excluded from this repository.

## API Endpoints

The FastAPI application currently provides:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API home |
| GET | `/health` | Health check |
| POST | `/api/v1/analyze` | Analyze a transaction |

### Run the API locally

Clone the repository:

```bash
git clone https://github.com/spqdot/FraudShield-AI.git
cd FraudShield-AI
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

Ensure the trained model files are available in the local `models/` directory and the processed dataset is available in `data/processed/` if you intend to run the training and testing scripts.

Start the API:

```bash
uvicorn fraudshield.api.main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Example API Result

A successful transaction analysis returns information similar to:

```json
{
  "fraud_detection": {
    "model": "xgboost",
    "fraud_probability": 0.0002,
    "prediction": 0,
    "risk_level": "Low",
    "status": "completed"
  },
  "risk_assessment": {
    "risk_score": 0.02,
    "risk_level": "Low",
    "status": "completed"
  },
  "investigation_status": "risk_assessment_completed"
}
```

This is an illustrative example based on a test transaction.

## Current Development Status

**Implemented**
- Data inspection and preprocessing
- Model training and evaluation
- Logistic Regression, Random Forest and XGBoost
- Fraud Detection Agent
- Risk Assessment Agent
- LangGraph workflow
- FastAPI application
- Transaction analysis endpoint
- Local API testing

**Planned Enhancements**
- RAG-based fraud knowledge retrieval
- Additional investigation and research agents
- Explainable AI and evidence-based investigation reports
- React-based frontend dashboard
- Docker containerization
- AWS deployment
- Monitoring and production evaluation

## Important Note

This project is a development and demonstration system. Its risk scoring rules are illustrative and have not been validated for production financial decisions. Predictions should support human review rather than automatically determine whether a transaction is fraudulent.

## Author

**Shrabani Panigrahi**

GitHub: https://github.com/spqdot

LinkedIn: https://www.linkedin.com/
