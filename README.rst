=============================
Django Ubigeo
=============================

A database with Ubigeo codes

Usage
----------

Install Django Ubigeo::

    pip install git+ssh://git@bitbucket.org/minsa_dev/django_ubigeo.git
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata data.json

Then use it in a project::

    import ubigeo

Features
--------

* ICD10 model

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
