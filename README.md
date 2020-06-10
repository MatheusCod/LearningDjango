# LearningDjango
Repository for learning the Django framework.

Attention: this is not a tutorial, it is just a project for me to test and implement what I learn from tutorials and documentations using the django python framework. <br>
Disclaimer: Currently (July/2020), as you can see, I do not claim to have fluency in English, which means that many English errors can be found in this readme. Sorry for the inconvenience.

## Version 01:
 1. Install Django with pip3 install django
 2. Check if django is installed with: $ python3 -m django --version
 3. Check admin option with: $ django-admin
 3. Create a project with: $ django-admin startproject _project_name_
 4. (Inside the project folder) Run server with: $ python3 manage.py runserver

## Version 02:
 (Inside the project folder)
 1. Create an app with: $ python3 manage.py startapp _app_name_
 2. Create a urls.py file inside the app folder.
 A blog app and a route to the blog app was created in this version.

 Routes:
  The user access "localhost:8000/blog", for example, which goes to urls.py on the main project, where is a url pattern pointing to the _app_name_.urls by using the include('_app_name_.url'). <br> In the _app_name_'s urls.py file there is a pattern with a route that points to the views.py module, which have a function with a _request_ as parameter and a _HttpResponse_ as return of the function.
