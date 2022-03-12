import os


class Config:
    RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST")
    RABBITMQ_PORT = os.environ.get("RABBITMQ_PORT")
    RABBITMQ_EXCHANGE = os.environ.get("RABBITMQ_EXCHANGE")
    RABBITMQ_QUEUE = os.environ.get("RABBITMQ_QUEUE")

    REDIS_HOST = os.environ.get("REDIS_HOST")
    REDIS_PORT = os.environ.get("REDIS_PORT")
    REDIS_DB = os.environ.get("REDIS_DB")
