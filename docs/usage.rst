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

Add django-jsonschema-widget's URL patterns:

.. code-block:: python

    from jsonschema_widget import urls as jsonschema_widget_urls


    urlpatterns = [
        ...
        url(r'^', include(jsonschema_widget_urls)),
        ...
    ]
