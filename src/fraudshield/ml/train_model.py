
import pandas as pd
from pathlib import Path
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    average_precision_score,
    classification_report,
    confusion_matrix
)

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Load training and test datasets
train_df = pd.read_csv(DATA_DIR / "train.csv")
test_df = pd.read_csv(DATA_DIR / "test.csv")

X = train_df.drop(columns=["Class"])
y = train_df["Class"]

X_test = test_df.drop(columns=["Class"])
y_test = test_df["Class"]

# Create training and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Validation samples:", len(X_val))

# Build Logistic Regression pipeline
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(
        class_weight="balanced",
        max_iter=1000,
        random_state=42
    ))
])

# Train model
print("\nTraining Logistic Regression...")
model.fit(X_train, y_train)

# Get validation fraud probabilities
val_prob = model.predict_proba(X_val)[:, 1]

# Evaluate different thresholds

import numpy as np

# Evaluate finer threshold intervals
thresholds = np.arange(0.01, 0.901, 0.01)

results = []

for threshold in thresholds:
    val_pred = (val_prob >= threshold).astype(int)

    precision = precision_score(y_val, val_pred, zero_division=0)
    recall = recall_score(y_val, val_pred, zero_division=0)
    f1 = f1_score(y_val, val_pred, zero_division=0)

    results.append({
        "threshold": threshold,
        "precision": precision,
        "recall": recall,
        "f1": f1
    })

results_df = pd.DataFrame(results)

print("\n--- Detailed Threshold Comparison ---")
print(results_df.to_string(index=False))

# Select the threshold with maximum precision
# subject to minimum recall of 85%
eligible = results_df[results_df["recall"] >= 0.85]

if not eligible.empty:
    best_row = eligible.loc[eligible["precision"].idxmax()]

    print("\n--- Selected Threshold ---")
    print(best_row)
else:
    print("\nNo threshold achieved the minimum recall target.")



# Retrain using the complete training dataset
print("\nRetraining on complete training dataset...")

final_model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(
        class_weight="balanced",
        max_iter=1000,
        random_state=42
    ))
])

final_model.fit(X, y)

# Evaluate once on untouched test data
test_prob = final_model.predict_proba(X_test)[:, 1]

selected_threshold = 0.77
test_pred = (test_prob >= selected_threshold).astype(int)

print(f"\n--- Final Test Results (Threshold={selected_threshold}) ---")

print(classification_report(
    y_test,
    test_pred,
    zero_division=0
))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, test_pred))

print("\nTest PR-AUC:")
print(average_precision_score(y_test, test_prob))


# ==========================================
# RANDOM FOREST MODEL
# ==========================================

print("\n\nTraining Random Forest...")

rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

# Train using the training split
rf_model.fit(X_train, y_train)

# Get validation fraud probabilities
rf_val_prob = rf_model.predict_proba(X_val)[:, 1]

# Evaluate thresholds
rf_results = []

for threshold in thresholds:
    rf_val_pred = (rf_val_prob >= threshold).astype(int)

    precision = precision_score(y_val, rf_val_pred, zero_division=0)
    recall = recall_score(y_val, rf_val_pred, zero_division=0)
    f1 = f1_score(y_val, rf_val_pred, zero_division=0)

    rf_results.append({
        "threshold": threshold,
        "precision": precision,
        "recall": recall,
        "f1": f1
    })

rf_results_df = pd.DataFrame(rf_results)

print("\n--- Random Forest Threshold Comparison ---")
print(rf_results_df.to_string(index=False))

# Select threshold with maximum precision
# subject to minimum recall of 85%
rf_eligible = rf_results_df[rf_results_df["recall"] >= 0.85]

if not rf_eligible.empty:
    rf_best_row = rf_eligible.loc[rf_eligible["precision"].idxmax()]
    rf_selected_threshold = rf_best_row["threshold"]

    print("\n--- Random Forest Selected Threshold ---")
    print(rf_best_row)

    # Retrain using complete training dataset
    print("\nRetraining Random Forest on complete training dataset...")
    rf_final_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    )

    rf_final_model.fit(X, y)

    # Evaluate once on untouched test data
    rf_test_prob = rf_final_model.predict_proba(X_test)[:, 1]
    rf_test_pred = (
        rf_test_prob >= rf_selected_threshold
    ).astype(int)

    print(
        f"\n--- Random Forest Final Test Results "
        f"(Threshold={rf_selected_threshold:.2f}) ---"
    )

    print(classification_report(
        y_test,
        rf_test_pred,
        zero_division=0
    ))

    print("\nRandom Forest Confusion Matrix:")
    print(confusion_matrix(y_test, rf_test_pred))

    print("\nRandom Forest Test PR-AUC:")
    print(average_precision_score(y_test, rf_test_prob))

else:
    print("\nNo Random Forest threshold achieved minimum recall of 85%.")



    # -----------------------------------
# XGBoost Model
# -----------------------------------

# Calculate class imbalance ratio using training data only
scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

xgb_model = XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=scale_pos_weight,
    objective="binary:logistic",
    eval_metric="aucpr",
    random_state=42,
    n_jobs=-1
)

# Train on the inner training split
xgb_model.fit(X_train, y_train)

# Predict fraud probabilities on validation data
xgb_val_proba = xgb_model.predict_proba(X_val)[:, 1]

# Evaluate different classification thresholds
xgb_results = []

for threshold in thresholds:
    xgb_val_pred = (xgb_val_proba >= threshold).astype(int)

    precision = precision_score(
        y_val, xgb_val_pred, zero_division=0
    )
    recall = recall_score(
        y_val, xgb_val_pred, zero_division=0
    )
    f1 = f1_score(
        y_val, xgb_val_pred, zero_division=0
    )

    xgb_results.append({
        "threshold": threshold,
        "precision": precision,
        "recall": recall,
        "f1": f1
    })

xgb_results_df = pd.DataFrame(xgb_results)

# Select the threshold that maximises precision
# while maintaining at least 85% recall
xgb_eligible = xgb_results_df[
    xgb_results_df["recall"] >= 0.85
]

if xgb_eligible.empty:
    print("XGBoost: No threshold achieved the minimum recall of 85%.")
else:
    xgb_best_row = xgb_eligible.loc[
        xgb_eligible["precision"].idxmax()
    ]

    xgb_selected_threshold = xgb_best_row["threshold"]

    print("\nXGBoost Validation Results")
    print(f"Selected threshold: {xgb_selected_threshold:.2f}")
    print(f"Precision: {xgb_best_row['precision']:.4f}")
    print(f"Recall: {xgb_best_row['recall']:.4f}")
    print(f"F1-score: {xgb_best_row['f1']:.4f}")

    # Retrain using the complete training dataset
    xgb_final_model = XGBClassifier(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=(
            (y_train == 0).sum() / (y_train == 1).sum()
        ),
        objective="binary:logistic",
        eval_metric="aucpr",
        random_state=42,
        n_jobs=-1
    )

    xgb_final_model.fit(X, y)

    # Evaluate on the held-out test set
    xgb_test_proba = xgb_final_model.predict_proba(X_test)[:, 1]
    xgb_test_pred = (
        xgb_test_proba >= xgb_selected_threshold
    ).astype(int)

    print("\nXGBoost Test Results")
    print(classification_report(y_test, xgb_test_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, xgb_test_pred))
    print(
        "PR-AUC:",
        average_precision_score(y_test, xgb_test_proba)
    )


    # -----------------------------------
# Save Trained Models
# -----------------------------------

MODEL_DIR = PROJECT_ROOT / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

# Save Logistic Regression
joblib.dump(final_model, MODEL_DIR / "logistic_regression.pkl")

# Save Random Forest
joblib.dump(rf_final_model, MODEL_DIR / "random_forest.pkl")

# Save XGBoost
joblib.dump(xgb_final_model, MODEL_DIR / "xgboost.pkl")

# Save selected thresholds
threshold_config = {
    "logistic_regression": 0.77,
    "random_forest": 0.02,
    "xgboost": float(xgb_selected_threshold)
}

joblib.dump(
    threshold_config,
    MODEL_DIR / "thresholds.pkl"
)

print("\nAll models and thresholds saved successfully!")