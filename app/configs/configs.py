import logging


class BaseConfig:
    def __init__(self, *args, **kwargs):
        self.LOG_LEVEL = None
        self.DATABASE = None


class DevConfig(BaseConfig):
    def __init__(self, *args, **kwargs):
        self.LOG_LEVEL = logging.DEBUG
        self.DATABASE = 'app/assets/db_dev.csv'


class TestConfig(BaseConfig):
    def __init__(self, *args, **kwargs):
        self.LOG_LEVEL = logging.DEBUG
        self.DATABASE = 'app/assets/db_test.csv'


class ProductConfig(BaseConfig):
    def __init__(self, *args, **kwargs):
        self.LOG_LEVEL = logging.INFO
        self.DATABASE = 'app/assets/db_prod.csv'


CONFIGS = {
    'test': TestConfig,
    'develop': DevConfig,
    'product': ProductConfig,
}
