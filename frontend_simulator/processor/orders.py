import pandas as pd
from fetcher import get_data

from frontend_simulator.config import settings
from frontend_simulator.processor import format_date_columns


def process_orders(df_orders: pd.DataFrame) -> pd.DataFrame:
    """
    TODO
    """
    df_orders = get_data(settings.PATH_TO_ORDERS)

    columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]
    df_orders = format_date_columns(df=df_orders, columns=columns)

    return df_orders
