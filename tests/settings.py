# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import


DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "v+s=%bl$5s30!o@wnz1v^6##6pxl@0zs1iz+ie3q3%q+@t)igc"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"
STATIC_URL = "/static/"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_jsonschema_widget",
]

SITE_ID = 1
