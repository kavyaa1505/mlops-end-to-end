import pandas as pd

def ingest_transactions(path: str) -> pd.DataFrame:
    """
    Ingest raw transaction data.
    This is the ONLY place that reads raw data.
    """
    df = pd.read_csv(path)

    # minimal sanity cleanup
    df = df.dropna(subset=["CustomerID", "InvoiceDate"])
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    return df
