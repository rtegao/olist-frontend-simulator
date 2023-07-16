from typing import List

import pandas as pd


def format_date_columns(df_orders: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    TODO
    """

    for column in columns:
        df_orders[column] = pd.to_datetime(df_orders[column])
        df_orders[column + "_date"] = df_orders[column].dt.date
        df_orders[column + "_time"] = df_orders[column].dt.time
        df_orders = df_orders.drop(columns=[column])

    return df_orders
