# FraudShield AI
### Multi-Agent Financial Fraud Detection and Investigation System

FraudShield AI is an AI-powered financial fraud detection demo combining machine learning and multi-agent orchestration to identify potentially fraudulent transactions and assess transaction risk.

It uses **XGBoost** for fraud prediction, **LangGraph** to coordinate specialized agents, a **FastAPI** backend, and a **React** dashboard.

## Live Demo

- **Frontend dashboard:** http://fraudshield-ai-frontend-2026.s3-website.eu-north-1.amazonaws.com
- **Backend API:** http://51.20.77.183:8000
- **Swagger API documentation:** http://51.20.77.183:8000/docs
- **Health check:** http://51.20.77.183:8000/health

> **Deployment note:** This demo uses HTTP endpoints. The backend public IP may change if the AWS service is redeployed. It is not intended for production financial decision-making.

## Project Objectives

- Detect potentially fraudulent financial transactions.
- Estimate fraud probability using machine learning.
- Assess transaction risk using additional business rules.
- Coordinate specialized agents using LangGraph.
- Provide a REST API and interactive frontend for transaction analysis.
- Build a foundation for explainable AI-based fraud investigation.

## Architecture

The current implementation contains two agents coordinated through a LangGraph workflow.

### Fraud Detection Agent
- Uses a trained machine learning model, with XGBoost as the default.
- Calculates fraud probability.
- Compares probability against a decision threshold.
- Returns a fraud prediction and risk classification.

### Risk Assessment Agent
- Receives the fraud detection result.
- Considers transaction amount.
- Calculates an illustrative risk score.
- Assigns a Low, Medium, or High risk level.

### LangGraph Workflow

```text
Transaction Input
      |
      v
Fraud Detection Agent
      |
      v
Risk Assessment Agent
      |
      v
Investigation Result
```

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Frontend | React, Vite |
| Machine Learning | Scikit-learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Agent Orchestration | LangGraph |
| AI Frameworks | LangChain |
| API Development | FastAPI |
| API Documentation | Swagger UI |
| Model Persistence | Joblib |
| Containerization | Docker |
| Cloud Deployment | AWS ECS, Amazon ECR, Amazon S3 |

## Machine Learning Models

Three models were developed and evaluated: Logistic Regression, Random Forest, and XGBoost. XGBoost is currently selected as the default model.

### Evaluation Results

The following results were obtained on the held-out test split, using thresholds selected on validation data.

| Metric | Logistic Regression | Random Forest | XGBoost |
|---|---:|---:|---:|
| Precision | 14.94% | 11.63% | 18.45% |
| Recall | 89.80% | 91.84% | 89.80% |
| F1-score | 0.26 | 0.21 | 0.31 |
| PR-AUC | 0.719 | 0.863 | 0.855 |

XGBoost provides the best precision and F1-score at its selected operating threshold. Random Forest achieves the highest PR-AUC. The dataset is highly imbalanced, so precision-recall metrics are particularly relevant.

## Dataset

The project uses the [Credit Card Fraud Detection dataset from Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).

- 284,807 transactions
- 30 input features
- 492 fraudulent transactions
- Highly imbalanced target classes

The data is split into training and test sets using stratified sampling. Raw and processed datasets are excluded from this repository.

## Dashboard Features

- Interactive transaction analysis form.
- Quick demo selection using sample transactions.
- Fraud probability and prediction display.
- Risk assessment results.
- Backend connection status.
- Advanced input fields for PCA components.

The dataset's PCA features (V1â€“V28) are anonymized mathematical components and cannot be interpreted as ordinary transaction details.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API home |
| GET | `/health` | Health check |
| POST | `/api/v1/analyze` | Analyze a transaction |

Explore the deployed API using [Swagger UI](http://51.20.77.183:8000/docs).

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/spqdot/FraudShield-AI.git
cd FraudShield-AI
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

Ensure the trained model files are available in `models/`. The processed dataset in `data/processed/` is required if you intend to run the training and testing scripts.

### 4. Run the backend

```bash
uvicorn fraudshield.api.main:app --reload
```

Open the local API documentation at http://127.0.0.1:8000/docs.

### 5. Run the frontend

In a separate terminal:

```bash
cd frontend
npm install
```

Create or update `frontend/.env.local`:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Start the frontend:

```bash
npm run dev
```

Open http://localhost:5173.

## AWS Deployment

FraudShield AI is deployed using:

- **Amazon ECS (Fargate):** Hosts the FastAPI backend container.
- **Amazon ECR:** Stores the backend Docker image.
- **Amazon S3:** Hosts the static React frontend.
- **CloudWatch Logs:** Used for backend container logs.

| Component | Deployed link |
|---|---|
| Frontend | [FraudShield AI Dashboard](http://fraudshield-ai-frontend-2026.s3-website.eu-north-1.amazonaws.com) |
| Backend | [FastAPI API](http://51.20.77.183:8000) |
| API docs | [Swagger UI](http://51.20.77.183:8000/docs) |
| Health check | [Health endpoint](http://51.20.77.183:8000/health) |

## Example API Result

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

## Development Status

### Implemented
- Data inspection and preprocessing
- Model training and evaluation
- Logistic Regression, Random Forest, and XGBoost
- Fraud Detection Agent
- Risk Assessment Agent
- LangGraph workflow
- FastAPI application and transaction analysis endpoint
- React dashboard and quick demo sample transactions
- Docker containerization
- AWS deployment of backend and frontend

### Potential Enhancements
- RAG-based fraud knowledge retrieval
- Additional investigation and research agents
- Explainable AI and evidence-based investigation reports
- Monitoring and production evaluation

## Important Disclaimer

FraudShield AI is a development and demonstration system. Its risk scoring rules are illustrative and have not been validated for production financial decisions. Predictions should support human review rather than automatically determine whether a transaction is fraudulent.

## Author

**Shrabani Panigrahi**

- GitHub: [spqdot](https://github.com/spqdot)

