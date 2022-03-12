from flask import Flask, request

from api.api.infrastructure.rabbitmq import RabbitMqMessageBus
from api.api.infrastructure.redis import RedisCache
from api.api.rest.config import Config
from api.api.services.fib_service import FibService

app = Flask(__name__)


@app.route("/health")
def health():
    return "OK"


@app.route("/compute/<index>", methods=["POST"])
def compute(index):
    rabbitmq = RabbitMqMessageBus(host=Config.RABBITMQ_HOST,
                                  port=Config.RABBITMQ_PORT,
                                  exchange=Config.RABBITMQ_EXCHANGE)

    redis = RedisCache(host=Config.REDIS_HOST,
                       port=Config.REDIS_PORT,
                       db=Config.REDIS_DB)

    service = FibService(message_bus=rabbitmq, database=redis)
    return service.get_fib(index)


if __name__ == "__main__":
    app.run()
