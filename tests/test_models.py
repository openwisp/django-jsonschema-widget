#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-jsonschema-widget
------------

Tests for `django-jsonschema-widget` widget module.
"""

from django.test import SimpleTestCase

from django_jsonschema_widget.widgets import JsonSchemaWidget


class TestJsonSchemaWidget(SimpleTestCase):
    def test_render(self):
        html = JsonSchemaWidget().render('config', '{"interfaces": []}', attrs={})
        self.assertIn('value="Advanced mode (raw JSON)"', html)
        self.assertIn(
            'django._netjsonconfigSchemaUrl = "/netjsonconfig/schema.json";', html
        )
        self.assertIn('class="vLargeTextField jsoneditor-raw"', html)
        self.assertIn('name="config"', html)
        self.assertIn('{&quot;interfaces&quot;: []}</textarea>', html)

    def test_media(self):
        media = str(JsonSchemaWidget().media)
        for path in [
            'css/lib/jsonschema-ui.css',
            'css/lib/advanced-mode.css',
            'js/lib/advanced-mode.js',
            'js/lib/tomorrow_night_bright.js',
            'js/lib/jsonschema-ui.js',
            'js/widget.js',
        ]:
            with self.subTest(path=path):
                self.assertIn(
                    '"/static/django-jsonschema-widget/{0}"'.format(path), media
                )
