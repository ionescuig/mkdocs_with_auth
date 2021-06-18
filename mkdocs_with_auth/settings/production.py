from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ['mkdocs-with-auth.herokuapp.com']        # you can add '<custom-domain>.com' in the list

# ---=== DATABASE ===---
# after DATABASES = {...} add this:
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

# ---=== STATICFILES ===---
# at the end of the file
STATIC_URL = '/staticfiles_dir/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
