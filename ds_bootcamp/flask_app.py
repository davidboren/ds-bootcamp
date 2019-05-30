from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello, World!", 200

    @app.route("/bye")
    def goodby_world():
        raise Exception("BLAHD")
        return "Goodbye, World!", 200

    return app
