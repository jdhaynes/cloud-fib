from flask import Flask, request
from work_queue import WorkQueue

app = Flask(__name__)


@app.route("/")
def heartbeat():
    return "Service OK."


@app.route("/compute/<index>", methods=["POST"])
def compute_fib(index):
    with WorkQueue() as queue:
        queue.publish_work_request(index)

    return "Success."


if __name__ == "__main__":
    app.run()
