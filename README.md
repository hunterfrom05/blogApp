# Django project
## _Blog application files_
## Features
    + ***__init__.py***: an empty file that tells Python to treat the blog directory as a Python module.
    + ***admin.py***: This is where your register models to include them in the Django administration site (using of site is optional)
    + ***apps.py***: This includes the main configuration of the blog application
    - ***migrations.py***: This directory will contain database migrations of the application. Migrations allow Django to track your model changes and synchronize the database accordingly. This directory contain an empty __init__.py file
    + ***models.py***: This includes the data models of my application; all Django applications need to have a `models.py` file but it can be left empty
    + ***tests.py***: This is where you can add tests for your application.
    + ***views.py***: The logic of your application goes here, each view receives an HTTP request, precesses it , and returns a response.
With the applciation stucture ready, we can start building our app