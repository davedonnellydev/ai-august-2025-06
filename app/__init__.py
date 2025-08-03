import logging
from flask import Flask
from flask_talisman import Talisman
from app.proxy import proxy_bp
from app.health import health_bp
from app.main import main_bp
from app.config import config


def create_app(config_name="default"):
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config[config_name])

    # Setup logging
    logging.basicConfig(
        level=getattr(logging, app.config["LOG_LEVEL"]),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Setup security headers (only in production)
    if config_name == "production":
        Talisman(app, force_https=True)
    else:
        Talisman(app, force_https=False)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(proxy_bp)
    app.register_blueprint(health_bp)

    # Register error handlers
    from app.errors import register_error_handlers

    register_error_handlers(app)

    return app
