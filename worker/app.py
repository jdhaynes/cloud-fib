from flask import Flask

app = Flask(__name__)


@app.route("/")
def heartbeat():
    return "Service OK."


if __name__ == "__main__":
    app.run()
