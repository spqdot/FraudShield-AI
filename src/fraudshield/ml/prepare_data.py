import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[3]
RAW_DATA = PROJECT_ROOT / "data" / "raw" / "creditcard.csv"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"

# Load original dataset
df = pd.read_csv(RAW_DATA)

# Separate features and target
X = df.drop(columns=["Class"])
y = df["Class"]

# Split data using stratification
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Save training and testing datasets
PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

train_df = X_train.copy()
train_df["Class"] = y_train

test_df = X_test.copy()
test_df["Class"] = y_test

train_df.to_csv(PROCESSED_DATA / "train.csv", index=False)
test_df.to_csv(PROCESSED_DATA / "test.csv", index=False)

# Display results
print("Dataset preparation completed!")

print("\nTraining dataset:", X_train.shape)
print("Testing dataset:", X_test.shape)

print("\nTraining class distribution:")
print(y_train.value_counts())

print("\nTesting class distribution:")
print(y_test.value_counts())