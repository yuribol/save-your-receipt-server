import logging
from flask import Flask


def __import_variable(blueprint_path, module, variable_name):
    path = '.'.join(blueprint_path.split('.') + [module])
    mod = __import__(path, fromlist=[variable_name])
    return getattr(mod, variable_name)


def config_str_to_obj(cfg):
    if isinstance(cfg, basestring):
        module = __import__('config', fromlist=[cfg])
        return getattr(module, cfg)
    return cfg

def app_factory(app_name, blueprints=None):
    app = Flask(__name__)
    app.config.from_pyfile('config/config.cfg')

    # config = config_str_to_obj(config)
    configure_app(app, app.config)
    configure_logger(app, app.config)
    configure_blueprints(app, blueprints or app.config["BLUEPRINTS"])
    configure_database(app)
    # configure_extensions(app)
    # configure_before_request(app)
    # configure_views(app)

    return app

def configure_app(app, config):
    """Loads configuration class into flask app"""
    app.config.from_object(config)
    app.config.from_envvar("APP_CONFIG", silent=True)  # available in the server


def configure_logger(app, config):
    log_filename = "app/logs/flask-server.log"

    # Create a file logger since we got a logdir
    log_file = logging.FileHandler(filename=log_filename)
    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]")
    log_file.setFormatter(formatter)
    log_file.setLevel(logging.INFO)
    app.logger.addHandler(log_file)
    app.logger.info("Logger started")


def configure_blueprints(app, blueprints):
    """Registers all blueprints set up in config.py"""
    for blueprint_config in blueprints:
        blueprint, kw = None, {}

        if isinstance(blueprint_config, basestring):
            blueprint = blueprint_config
        elif isinstance(blueprint_config, tuple):
            blueprint = blueprint_config[0]
            kw = blueprint_config[1]
        else:
            print "Error in BLUEPRINTS setup in config.py"
            print "Please, verify if each blueprint setup is either a string or a tuple."
            exit(1)

        blueprint = __import_variable("app.rest", "receipt", blueprint)
        app.register_blueprint(blueprint.bp, url_prefix="/v1" + blueprint.bp_prefix)

def configure_database(app):
    """
    Database configuration should be set here
    """
    # uncomment for sqlalchemy support
    from database.db import db
    db.app = app
    db.init_app(app)
