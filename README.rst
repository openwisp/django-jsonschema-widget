=============================
django-jsonschema-widget
=============================

.. image:: https://badge.fury.io/py/django-jsonschema-widget.svg
    :target: https://badge.fury.io/py/django-jsonschema-widget

.. image:: https://travis-ci.org/openwisp/django-jsonschema-widget.svg?branch=master
    :target: https://travis-ci.org/openwisp/django-jsonschema-widget

.. image:: https://codecov.io/gh/openwisp/django-jsonschema-widget/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/openwisp/django-jsonschema-widget

Configuration widget for embedded device.

Documentation
-------------

The full documentation is at https://django-jsonschema-widget.readthedocs.io.

Quickstart
----------

Install django-jsonschema-widget::

    pip install django-jsonschema-widget

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
