"""
Réglages du portfolio CDB.

Étape actuelle : serveur de prototypes (aucune base de données).
Le vrai site (templates, i18n FR/EN, static, déploiement) viendra ensuite.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-only-not-a-secret')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# Pas de base de données pour l'instant.
DATABASES = {}

LANGUAGE_CODE = 'fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Dossier des prototypes HTML (servis tels quels, voir config/urls.py).
PROTOTYPES_DIR = BASE_DIR / 'prototypes'
