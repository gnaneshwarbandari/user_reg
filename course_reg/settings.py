import os
from pathlib import Path

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Security settings
SECRET_KEY = os.getenv('SECRET_KEY', 'your-production-secret-key')
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'course_reg',
    'userapp.apps.UserappConfig',
    'topicapp.apps.TopicappConfig',
    'courseapp.apps.CourseappConfig',
    'trainers.apps.TrainersConfig',
    'batchapp.apps.BatchappConfig',
    'studentapp.apps.StudentappConfig',
    'adminapp.apps.AdminappConfig',
    'crispy_forms',
    'crispy_bootstrap4',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'course_reg.middleware.RestrictStudentAccessMiddleware',
]

ROOT_URLCONF = 'course_reg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'course_reg.wsgi.application'

# Database configuration (SQLite for development)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',  # Replace with your MySQL database name
        'USER': 'root',       # Replace with your MySQL username
        'PASSWORD': 'root',   # Replace with your MySQL password
        'HOST': 'localhost',           # Or your database server IP
        'PORT': '3306',                # Default MySQL port
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static and media file settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

# Messages and crispy forms
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Authentication settings
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'userapp:login'

# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default, stores sessions in the database

# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # One week
# SESSION_COOKIE_AGE = 60   # One week
SESSION_COOKIE_SECURE = False # Set to True for HTTPS only, False for local development
SESSION_COOKIE_HTTPONLY = True # Save the session to the database on every request
SESSION_EXPIRE_AT_BROWSER_CLOSE = False # Session will not expire when the browser is closed
SESSION_SAVE_EVERY_REQUEST = True # Save the session to the database on every request

# messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Email backend (Console for development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.example.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@example.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'