from pathlib import Path
import joblib
import logging

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path.cwd()
MODEL_DIR = PROJECT_ROOT / "models"

def load_models():
    """
    Load trained fraud detection models and thresholds.
    
    Returns:
        Tuple of (models dict, thresholds dict)
        
    Raises:
        FileNotFoundError: If model files are missing.
        Exception: If model loading fails.
    """
    
    try:
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
    
    except FileNotFoundError as e:
        logger.error(f"Model file not found: {e}")
        raise FileNotFoundError(f"Model file missing: {e}")
    except Exception as e:
        logger.error(f"Failed to load models: {e}")
        raise


def predict_fraud(transaction, model_name="xgboost"):
    """
    Predict whether a transaction is potentially fraudulent.

    Args:
        transaction: A pandas DataFrame containing one transaction.
        model_name: logistic_regression, random_forest, or xgboost.

    Returns:
        Dictionary containing probability, threshold, and prediction.
        
    Raises:
        ValueError: If model_name is invalid or prediction fails.
        Exception: If model loading or prediction fails.
    """
    
    if transaction is None or transaction.empty:
        raise ValueError("Transaction DataFrame cannot be None or empty")

    models, thresholds = load_models()

    if model_name not in models:
        raise ValueError(
            f"Unknown model: {model_name}. "
            f"Choose from {list(models.keys())}"
        )

    model = models[model_name]
    threshold = thresholds[model_name]

    try:
        probability = float(model.predict_proba(transaction)[0][1])
    except Exception as e:
        logger.error(f"Prediction failed for model {model_name}: {e}")
        raise ValueError(f"Prediction failed: {e}")
    
    if probability is None:
        raise ValueError(f"Model returned None probability")

    prediction = int(probability >= threshold)

    return {
        "model": model_name,
        "fraud_probability": round(probability, 4),
        "threshold": threshold,
        "prediction": prediction,
        "risk_level": "High" if prediction == 1 else "Low",
    }
