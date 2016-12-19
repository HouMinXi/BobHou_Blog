class Config(object):
    SECRET_KEY = '49453b26ed7f1bb84b2be7c1245851c9'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

class DevConfig(Config):
    debug = True


    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:hmx@10931@127.0.0.1:3306/flask"
