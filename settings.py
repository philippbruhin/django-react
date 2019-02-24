# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())


# all django settings can be altered here
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',)
}

CORS_ORIGIN_ALLOW_ALL=True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-disposition',
    'content-type',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
    '127.0.0.1:3000'
)


MIDDLEWARE.insert(
    MIDDLEWARE.index("django.middleware.common.CommonMiddleware") + 0,
    "corsheaders.middleware.CorsMiddleware"
)

INSTALLED_APPS.extend([
    # add your project specific apps here
    'leads',
    'rest_framework',
    'knox',
    'accounts',
    'corsheaders',
])
