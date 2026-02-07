from pathlib import Path
import joblib
import pandas as pd

MODEL_PATH = Path(__file__).parent / "artifacts" / "bloom_honey_model.joblib"

_model = None

def get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_honey(month: int, species: str) -> float:
    model = get_model()
    X = pd.DataFrame([{"month": month, "species": species}])
    pred = model.predict(X)[0]
    return float(pred)