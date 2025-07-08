import os
import dj_database_url
from pathlib import Path

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان
SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme-in-production')

# وضع التصحيح
DEBUG = os.environ.get("DEBUG", "False") == "True"

# النطاقات المسموحة
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'survey-sbe6.onrender.com']

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'pages',
    'surveys',
    'rewards',
    'accounts',
    'rest_framework',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/auth/auth/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ✅ قاعدة البيانات (تقرأ من DATABASE_URL)
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ar'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'frontend', 'static'),  # إن وجد فعليًا
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ✅ نموذج تسجيل الدخول المخصص
ACCOUNT_FORMS = {
    'login': 'accounts.forms.CustomLoginForm',
}

# ✅ رابط تسجيل الدخول الافتراضي
LOGIN_URL = '/auth/auth/'

# Trigger Render deploy for static files
