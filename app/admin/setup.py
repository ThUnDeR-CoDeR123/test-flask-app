import environ
import os


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
SQLALCHEMY_DATABASE_URI=env('SQLALCHEMY_DATABASE_URI')
