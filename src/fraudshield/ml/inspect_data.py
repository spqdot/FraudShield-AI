import pandas as pd
from pathlib import Path

# Locate the dataset from the project root
project_root = Path(__file__).resolve().parents[3]
data_path = project_root / "data" / "raw" / "creditcard.csv"

# Load dataset
df = pd.read_csv(data_path)

# Basic inspection
print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Missing Values ---")
print(df.isnull().sum().sum())

print("\n--- Class Distribution ---")
print(df["Class"].value_counts())

print("\n--- Fraud Percentage ---")
print(df["Class"].value_counts(normalize=True) * 100)

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

print("\n--- Transaction Amount Statistics ---")
print(df["Amount"].describe())

print("\n--- Amount Statistics by Class ---")
print(df.groupby("Class")["Amount"].describe())

print("\n--- Feature Statistics ---")
print(df.describe().T)

print("\n--- Duplicate Records by Class ---")

duplicate_rows = df[df.duplicated(keep=False)]

print(duplicate_rows["Class"].value_counts())

print("\n--- Duplicate Feature Combinations with Conflicting Labels ---")

feature_columns = df.columns.drop("Class")

duplicate_features = df[
    df.duplicated(subset=feature_columns, keep=False)
]

conflicting_labels = (
    duplicate_features
    .groupby(list(feature_columns))["Class"]
    .nunique()
    .gt(1)
    .sum()
)

print("Conflicting duplicate groups:", conflicting_labels)