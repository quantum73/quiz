import os
import secrets

from dotenv import dotenv_values

env_config = dotenv_values(".env")

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = env_config.get('SECRET_KEY', secrets.token_hex())
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = env_config.get('HOST', '127.0.0.1')
    PORT = env_config.get('PORT', 5000)
    EXTERNAL_API_URL = 'https://jservice.io/api/random?count=1'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = env_config.get(
        'DEV_DATABASE_URL',
        f"sqlite:///{os.path.join(basedir, 'data_dev.sqlite')}"
    )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = env_config.get(
        'TEST_DATABASE_URL',
        f"sqlite:///{os.path.join(basedir, 'data_test.sqlite')}"
    )


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = env_config.get(
        'DATABASE_URL',
        f"sqlite:///{os.path.join(basedir, 'data_prod.sqlite')}"
    )


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
