# LearningDjango
Repository for learning the Django framework.

Attention: this is not a tutorial, it is just a project for me to test and implement what I learn from tutorials and documentations using the django python framework. <br>
Disclaimer: Currently (July/2020), as you can see, I do not claim to have fluency in English, which means that many English errors can be found in this readme. Sorry for the inconvenience.
Primarily, this repository is being build by following this Python Django Tutorial: https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

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

## Version 03:
  1. Created a folder called "templates" inside the _app_name_ folder, and inside the new folder was created a folder called _app_name_. This is the way Django works with templates. The _blog_templates.html_ will be inside that last folder.
  2. Add the _app_name_ to the installed apps in settings.py file. Go to the apps.py file inside the _app_name_ folder and copy the only function of that file to the installed apps list in settings.py like this: '_app_name_.apps._functionName_'.
  3. It is possible to write code into the html files used by render. It is something like this:<br>
  _{% for post in posts %}<br>
    <h1>{{post.title}}</h1><br>
  {% endfor %}<br>_
  post is a dictionary passed as argument in the render function.
  4. It is useful to have a base.html file that will hold a base html code that most of the apps pages will expand from it.
  5. Create a foler called _static_ inside the _app_name_'s folder. That folder will contain another folder called _app_name_. Inside this last folder you will put static css files, like a main.css.
  6. In order to use the static css files, this following code must be included at the base.html file: {% load static %}
  7. Using a url tag in the html are better by passing the routes arguments, and not put directly the link for the page.
