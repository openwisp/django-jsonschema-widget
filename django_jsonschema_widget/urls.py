# -*- coding: utf-8 -*-
from django.urls import re_path
from django.views.generic import TemplateView


app_name = 'django_jsonschema_widget'
urlpatterns = [
    re_path(r'', TemplateView.as_view(template_name="base.html")),
]
