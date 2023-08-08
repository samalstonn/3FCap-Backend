from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from etrade.login import oauth

api = Api()

app = Flask(__name__)
api.init_app(app)
CORS(app)


@app.route("/portfolio")
def get_portfolio():
    return oauth()


@app.route("/profile")
def my_profile():
    response_body = {
        "name": "Nagato",
        "about": "Hello! I'm a full stack developer that loves python and javascript",
    }

    return response_body


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
