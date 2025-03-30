import numpy as np
import pandas as pd

ZERO_AS_MISSING_COLS = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

def treat_zeros_as_missing(df: pd.DataFrame, cols: list[str] | None = None) -> pd.DataFrame:
    """Replace 0 with NaN for known physiological columns where 0 is often missing."""
    df = df.copy()
    cols = cols or [c for c in ZERO_AS_MISSING_COLS if c in df.columns]
    for c in cols:
        df.loc[df[c] == 0, c] = np.nan
    return df

def impute_numeric_median(df: pd.DataFrame) -> pd.DataFrame:
    """Simple median imputation for numeric columns."""
    df = df.copy()
    num_cols = df.select_dtypes(include=[np.number]).columns
    for c in num_cols:
        if df[c].isna().any():
            df[c] = df[c].fillna(df[c].median())
    return df
