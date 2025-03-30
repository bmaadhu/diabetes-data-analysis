import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def save_current_fig(path: str | Path, dpi: int = 180) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=dpi)
    plt.close()

def plot_outcome_distribution(df: pd.DataFrame, outcome_col: str = "Outcome") -> None:
    ax = df[outcome_col].value_counts().sort_index().plot(kind="bar")
    ax.set_title("Outcome distribution")
    ax.set_xlabel(outcome_col)
    ax.set_ylabel("Count")

def plot_hist(df: pd.DataFrame, col: str, bins: int = 30, title: str | None = None) -> None:
    ax = df[col].dropna().plot(kind="hist", bins=bins)
    ax.set_title(title or f"{col} distribution")
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")

def plot_corr_heatmap(df: pd.DataFrame, title: str = "Correlation heatmap") -> None:
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(9, 7))
    plt.imshow(corr, aspect="auto")
    plt.title(title)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
    plt.yticks(range(len(corr.index)), corr.index)
    plt.colorbar()
