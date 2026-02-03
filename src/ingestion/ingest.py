from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw/creditcard.csv")
PROCESSED_DATA_PATH = Path("data/processed/data.csv")


def ingest_data() -> pd.DataFrame:
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Raw data not found at {RAW_DATA_PATH}")

    df = pd.read_csv(RAW_DATA_PATH)

    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    return df


if __name__ == "__main__":
    df = ingest_data()
    print(f"✅ Data ingested successfully. Shape: {df.shape}")
