import time

import pika
import env


class WorkQueue:
    def __init__(self):
        while True:
            try:
                parameters = pika.ConnectionParameters(host=env.RABBITMQ_HOST,
                                                       port=env.RABBITMQ_PORT)

                self.connection = pika.BlockingConnection(parameters)
                self.channel = self.connection.channel()

                self.channel.exchange_declare(exchange="fib")
                self.channel.queue_declare(queue="values")

                break
            except pika.exceptions.AMQPConnectionError:
                time.sleep(1)
                continue

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def subscribe(self, callback):
        self.channel.basic_consume(queue="values",
                                   auto_ack=True,
                                   on_message_callback=callback)

        self.channel.start_consuming()
