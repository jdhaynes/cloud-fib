from flask import Flask, request
import fib

app = Flask(__name__)


@app.route("/")
def heartbeat():
    return "Service OK."


@app.route("/compute/<index>", methods=["POST"])
def compute_fib(index: int):
    return str(fib.compute(int(index)))


if __name__ == "__main__":
    app.run()
