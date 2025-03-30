import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

def train_logistic_regression(df: pd.DataFrame, target_col: str = "Outcome", test_size: float = 0.2, random_state: int = 42):
    """Train a simple baseline Logistic Regression model."""
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Drop non-feature ID-like columns if present
    for c in ["Id", "ID", "PatientId", "patient_id"]:
        if c in X.columns:
            X = X.drop(columns=[c])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y if y.nunique() == 2 else None
    )

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=2000))
    ])
    pipe.fit(X_train, y_train)

    y_pred = pipe.predict(X_test)
    y_proba = pipe.predict_proba(X_test)[:, 1] if hasattr(pipe, "predict_proba") and y.nunique() == 2 else None

    report = classification_report(y_test, y_pred, output_dict=False)
    auc = roc_auc_score(y_test, y_proba) if y_proba is not None else None

    return pipe, report, auc
