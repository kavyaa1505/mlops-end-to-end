import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/processed/data.csv")


def test_processed_data_exists():
    assert DATA_PATH.exists(), "Processed data file does not exist"


def test_required_columns_exist():
    df = pd.read_csv(DATA_PATH)
    required_columns = {"Amount", "Class"}
    assert required_columns.issubset(df.columns)


def test_class_column_values():
    df = pd.read_csv(DATA_PATH)
    assert set(df["Class"].unique()).issubset({0, 1})
