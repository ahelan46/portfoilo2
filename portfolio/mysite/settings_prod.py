import os
from .settings import *

# Override with environment variables for production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

hosts = os.environ.get('DJANGO_ALLOWED_HOSTS', '')
if hosts:
    ALLOWED_HOSTS = [h.strip() for h in hosts.split(',') if h.strip()]
else:
    ALLOWED_HOSTS = []

# Security defaults
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'True') == 'True'
SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'True') == 'True'
CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', 'True') == 'True'
X_FRAME_OPTIONS = 'DENY'

# Use WhiteNoise for static file serving in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Allow additional trusted origins (comma-separated)
trusted = os.environ.get('CSRF_TRUSTED_ORIGINS', '')
if trusted:
    CSRF_TRUSTED_ORIGINS = [t.strip() for t in trusted.split(',') if t.strip()]

# Database from DATABASE_URL (Render managed Postgres or other URL)
try:
    import dj_database_url
except Exception:
    dj_database_url = None

DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL and dj_database_url:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=not DEBUG)
    }
