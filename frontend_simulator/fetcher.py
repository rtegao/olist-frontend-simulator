from typing import Dict, List

import pandas as pd


def get_data(path: str) -> pd.DataFrame:
    """
    TODO
    """
    return pd.read_csv(path)


def get_data_as_chunks(path: str, chunk_size: int) -> List[Dict]:
    """
    TODO
    """
    data = get_data(path)
    max_size = len(data.index)
    for i in range(0, max_size, chunk_size):
        yield data.iloc[i : i + chunk_size, :].to_dict()
