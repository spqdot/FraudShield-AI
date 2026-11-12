import pandas as pd
from pathlib import Path

from fraud_detection_agent import run_fraud_detection


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Load a transaction from the test dataset
test_df = pd.read_csv(DATA_DIR / "test.csv")

transaction = test_df.drop(columns=["Class"]).iloc[[0]]

actual_label = int(test_df.iloc[0]["Class"])

# Run the Fraud Detection Agent
result = run_fraud_detection(transaction)

print("\n--- Fraud Detection Agent Result ---")
print("Actual label:", actual_label)
print("Agent result:", result)