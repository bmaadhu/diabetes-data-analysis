# Diabetes Dataset Quick Summary

- Rows: **2,768**
- Columns: **10**
- Target column: **Outcome** (0/1)

## Class balance

- Outcome counts: {0: 1816, 1: 952}
- Positive class rate (Outcome=1): **0.344**

## Potential missing-value signals (zeros)

- `Glucose`: zeros in **0.7%** of rows (often indicates missing in Pima-style datasets)
- `BloodPressure`: zeros in **4.5%** of rows (often indicates missing in Pima-style datasets)
- `SkinThickness`: zeros in **28.9%** of rows (often indicates missing in Pima-style datasets)
- `Insulin`: zeros in **48.0%** of rows (often indicates missing in Pima-style datasets)
- `BMI`: zeros in **1.4%** of rows (often indicates missing in Pima-style datasets)

## Generated figures

- `reports/figures/outcome_distribution.png`
- `reports/figures/correlation_heatmap.png`
- Histograms for key features (if present)

