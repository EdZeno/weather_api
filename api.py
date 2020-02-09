import os

from flask import Flask, jsonify
from flask_cors import CORS


def create_app(config=None):
    app = Flask(__name__)

    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    CORS(app)

    @app.route('/', methods=['GET'])
    def home():
        return "Hello"

    @app.route('/ping/', methods=['GET'])
    def ping():

        # response = 'api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=a6121cbc06318911011306f3eaebaf2a&units=metric'
        # print(response)
        return {
        "name": "weatherservice",
        "status": "ok",
        "version": "1.0.0"
    }

    return app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
