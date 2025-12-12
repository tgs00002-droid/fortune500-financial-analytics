"""
Fortune 500 Financial Analytics Platform
Step 1: Load and clean Fortune 500 company data
"""

import pandas as pd


def load_fortune500_data(path: str) -> pd.DataFrame:
    """
    Load Fortune company data and filter to Top 500
    """
    df = pd.read_csv(path)

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Filter Top 500 if ranking column exists
    if "rank" in df.columns:
        df = df[df["rank"] <= 500].copy()

    return df


def main():
    input_path = "data/fortune_raw.csv"
    output_path = "data/fortune500_clean.csv"

    df = load_fortune500_data(input_path)

    print("Rows:", df.shape[0])
    print("Columns:", list(df.columns))
    print(df.head())

    # Save cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Clean Fortune 500 data saved to {output_path}")


if __name__ == "__main__":
    main()
