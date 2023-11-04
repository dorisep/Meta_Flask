import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_kEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
###
#bash commands for setting env vars
#
#export SECRET_KEY="your secret key"
#
#export DATABASE_URI="postgresql://username:password@host:port/database_name"
#
###