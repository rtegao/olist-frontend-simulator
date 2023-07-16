import json
import time
from typing import Generator, List
from uuid import uuid4

from confluent_kafka import KafkaError, Message, Producer

from frontend_simulator.config import settings

class BaseProducer:
    """
    TODO
    """

    def __init__(self, topic_name: str, sleep_time: int):
        config = {
            "bootstrap.servers": settings.bootstrap_server,
            "client.id": "front-end-simulator",
            "queue.buffering.max.messages": 1000000,
            "queue.buffering.max.ms": 500,
        }

        self.producer = Producer(config)
        self.topic_name = topic_name
        self.sleep_time = sleep_time

    def delivery_report(self, err: KafkaError, msg: Message) -> None:
        """
        Delivery report callback function.

        Args:
            err (KafkaError): Error information, or None if message was successfully delivered.
            msg (Message): Message object containing delivery information.

        Returns:
            None

        """
        if err is not None:
            if err.name() == "KafkaError":
                # Error occurred during message production
                print(f"Message delivery failed: {err}")
            elif err.name() == "DrMsgPayloadOnly":
                # Message payload was delivered, but the report is an acknowledgment
                print(
                    f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}"
                )
        else:
            # Message successfully delivered
            print(
                f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}"
            )

    def send_message(self, messages: Generator):
        """
        TODO
        """
        try:
            for message in messages:
                serialized_message = json.dumps(message).encode("utf-8")
                self.producer.produce(
                    topic=self.topic_name,
                    key=str(uuid4()),
                    value=serialized_message,
                    callback=self.delivery_report,
                )
                # handle any pending events, such as message deliveries or message consumption, without blocking indefinitely.
                # It allows the producer to handle acknowledgment callbacks and errors related to message delivery.
                self.producer.poll(0)
            print("\nflushing records...")
            self.producer.flush()  # it ensures that all pending messages are delivered to the Kafka broker before the function returns.
        except Exception as e:
            print(f"Error occurred: {e}")
