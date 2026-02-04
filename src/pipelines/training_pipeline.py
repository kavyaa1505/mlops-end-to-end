import pandas as pd
from ingestion.ingest import ingest_transactions
from feature_store.computation.batch_features import (
    compute_user_transaction_count_7d
)
from feature_store.validation.schema_checks import validate_feature_schema

def run_training_pipeline(config):
    transactions = ingest_transactions(config["data"]["raw_path"])

    as_of_date = transactions["InvoiceDate"].max()

    features = compute_user_transaction_count_7d(
        transactions=transactions,
        as_of_date=as_of_date
    )

    validate_feature_schema(
        features,
        {"user_transaction_count_7d": int}
    )

    print("✅ Features computed and validated")
    print(features.head())

    # model training will come later
    return features
