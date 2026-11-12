import pandas as pd
from pathlib import Path

from fraudshield.agents.fraud_workflow import build_fraud_workflow


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Load a sample transaction
test_df = pd.read_csv(DATA_DIR / "test.csv")

transaction = test_df.drop(columns=["Class"]).iloc[[0]]
actual_label = int(test_df.iloc[0]["Class"])

# Build and execute the LangGraph workflow
app = build_fraud_workflow()

initial_state = {
    "transaction": transaction,
    "actual_label": actual_label,
    "fraud_result": None,
    "risk_result": None,
    "investigation_status": "started",
    "error": None
}

result = app.invoke(initial_state)

print("\n--- FraudShield LangGraph Workflow ---")
print("Actual label:", actual_label)
print("Investigation status:", result["investigation_status"])
print("Fraud detection result:", result["fraud_result"])
print("Risk assessment result:", result["risk_result"])
print("Error:", result["error"])