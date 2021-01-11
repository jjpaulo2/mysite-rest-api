from dotenv import load_dotenv
from os import getenv

load_dotenv()

def is_debug():
    debug = getenv('DEBUG')
    return debug != '0'


CONFIG_PARAMS = {
    'SECRET_KEY': getenv('SECRET_KEY'),
    'DROPBOX_OAUTH2_TOKEN': getenv('DROPBOX_OAUTH2_TOKEN'),
    'DEBUG': is_debug(),
}
