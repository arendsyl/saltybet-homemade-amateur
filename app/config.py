ENVIRONMENT = 'DEV'  # "prod" or other
PRODUCTION_SERVER = ''
API_NAME = 'saltybet-homemade-amateur'
VERSION = '0.0.1'


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    API_NAME = API_NAME


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # SWAGGER Configuration
    SWAGGER_URL = '/api/docs'
    API_URL = 'http://127.0.0.1:5000/spec'


class ProductionConfig(BaseConfig):
    DEBUG = True
    # SWAGGER Configuration
    SWAGGER_URL = '/api/docs'
    API_URL = 'http://' + PRODUCTION_SERVER + ':5000/spec'
