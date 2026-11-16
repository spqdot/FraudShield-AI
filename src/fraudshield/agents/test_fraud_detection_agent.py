import pandas as pd
from pathlib import Path
import pytest

from fraudshield.agents.fraud_detection_agent import run_fraud_detection


@pytest.fixture
def test_data():
    """Load test transaction from the test dataset."""
    project_root = Path(__file__).resolve().parents[3]
    data_dir = project_root / "data" / "processed"
    test_df = pd.read_csv(data_dir / "test.csv")
    transaction = test_df.drop(columns=["Class"]).iloc[[0]]
    actual_label = int(test_df.iloc[0]["Class"])
    return transaction, actual_label


def test_fraud_detection_success(test_data):
    """Test fraud detection agent with valid transaction (success case)."""
    transaction, actual_label = test_data
    
    result = run_fraud_detection(transaction)
    
    # Verify result is a dictionary
    assert isinstance(result, dict)
    
    # Verify all required fields are present
    required_fields = ["model", "fraud_probability", "threshold", "prediction", "risk_level", "status"]
    for field in required_fields:
        assert field in result, f"Missing field: {field}"
    
    # Verify field types
    assert isinstance(result["model"], str)
    assert isinstance(result["fraud_probability"], float)
    assert isinstance(result["prediction"], int)
    assert result["prediction"] in [0, 1]
    assert result["status"] == "completed"


def test_fraud_detection_empty_transaction():
    """Test fraud detection agent with empty transaction (failure case)."""
    empty_transaction = pd.DataFrame([])
    
    with pytest.raises(ValueError, match="Transaction DataFrame cannot be None or empty"):
        run_fraud_detection(empty_transaction)
