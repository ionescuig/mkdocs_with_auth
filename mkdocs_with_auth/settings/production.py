from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = ['mkdocs-with-auth.herokuapp.com']        # you can add '<custom-domain>.com' in the list

# ---=== DATABASE ===---
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

print('-' * 50)
print('> BASE_DIR:', BASE_DIR)
print('> DOCS_DIR:', DOCS_DIR)

print()
print('> STATIC_URL:', STATIC_URL)
print('> STATIC_DIR:', STATIC_DIR)

print()
print('> STATIC_ROOT:', STATIC_ROOT)
print('> STATICFILES_STORAGE:', STATICFILES_STORAGE)

print()
print('> TEMPLATES_DIR:', TEMPLATES_DIR)
print('=' * 50)