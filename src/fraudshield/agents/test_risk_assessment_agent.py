import pandas as pd
from pathlib import Path
import pytest

from fraudshield.agents.risk_assessment_agent import assess_transaction_risk
from fraudshield.ml.predict import predict_fraud


@pytest.fixture
def test_data():
    """Load test transaction from the test dataset."""
    project_root = Path(__file__).resolve().parents[3]
    data_dir = project_root / "data" / "processed"
    test_df = pd.read_csv(data_dir / "test.csv")
    transaction = test_df.drop(columns=["Class"]).iloc[[0]]
    return transaction


@pytest.fixture
def fraud_result(test_data):
    """Get ML fraud prediction for test transaction."""
    return predict_fraud(test_data, model_name="xgboost")


def test_risk_assessment_success(test_data, fraud_result):
    """Test risk assessment agent with valid inputs (success case)."""
    risk_result = assess_transaction_risk(test_data, fraud_result)

    # Verify result is a dictionary
    assert isinstance(risk_result, dict)
    
    # Verify all required fields are present
    required_fields = ["fraud_probability", "transaction_amount", "risk_score", "risk_level", "status"]
    for field in required_fields:
        assert field in risk_result, f"Missing field: {field}"
    
    # Verify field types and values
    assert isinstance(risk_result["fraud_probability"], float)
    assert isinstance(risk_result["transaction_amount"], float)
    assert isinstance(risk_result["risk_score"], float)
    assert risk_result["risk_level"] in ["Low", "Medium", "High"]
    assert risk_result["status"] == "completed"
    
    # Verify risk score is in valid range
    assert 0 <= risk_result["risk_score"] <= 100


def test_risk_assessment_none_fraud_result(test_data):
    """Test risk assessment agent with None fraud_result (failure case)."""
    with pytest.raises(ValueError, match="fraud_result cannot be None"):
        assess_transaction_risk(test_data, None)


def test_risk_assessment_missing_fraud_probability(test_data):
    """Test risk assessment agent with missing fraud_probability field (failure case)."""
    invalid_fraud_result = {"agent": "test"}
    
    with pytest.raises(ValueError, match="fraud_result missing fraud_probability field"):
        assess_transaction_risk(test_data, invalid_fraud_result)
