from dotenv import load_dotenv
from os import getenv

load_dotenv()

CONFIG_PARAMS = {
    'SECRET_KEY': getenv('SECRET_KEY')
}
