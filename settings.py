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

INSTALLED_APPS.extend([
    # add your project specific apps here
    'leads',
    'rest_framework',
    'knox',
    'accounts',
    'corsheaders',
])

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

MIDDLEWARE.insert(
        MIDDLEWARE.index("corsheaders.middleware.CorsMiddleware") + 1,
        "django.middleware.common.CommonMiddleware"
    )

CORS_ORIGIN_ALLOW_ALL=True