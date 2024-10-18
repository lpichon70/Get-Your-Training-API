from sqlalchemy.engine import URL
import configparser
import os

config = configparser.ConfigParser()

config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

def get_db() -> URL:

    db_URL = URL.create(
        "mysql+pymysql",
        username=config.get('database','username'),
        password=config.get('database','password'),
        host="localhost",
        database="muscle_API",
    )

    return db_URL
