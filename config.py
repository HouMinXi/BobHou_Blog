class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

class DevConfig(Config):
    debug = True


    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:hmx@10931@127.0.0.1:3306/flask"
