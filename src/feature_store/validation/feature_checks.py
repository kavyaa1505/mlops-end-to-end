from pathlib import Path
import pandas as pd
import great_expectations as ge

DATA_PATH = Path("data/processed/data.csv")


def validate_data() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Processed data not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    ge_df = ge.from_pandas(df)

    ge_df.expect_column_values_to_not_be_null("Amount")
    ge_df.expect_column_values_to_be_between(
        "Amount", min_value=0, mostly=0.99
    )
    ge_df.expect_column_values_to_be_in_set("Class", [0, 1])

    results = ge_df.validate()

    if not results["success"]:
        raise ValueError("❌ Data validation failed")

    print("✅ Data validation passed successfully")


if __name__ == "__main__":
    validate_data()
