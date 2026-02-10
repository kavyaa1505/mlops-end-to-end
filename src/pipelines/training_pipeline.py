import yaml

from ingestion.ingest import ingest_transactions
from feature_store.computation.batch_features import (
    compute_user_transaction_count_7d
)
from feature_store.validation.schema_checks import validate_feature_schema
from feature_store.validation.feature_checks import detect_breaking_changes


def load_change_policy():
    """
    Load declared breaking-change allowances.
    Defensive by design: config must not crash the system.
    """
    with open("src/feature_store/registry/change_policy.yaml") as f:
        policy = yaml.safe_load(f) or {}

    allowed = policy.get("allowed_breaking_changes")

    if allowed is None:
        return set()

    return set(allowed)


def run_training_pipeline(config):
    # 1️⃣ Ingest raw data
    transactions = ingest_transactions(config["data"]["raw_path"])

    # 2️⃣ Define feature computation cutoff
    as_of_date = transactions["InvoiceDate"].max()

    # 3️⃣ Compute features (ONLY via feature store)
    features = compute_user_transaction_count_7d(
        transactions=transactions,
        as_of_date=as_of_date
    )

    # 4️⃣ CHANGE GOVERNANCE (intent-aware)
    allowed_breaks = load_change_policy()

    current_feature_set = set(features.columns) - {"user_id"}
    registry_feature_set = {"user_transaction_count_7d"}

    detect_breaking_changes(
        current_features=current_feature_set,
        registry_features=registry_feature_set,
        allowed_breaks=allowed_breaks
    )

    # 5️⃣ Schema validation (contract enforcement)
    validate_feature_schema(
        features,
        {"user_transaction_count_7d": int}
    )

    print("✅ Features computed, governance checked, and schema validated")
    print(features.head())

    # Model training intentionally comes later
    return features
