class BaseConfig(object):
    # SQLALCHEMY_DATABASE_URI = "sqlite:///raices.db"
    SQLALCHEMY_DATABASE_URI = "mysql://b848d6e2f90ff2:15ac7a17@us-cdbr-east-05.cleardb.net/heroku_7a5d8a412fdac8b" 
    SQLALCHEMY_POOL_SIZE = 50
    SQLALCHEMY_POOL_TIMEOUT = 300
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "1414892a04d3eb59b0c9953af3487cb1ff88152eb386b3bc50feac70e68098d71c682f63d3c0d8b5"
    LOGIN_DISABLE = True
