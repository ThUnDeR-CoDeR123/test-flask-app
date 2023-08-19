# # import environ
# import os


# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )


# Set the project base directory
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Take environment variables from .env file
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))/
# DEBUG = env('DEBUG')
SECRET_KEY = "d55cc5e7c5c840b29eac8831d43203da"
SQLALCHEMY_DATABASE_URI="postgresql://ecelilmw:Eb9eNRBLa1rQeA1O6eSAZjRC9BUJwDBm@tiny.db.elephantsql.com/ecelilmw"
