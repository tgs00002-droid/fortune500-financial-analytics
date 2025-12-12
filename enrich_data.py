"""
Fortune 500 Financial Analytics Platform
Step 2: Data cleaning and logo enrichment
"""

import pandas as pd

LOGO_BASE_URL = "https://logo.clearbit.com"


def clean_currency(series):
    return (
        series.astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace("-", "", regex=False)
        .astype(float)
    )


def clean_percentage(series):
    return (
        series.astype(str)
        .str.replace("%", "", regex=False)
        .str.replace("-", "", regex=False)
        .astype(float)
    )


def generate_domain(company):
    company = company.lower()
    company = company.replace(" ", "")
    company = company.replace(".", "")
    company = company.replace(",", "")
    company = company.replace("&", "and")
    return f"{company}.com"


def main():
    df = pd.read_csv("fortune_raw.csv")

    # Standardize columns
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Clean numeric columns
    df["revenues"] = clean_currency(df["revenues"])
    df["profits"] = clean_currency(df["profits"])
    df["assets"] = clean_currency(df["assets"])
    df["market_value"] = clean_currency(df["market_value"])
    df["revenue_change"] = clean_percentage(df["revenue_change"])
    df["profit_change"] = clean_percentage(df["profit_change"])

    # Add domains and logos
    df["domain"] = df["company_name"].apply(generate_domain)
    df["logo_url"] = df["domain"].apply(
        lambda d: f"{LOGO_BASE_URL}/{d}"
    )

    # Save enriched dataset
    df.to_csv("fortune500_enriched.csv", index=False)

    print("Saved: fortune500_enriched.csv")
    print(df[["rank", "company_name", "revenues", "profits", "logo_url"]].head())


if __name__ == "__main__":
    main()
