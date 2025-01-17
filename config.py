import os
from dotenv import load_dotenv

load_dotenv(".env.base")


class Config:
    USER = os.environ["USER"]
    PASSWORD = os.environ["PASSWORD"]
    EMPLOYEE_DB = os.environ["EMPLOYEE_DB"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    PORT = os.environ["PORT"]
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]
    SECRET_KEY = os.environ["SECRET_KEY"]
