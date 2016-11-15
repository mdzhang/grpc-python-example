"""Per environment settings for grpc_python_example.apis.http."""

# pylint: disable=too-few-public-methods, missing-docstring


class Config(object):
    DEBUG = True


class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'


class StagingConfig(Config):
    ENV = 'staging'


class TestConfig(Config):
    ENV = 'test'
