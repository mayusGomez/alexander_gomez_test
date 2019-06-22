from flask import Flask

from .rest import cache_rest 
from .flask_settings import DevConfig
from .repository import memory


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    memory.init()

    @app.route('/')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(cache_rest.blueprint)
    return app
