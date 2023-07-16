from frontend_simulator.config import settings
from frontend_simulator.fetcher import get_data_as_chunks
from frontend_simulator.producers.base_producer import BaseProducer


class Simulate:
    """
    TODO
    """

    def __init__(self, chunck_size: int, sleep: float):
        self.orders_producer = BaseProducer(topic_name="orders-topic", sleep_time=sleep)
        self.order_items_producer = BaseProducer(
            topic_name="order-items-topic", sleep_time=sleep
        )
        self.order_reviews_producer = BaseProducer(
            topic_name="order-review-topic", sleep_time=sleep
        )
        self.sleep = sleep
        self.chunk_size = chunck_size

    def simulate(self):
        """TODO"""
        orders = get_data_as_chunks(
            path=settings.PATH_TO_ORDERS, chunk_size=self.chunk_size
        )
        order_items = get_data_as_chunks(
            path=settings.PATH_TO_ORDER_ITEMS, chunk_size=self.chunk_size
        )
        order_reviews = get_data_as_chunks(
            path=settings.PATH_TO_ORDER_REVIEWS, chunk_size=self.chunk_size
        )
        self.orders_producer.send_message(messages=orders)
        self.order_items_producer.send_message(messages=order_items)
        self.order_reviews_producer.send_message(messages=order_reviews)
