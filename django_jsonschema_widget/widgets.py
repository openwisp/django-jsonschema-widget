from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib.admin.templatetags.admin_static import static
from django.contrib.admin.widgets import AdminTextareaWidget
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class JsonSchemaWidget(AdminTextareaWidget):
    """
    JSON Schema Editor widget
    """
    @property
    def media(self):
        prefix = 'django-jsonschema-widget'
        js = [static('{0}/js/{1}'.format(prefix, f))
              for f in ('lib/advanced-mode.js',
                        'lib/tomorrow_night_bright.js',
                        'lib/jsonschema-ui.js',
                        'widget.js')]
        css = {'all': [static('{0}/css/{1}'.format(prefix, f))
                       for f in ('lib/jsonschema-ui.css',
                                 'lib/advanced-mode.css')]}
        return forms.Media(js=js, css=css)

    def render(self, name, value, attrs=None, renderer=None, **kwargs):
        attrs['class'] = 'vLargeTextField jsoneditor-raw'
        html = """
<input class="button json-editor-btn-edit advanced-mode" type="button" value="{0}">
<script>django._netjsonconfigSchemaUrl = "{1}";</script>
<label id="netjsonconfig-hint">
    Want learn to use the advanced mode? Consult the
    <a href="http://netjsonconfig.openwisp.org/en/stable/general/basics.html"
       target="_blank">netjsonconfig documentation</a>.
</label>
"""
        html = html.format(_('Advanced mode (raw JSON)'),
                           reverse('netjsonconfig:schema'))
        html += super(JsonSchemaWidget, self).render(name, value, attrs, renderer, **kwargs)
        return html
