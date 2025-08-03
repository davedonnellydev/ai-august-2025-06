import os
from dotenv import load_dotenv

# Auto loads variables from .env files
load_dotenv()

# Default config


class Config:
    """Base configuration class"""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-key-change-in-production"
    DEBUG = False
    TESTING = False
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")


# Dev environment config w verbose logging
class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG = True
    LOG_LEVEL = "DEBUG"


# Test environment config w verbose logging
class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True
    DEBUG = True
    LOG_LEVEL = "DEBUG"


# Prod environment config w less verbose logging
class ProductionConfig(Config):
    """Production configuration"""

    DEBUG = False
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "WARNING")


# Config dictionary
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
