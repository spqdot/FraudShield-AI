from pathlib import Path
import joblib


PROJECT_ROOT = Path(__file__).resolve().parents[3]
MODEL_DIR = PROJECT_ROOT / "models"


def load_models():
    """Load trained fraud detection models and thresholds."""

    models = {
        "logistic_regression": joblib.load(
            MODEL_DIR / "logistic_regression.pkl"
        ),
        "random_forest": joblib.load(
            MODEL_DIR / "random_forest.pkl"
        ),
        "xgboost": joblib.load(
            MODEL_DIR / "xgboost.pkl"
        ),
    }

    thresholds = joblib.load(MODEL_DIR / "thresholds.pkl")

    return models, thresholds


def predict_fraud(transaction, model_name="xgboost"):
    """
    Predict whether a transaction is potentially fraudulent.

    Args:
        transaction: A pandas DataFrame containing one transaction.
        model_name: logistic_regression, random_forest, or xgboost.

    Returns:
        Dictionary containing probability, threshold, and prediction.
    """

    models, thresholds = load_models()

    if model_name not in models:
        raise ValueError(
            f"Unknown model: {model_name}. "
            f"Choose from {list(models.keys())}"
        )

    model = models[model_name]
    threshold = thresholds[model_name]

    probability = float(model.predict_proba(transaction)[0][1])

    prediction = int(probability >= threshold)

    return {
        "model": model_name,
        "fraud_probability": round(probability, 4),
        "threshold": threshold,
        "prediction": prediction,
        "risk_level": "High" if prediction == 1 else "Low",
    }