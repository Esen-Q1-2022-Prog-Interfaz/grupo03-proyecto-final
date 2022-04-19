class BaseConfig(object):
    # SQLALCHEMY_DATABASE_URI = "sqlite:///raices.db"
    SQLALCHEMY_DATABASE_URI = "mysql://b24279e4057c7b:14ff250a@us-cdbr-east-05.cleardb.net/heroku_3ff1f77bec6ca8a" 
    SQLALCHEMY_POOL_SIZE = 50
    SQLALCHEMY_POOL_TIMEOUT = 300
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "1414892a04d3eb59b0c9953af3487cb1ff88152eb386b3bc50feac70e68098d71c682f63d3c0d8b5"
    LOGIN_DISABLE = True
