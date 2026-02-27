# import os
from pathlib import Path


def pytest_configure(config):
    # Only configure settings if we're actually running pytest
    # Never interfere with production Django settings
    import django
    from django.conf import settings

    if not settings.configured:
        BASE_DIR = Path(__file__).resolve().parent

        settings.configure(
            BASE_DIR=BASE_DIR,
            DEBUG=True,
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            INSTALLED_APPS=[
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'accounts',
                'tasks',
                'core',
            ],
            MIDDLEWARE=[
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ],
            ROOT_URLCONF='taskmanager.urls',
            TEMPLATES=[
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
            ],
            STATIC_URL='/static/',
            STATICFILES_DIRS=[BASE_DIR / 'static'],
            STATIC_ROOT=BASE_DIR / 'staticfiles',
            MEDIA_URL='/media/',
            MEDIA_ROOT=BASE_DIR / 'media',
            SECRET_KEY='test-secret-key-only-for-testing',
            DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
            LOGIN_URL='/accounts/login/',
            LOGIN_REDIRECT_URL='/',
            LOGOUT_REDIRECT_URL='/accounts/login/',
            MESSAGE_STORAGE='django.contrib.messages.storage.cookie.CookieStorage',
        )
        django.setup()
