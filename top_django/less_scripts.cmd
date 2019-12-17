REM create boilerplate
django-admin startproject mysite

REM run server (dev)
python mysite\manage.py runserver

REM create app (boilerplate)
python manage.py startapp my_first_app

REM ####################################
REM Moving model to DB.
REM ####################################

REM migrate data do DB
python manage.py makemigrations my_first_app

REM migrate data do DB
python manage.py startapp my_first_app
