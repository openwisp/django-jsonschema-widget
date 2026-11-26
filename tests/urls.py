# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.http import JsonResponse
from django.urls import include, path, re_path

# The widget points its editor at the schema served by the
# "netjsonconfig:schema" URL, which the project that uses it provides.
netjsonconfig_urls = (
    [path('schema.json', lambda request: JsonResponse({}), name='schema')],
    'netjsonconfig',
)

urlpatterns = [
    path('netjsonconfig/', include(netjsonconfig_urls)),
    re_path(r'^', include('django_jsonschema_widget.urls', namespace='django_jsonschema_widget')),
]
