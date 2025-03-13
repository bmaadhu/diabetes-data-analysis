# Diabetes Data Analysis (EDA + Baseline Model)

A clean, reproducible data analysis project using a diabetes healthcare dataset (`Healthcare-Diabetes.csv`).  
Includes exploratory analysis, data cleaning, visualizations, and an optional baseline model.

## Dataset
- File: `data/raw/Healthcare-Diabetes.csv`
- Shape: **2,768 rows × 10 columns**
- Target: **Outcome** (0/1)

⚠️ Some physiological columns contain many **0** values that often represent missing measurements in Pima-style datasets:
`Glucose` (0.7% zeros), `BloodPressure` (4.5% zeros), `SkinThickness` (28.9% zeros), `Insulin` (48.0% zeros), `BMI` (1.4% zeros)

This project treats those zeros as missing values for analysis and then imputes numeric columns with the median.

## What’s inside
- **Notebook:** `notebooks/01_eda.ipynb`
- **Reusable code:** `src/` (loading, cleaning, visualization, modeling)
- **Figures:** `reports/figures/`
- **Quick report:** `reports/summary.md`

## Key outputs
- Outcome distribution: `reports/figures/outcome_distribution.png`
- Correlation heatmap: `reports/figures/correlation_heatmap.png`
- Feature histograms (e.g., glucose/BMI): `reports/figures/*_hist.png`

## Project structure
```
diabetes-data-analysis/
├─ data/
│  ├─ raw/Healthcare-Diabetes.csv
│  └─ processed/diabetes_clean_imputed.csv
├─ notebooks/01_eda.ipynb
├─ src/
├─ reports/figures/
├─ requirements.txt
└─ README.md
```

## How to run (local)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate

pip install -r requirements.txt
jupyter notebook
```

Open `notebooks/01_eda.ipynb` and run all cells.

## Notes
- If you plan to make the repo public, confirm you’re allowed to share the dataset.
- You can extend this into a full ML project (cross-validation, feature engineering, model comparison) if you want.
