# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls


urlpatterns = [
    # add your own patterns here
    path('', include('leads.urls')),
    path('', include('accounts.urls'))
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
