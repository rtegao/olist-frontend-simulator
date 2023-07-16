import pandas as pd
from fetcher import get_data

from frontend_simulator.config import settings
from frontend_simulator.processor import format_date_columns


def process_order_reviews(df_order_items: pd.DataFrame) -> pd.DataFrame:
    """
    TODO
    """
    df_order_items = get_data(settings.PATH_TO_ORDER_ITEMS)

    columns = ["review_creation_date", "review_answer_timestamp"]
    df_order_items = format_date_columns(df=df_order_items, columns=columns)
    return df_order_items
