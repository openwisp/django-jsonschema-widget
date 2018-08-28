=====
Usage
=====

To use django-jsonschema-widget in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'jsonschema_widget.apps.JsonschemaWidgetConfig',
        ...
    )

Please add django-jsonschema-widget's URL patterns in your project's ``urls.py``:

.. code-block:: python

    from jsonschema_widget import urls as jsonschema_widget_urls


    urlpatterns = [
        ...
        url(r'^', include(jsonschema_widget_urls)),
        ...
    ]
