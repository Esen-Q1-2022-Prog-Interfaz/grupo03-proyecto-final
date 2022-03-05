DATA_BASE_NAME = 'pruebaxd'
USER = "root"
PASSWORD = "rootroot"

class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = f"mysql://{USER}:{PASSWORD}@localhost:3306/{DATA_BASE_NAME}"
    SQLALCHEMY_POOL_SIZE = 50
    SQLALCHEMY_POOL_TIMEOUT = 300
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #TODO: create a secret key
    SECRET_KEY = "parangaracutirimicuaro"