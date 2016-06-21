# hbt
=====
ygag
=====

ygag is a simple Hello World kind of django project:

- home page should have a form that asks for a name
- on POST, the name should be saved in a database together with the date/time it was added, then redirect to...
- a view that displays "Hello, submitted name"
- activate the django admin and make the names listed with the date/time it was added
- Create a RESTful webservice API endpoint for returning the submitted names in JSON format (you can use django-rest-framework)
- the API endpoint should be protected by an authorization token

Quick start
-----------

1. Add "ygag" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ygag.apps.YgagConfig',,
        'rest_framework',
    ]

2. Include the ygag URLconf in your project urls.py like this::

    url(r'^ygag/', include('ygag.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
3. Any global settings for a REST framework API are kept in a single configuration dictionary named REST_FRAMEWORK. Start off by adding the following to your settings.py module:
    REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
    }

4. Run `python manage.py migrate` to create the ygag models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a name (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/ygag/ to add names

