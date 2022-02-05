import env
import fib
import redis
from work_queue import WorkQueue


def handle_message(ch, method, properties, body):
    fib_number = fib.compute(int(body.decode()))
    redis_client = redis.Redis(host=env.REDIS_HOST,
                               port=env.REDIS_PORT,
                               db=0)

    redis_client.set(body.decode(), fib_number)


class Worker:
    def start(self):
        with WorkQueue() as queue:
            queue.subscribe(handle_message)


if __name__ == "__main__":
    Worker().start()
