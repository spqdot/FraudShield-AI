import pandas as pd
from pathlib import Path

from fraudshield.agents.risk_assessment_agent import (
    assess_transaction_risk
)
from fraudshield.ml.predict import predict_fraud


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Load a sample transaction
test_df = pd.read_csv(DATA_DIR / "test.csv")

transaction = test_df.drop(columns=["Class"]).iloc[[0]]

# Get the ML fraud prediction
fraud_result = predict_fraud(
    transaction,
    model_name="xgboost"
)

# Assess transaction risk
risk_result = assess_transaction_risk(
    transaction,
    fraud_result
)

print("\n--- Risk Assessment Agent Result ---")
print("Fraud Detection Result:", fraud_result)
print("Risk Assessment Result:", risk_result)