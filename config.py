import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST='app/static/photos'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465 
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True
    MAIL_USERNAME='appskelvin5@gmail.com'
    MAIL_PASSWORD='sjyhfgizwssnlttl'
    SIMPLEMDE_JS_IIFE=True
    SIMPLEMDE_USE_CDN=True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    pass

config_options= {
    'development': DevConfig,
    'production': ProdConfig
}