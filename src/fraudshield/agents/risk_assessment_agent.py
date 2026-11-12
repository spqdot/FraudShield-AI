from typing import Any
import pandas as pd

def assess_transaction_risk(
    transaction: pd.DataFrame,
    fraud_result: dict[str, Any]
) -> dict[str, Any]:
    """
    Assess transaction risk using ML probability
    and transparent business rules.
    """

    fraud_probability = fraud_result["fraud_probability"]

    amount = float(transaction["Amount"].iloc[0])

    # Calculate a transparent risk score
    risk_score = fraud_probability * 100

    if amount > 1000:
        risk_score += 15
    elif amount > 500:
        risk_score += 10
    elif amount > 100:
        risk_score += 5

    risk_score = min(risk_score, 100)

    # Determine overall risk category
    if risk_score >= 70:
        risk_level = "High"
    elif risk_score >= 30:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "agent": "risk_assessment_agent",
        "fraud_probability": fraud_probability,
        "transaction_amount": amount,
        "risk_score": round(risk_score, 2),
        "risk_level": risk_level,
        "status": "completed"
    }

