
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import logging

from fraudshield.agents.fraud_workflow import build_fraud_workflow

logger = logging.getLogger(__name__)

app = FastAPI(
    title="FraudShield AI",
    description="Multi-Agent Financial Fraud Detection and Investigation API",
    version="1.0.0"
)

fraud_workflow = build_fraud_workflow()


class TransactionRequest(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float = Field(ge=0)


@app.get("/")
def home():
    return {
        "message": "Welcome to FraudShield AI",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/api/v1/analyze")
def analyze_transaction(request: TransactionRequest):
    """
    Analyze a transaction for fraud using the LangGraph workflow.
    
    Returns fraud detection and risk assessment results.
    Handles errors gracefully with proper logging.
    """
    try:
        transaction = pd.DataFrame([request.model_dump()])

        initial_state = {
            "transaction": transaction,
            "actual_label": None,
            "fraud_result": None,
            "risk_result": None,
            "investigation_status": "started",
            "error": None
        }

        result = fraud_workflow.invoke(initial_state)

        if result.get("error"):
            logger.error(f"Workflow error: {result['error']}")
            raise HTTPException(
                status_code=500,
                detail=f"Fraud analysis failed: {result['error']}"
            )

        return {
            "fraud_detection": result["fraud_result"],
            "risk_assessment": result["risk_result"],
            "investigation_status": result["investigation_status"]
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in analyze_transaction: {type(e).__name__}: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Internal server error during transaction analysis"
        )
