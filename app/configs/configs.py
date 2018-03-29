import logging


class BaseConfig:
    def __init__(self, *args, **kwargs):
        self.LOG_CONFIGS = {}
        self.DATABASE = None


class DevConfig(BaseConfig):
    def __init__(self, *args, **kwargs):
        self.LOG_LEVEL = logging.DEBUG
        self.LOG_FILENAME = 'app/assets/actions.log'
        self.LOG_CONFIGS = {
            'level': 10,
            'filename': 'app/assets/actions.log',
        }
        self.DATABASE = 'app/assets/db_dev.csv'


class TestConfig(BaseConfig):
    def __init__(self, *args, **kwargs):
        self.LOG_LEVEL = logging.DEBUG
        self.DATABASE = 'app/assets/db_test.csv'
        self.LOG_FILENAME = 'app/assets/actions.log'


class ProductConfig(BaseConfig):
    def __init__(self, *args, **kwargs):
        self.LOG_LEVEL = logging.INFO
        self.DATABASE = 'app/assets/db_prod.csv'
        self.LOG_FILENAME = 'app/assets/actions.log'


CONFIGS = {
    'test': TestConfig,
    'develop': DevConfig,
    'product': ProductConfig,
}
