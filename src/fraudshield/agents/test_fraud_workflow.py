import pandas as pd
from pathlib import Path
import pytest

from fraudshield.agents.fraud_workflow import build_fraud_workflow


@pytest.fixture
def test_data():
    """Load test transactions from the test dataset."""
    project_root = Path(__file__).resolve().parents[3]
    data_dir = project_root / "data" / "processed"
    test_df = pd.read_csv(data_dir / "test.csv")
    transaction = test_df.drop(columns=["Class"]).iloc[[0]]
    actual_label = int(test_df.iloc[0]["Class"])
    return transaction, actual_label


@pytest.fixture
def fraud_workflow():
    """Build the fraud workflow."""
    return build_fraud_workflow()


def test_fraud_workflow_success(fraud_workflow, test_data):
    """Test FraudShield LangGraph workflow with valid transaction (success case)."""
    transaction, actual_label = test_data
    
    initial_state = {
        "transaction": transaction,
        "actual_label": actual_label,
        "fraud_result": None,
        "risk_result": None,
        "investigation_status": "started",
        "error": None
    }

    result = fraud_workflow.invoke(initial_state)

    # Verify workflow completed successfully
    assert result["investigation_status"] == "risk_assessment_completed"
    assert result["error"] is None
    
    # Verify fraud detection was performed
    assert result["fraud_result"] is not None
    assert isinstance(result["fraud_result"], dict)
    
    # Verify risk assessment was performed
    assert result["risk_result"] is not None
    assert isinstance(result["risk_result"], dict)


def test_fraud_workflow_empty_transaction(fraud_workflow):
    """Test FraudShield LangGraph workflow with empty transaction (failure case)."""
    invalid_transaction = pd.DataFrame([])

    initial_state = {
        "transaction": invalid_transaction,
        "actual_label": None,
        "fraud_result": None,
        "risk_result": None,
        "investigation_status": "started",
        "error": None
    }

    result = fraud_workflow.invoke(initial_state)

    # Verify workflow handled the error
    assert result["investigation_status"] == "failed"
    assert result["error"] is not None
    
    # Verify fraud detection failed
    assert result["fraud_result"] is None
    
    # Verify risk assessment was skipped (conditional routing)
    assert result["risk_result"] is None
