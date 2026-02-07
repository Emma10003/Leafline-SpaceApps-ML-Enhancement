from pathlib import Path
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

DATA_PATH = Path(__file__).parent / "data.csv"
OUT_PATH = Path(__file__).parents[1] / "app" / "ml" / "artifacts" / "bloom_honey_model.joblib"

def main():
    df = pd.read_csv(DATA_PATH)

    # 입력 피처
    X = df[["month", "species"]]
    # 타겟 (꿀 수확량)
    y = df["honey_amount"]

    pre = ColumnTransformer(
        transformers= [
            ("species", OneHotEncoder(handle_unknown="ignore"), ["species"]),
        ],
        remainder="passthrough",  # month는 그대로 통과
    )

    model = RandomForestRegressor(
        n_estimators=300,
        random_state=42,
    )

    pipe = Pipeline([
        ("preprocess", pre),
        ("model", model),
    ])

    pipe.fit(X, y)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, OUT_PATH)
    print(f"Saved model to: {OUT_PATH}")

if __name__ == "__main__":
    main()