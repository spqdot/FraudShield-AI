from typing import Any
import pandas as pd

from fraudshield.ml.predict import predict_fraud

def run_fraud_detection(
    transaction: pd.DataFrame,
    model_name: str = "xgboost"
) -> dict[str, Any]:
    """
    Run fraud detection on a financial transaction.
    
    Args:
        transaction: DataFrame with one transaction row.
        model_name: Model to use for prediction.
        
    Returns:
        Dictionary with fraud detection results.
        
    Raises:
        ValueError: If transaction or prediction result is invalid.
    """

    if transaction is None or transaction.empty:
        raise ValueError("Transaction DataFrame cannot be None or empty")

    result = predict_fraud(
        transaction,
        model_name=model_name
    )
    
    if result is None:
        raise ValueError("Prediction result is None")
    
    if "fraud_probability" not in result:
        raise ValueError("Prediction result missing fraud_probability")

    return {
        "agent": "fraud_detection_agent",
        "model": result["model"],
        "fraud_probability": result["fraud_probability"],
        "threshold": result["threshold"],
        "prediction": result["prediction"],
        "risk_level": result["risk_level"],
        "status": "completed"
    }

