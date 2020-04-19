from flask import Flask, escape, request


def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app


def register_routes(app):

    @app.route('/')
    def hello():
        name = request.args.get("name", "World")
        return f'Hello, {escape(name)}!'
