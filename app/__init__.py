from apiflask import APIFlask
import openai
import os
from .config import Config
from app.promote_letter import bp as promote_letter_bp

def create_app(test_config=None):
    # create and configure the app
    app = APIFlask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    openai.api_key = Config.OPENAI_API_KEY
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/ping')
    def ping():
        return 'Ping!'


    app.register_blueprint(promote_letter_bp)


    return app

create_app()