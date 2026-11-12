from typing import Any
import pandas as pd

from fraudshield.ml.predict import predict_fraud

def run_fraud_detection(
    transaction: pd.DataFrame,
    model_name: str = "xgboost"
) -> dict[str, Any]:
    """
    Run fraud detection on a financial transaction.
    """

    result = predict_fraud(
        transaction,
        model_name=model_name
    )

    return {
        "agent": "fraud_detection_agent",
        "model": result["model"],
        "fraud_probability": result["fraud_probability"],
        "threshold": result["threshold"],
        "prediction": result["prediction"],
        "risk_level": result["risk_level"],
        "status": "completed"
    }

