from flask import Flask
from flask_cors import CORS
from flask_restx import Api

api = Api(prefix="/api/v1", doc="/api/v1/docs")

app = Flask(__name__)
api.init_app(app)
CORS(app)


@app.route("/profile")
def my_profile():
    response_body = {
        "name": "Nagato",
        "about": "Hello! I'm a full stack developer that loves python and javascript",
    }

    return response_body


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
