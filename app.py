import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "Hello, DevOps!"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/info")
def info():
    return jsonify(
        {
            "version": os.getenv("APP_VERSION", "1.0.0"),
            "environment": os.getenv("ENVIRONMENT", "development"),
        }
    )


@app.route("/api/greet/<name>")
def greet(name):
    capitalized_name = name.capitalize()
    return jsonify(
        {
            "greeting": f"Hello, {capitalized_name}!",
            "name_length": len(name),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
