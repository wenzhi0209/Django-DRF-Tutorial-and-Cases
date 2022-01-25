=====
polls_module
=====

polls_module is a Django app to conduct web-based polls_module. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls_module" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls_module',
    ]

2. Include the polls_module URLconf in your project urls.py like this::

    path('polls/', include('polls_module.urls')),

3. Run ``python manage.py migrate`` to create the polls_module models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
