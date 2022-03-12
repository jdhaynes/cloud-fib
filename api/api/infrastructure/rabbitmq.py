from typing import Callable
import pika

from api.api.services.ports.message_bus import MessageBusPort


class RabbitMqMessageBus(MessageBusPort):
    def __init__(self, host: str, port: int, exchange: str, queue: str) -> None:
        self.__channel = None
        self.__connection = None
        self.__host = host
        self.__port = port
        self.__exchange = exchange
        self.__queue = queue

        self.connected = False

    def connect(self) -> None:
        params = pika.ConnectionParameters(host=self.__host,
                                           port=self.__port)

        self.__connection = pika.BlockingConnection(params)
        self.__channel = self.__connection.channel()

    def close_connection(self) -> None:
        self.__connection.close()

    def publish(self, queue: str, body: str) -> None:
        if not self.connected:
            self.connect()

        self.__channel.basic_publish(exchange=self.__exchange,
                                     routing_key=self.__queue,
                                     body=body)

    def subscribe(self, queue: str, callback: Callable[[str], None]) -> None:
        if not self.connected:
            self.connect()

        self.__channel.basic_consume(queue=self.__queue,
                                     auto_ack=True,
                                     on_message_callback=callback)

        self.__channel.start_consuming()

    def declare(self) -> None:
        self.__channel.exchange_declare(exchange=self.__exchange)
        self.__channel.queue_declare(queue=self.__queue)
        self.__channel.queue_bind(exchange=self.__exchange,
                                  queue=self.__queue,
                                  routing_key=self.__queue)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()
