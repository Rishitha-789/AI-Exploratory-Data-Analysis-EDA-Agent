import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

PLOT_DIR = "static/plots"

def run_eda_agent(df: pd.DataFrame) -> str:
    """
    Lightweight EDA agent: inspects the dataset and generates insights.
    """
    insights = []

    insights.append("COLUMN SUMMARY")
    insights.append(str(df.dtypes))

    insights.append("\nBASIC STATISTICS")
    insights.append(str(df.describe(include='all')))

    # Missing values
    missing = df.isnull().sum()
    insights.append("\nMISSING VALUES")
    insights.append(str(missing[missing > 0]))

    # Correlation matrix (numeric only)
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if not numeric_df.empty:
        corr = numeric_df.corr()
        insights.append("\nCORRELATIONS (numeric features)")
        insights.append(str(corr))
    else:
        insights.append("\nNo numeric columns found for correlation analysis.")

    # Simple trend detection for time columns
    time_cols = [col for col in df.columns if 'date' in col.lower()]
    if time_cols:
        insights.append("\nTIME COLUMN DETECTED")
        insights.append(f"Using time column: {time_cols[0]}")

    return "\n".join(insights)


def generate_plots(df: pd.DataFrame):
    """
    Generates a set of useful EDA visualizations.
    Saves them as PNGs and returns file names.
    """
    os.makedirs(PLOT_DIR, exist_ok=True)
    plot_files = []

    # 1. Correlation heatmap (numeric only)
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if not numeric_df.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
        f = f"heatmap_{timestamp()}.png"
        plt.savefig(os.path.join(PLOT_DIR, f))
        plt.close()
        plot_files.append(f)

    # 2. Distribution plots
    for col in numeric_df.columns[:3]:  # limit to 3 for simplicity
        plt.figure()
        sns.histplot(df[col], kde=True)
        f = f"dist_{col}_{timestamp()}.png"
        plt.savefig(os.path.join(PLOT_DIR, f))
        plt.close()
        plot_files.append(f)

    return plot_files


def timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S%f")
