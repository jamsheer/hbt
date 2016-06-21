# hbt
=====
Names
=====

Names is a simple Hello World kind of django project:

- home page should have a form that asks for a name
- on POST, the name should be saved in a database together with the date/time it was added, then redirect to...
- a view that displays "Hello, <submitted name>"
- activate the django admin and make the names listed with the date/time it was added
- Create a RESTful webservice API endpoint for returning the submitted names in JSON format (you can use django-rest-framework)
- the API endpoint should be protected by an authorization token

Quick start
-----------

1. Add "names" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'names',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^names/', include('names.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/names/ to add names

