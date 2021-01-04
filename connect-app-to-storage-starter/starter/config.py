import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'examplesqlsvr.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'examplesqlsvrdb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'INeedMoney44'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'storageaccountudacityexe'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '0DFmEcT+OOZjO0mjbnE0at5sUy1G6662M/1Tij1fHegu5pbARRDM3HHcyq6G7h0oJ2iQyBMTOP4WI3v2o7DIQA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
