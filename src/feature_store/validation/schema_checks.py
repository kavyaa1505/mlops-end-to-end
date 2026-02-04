def validate_feature_schema(df, expected_schema: dict):
    """
    Ensure features match the contract.
    expected_schema = {column_name: dtype}
    """
    for col, dtype in expected_schema.items():
        if col not in df.columns:
            raise ValueError(f"Missing required feature: {col}")

        if not df[col].map(lambda x: isinstance(x, dtype)).all():
            raise TypeError(f"Feature {col} has incorrect type")

    return True
