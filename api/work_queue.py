import pika
import env


class WorkQueue:
    def __init__(self):
        parameters = pika.ConnectionParameters(host=env.RABBITMQ_HOST,
                                               port=env.RABBITMQ_PORT)

        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange="fib")
        self.channel.queue_declare(queue="values")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def publish_work_request(self, index):
        self.channel.basic_publish(exchange="fib",
                                   routing_key="values",
                                   body=index)