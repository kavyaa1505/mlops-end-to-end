import pandas as pd

def compute_user_transaction_count_7d(
    transactions: pd.DataFrame,
    as_of_date: pd.Timestamp
) -> pd.DataFrame:
    """
    Compute number of transactions per user in the last 7 days.

    Returns a feature dataframe:
    user_id | user_transaction_count_7d
    """

    window_start = as_of_date - pd.Timedelta(days=7)

    window_df = transactions[
        (transactions["InvoiceDate"] > window_start) &
        (transactions["InvoiceDate"] <= as_of_date)
    ]

    feature_df = (
        window_df
        .groupby("CustomerID")
        .size()
        .reset_index(name="user_transaction_count_7d")
        .rename(columns={"CustomerID": "user_id"})
    )

    return feature_df
