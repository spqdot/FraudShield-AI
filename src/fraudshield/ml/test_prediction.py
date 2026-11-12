import pandas as pd
from pathlib import Path
from predict import predict_fraud


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Load one transaction from the test dataset
test_df = pd.read_csv(DATA_DIR / "test.csv")

transaction = test_df.drop(columns=["Class"]).iloc[[0]]

actual_label = int(test_df.iloc[0]["Class"])

# Predict using XGBoost
print("\n--- Fraud Detection Model Comparison ---")
print("Actual label:", actual_label)

for model_name in [
    "logistic_regression",
    "random_forest",
    "xgboost"
]:
    result = predict_fraud(transaction, model_name=model_name)
    print(f"\n{model_name}:")
    print(result)