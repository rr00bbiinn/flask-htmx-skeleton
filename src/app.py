from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    return app


def init_blueprints(app: Flask) -> None:
    pass


app = create_app()

if __name__ == "__main__":
    app.run(port=8080, debug=True)
