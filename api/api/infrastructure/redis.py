from api.api.services.ports.database import FibDatabasePort
import redis


class RedisCache(FibDatabasePort):
    def __init__(self, host: str, port: int, db: str) -> object:
        self.__client = redis.Redis(host=host, port=port, db=db)

    def get_fib(self, index: int) -> int:
        return self.__client.get(index)
