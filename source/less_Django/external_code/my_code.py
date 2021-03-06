PYTHON_PATH = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\venv\Scripts\python.exe"
MANAGE_PY = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\less_Django\my_own_name\manage.py"

"""#######################################
catalog of names
#######################################"""
# generic views

"""#######################################
APP
#######################################"""
"""how to add app from external source?"""
# #---# in 'mysite.setting.py'
# import sys
# sys.path.insert(0, r"path\to\containing_directory")
#
# INSTALLED_APPS = [
#     ...,
#     'some_app.apps.SomeAppConfig',
#     ...
# ]

"""#######################################
URL DISPATCHER
#######################################"""
""" api """
# from django.urls import path
# from django.http import HttpResponse
#
# some_pattern = '<int:question_id>/'
# some_request_handler = lambda x: HttpResponse("Some output")
#
# next_url = path(some_pattern, some_request_handler, name='some_name'),
#
# urlpatterns = [
#     # ...
#     next_url
#     # ...
# ]

"""#######################################
VIEWS
#######################################"""
""" Przykladowy view"""
# from django.http import HttpResponse
# def my_custom_request_handler(request):
#     return HttpResponse("could be: string, template or JSON (?)")

"""Wyrzucenie 404 (w ciele widoku)"""
"""
czy trzeba cos returnowac? ->                                                          NIE, robi się samo (404 w sensie)
"""
# from django.http import Http404
# raise Http404

"""VIEW - MODEL recoupling"""
"""
o co chodzi? ->                                                       np. o 'get_object_or_404(ModelName, pk=chosen_id)'
"""

''' POST '''
# def view_getting_POST(request):
#    data = request.POST


''' creating_urls_on_fly '''
# from django.urls import reverse
#
# # ASSUME # path('<int:some_arg>/', some_view_func, name='some_view_name'),
# namespace_name = "some_namespace_name"
# view_name = "some_view_name"
# arguments_from_pattern = (123,)
#
# rendered_url = reverse(
#     viewname=":".join([namespace_name, view_name]),
#     args=arguments_from_pattern
# )


''' redirection '''
# from django.http import HttpResponseRedirect
# def some_view(request):
#     ...
#     return HttpResponseRedirect("some/url")

"""#######################################
MODEL workflow
#######################################"""
""" workflow """
# from less_Django.external_code.scripts_ import run_command_line
# def commit_changes_in_app_models(app_name):
#     run_command_line([
#         PYTHON_PATH, MANAGE_PY, "makemigrations", app_name
#     ])
#
# def push_changes_in_ALL_models():
#     run_command_line([
#         PYTHON_PATH, MANAGE_PY, "migrate"
#     ])

"""`Model.objects.create()` zamiast `Model()`"""
# # https://stackoverflow.com/questions/26672077/django-model-vs-model-objects-create


"""#######################################
DATABASE API
#######################################"""
"""
1. SELECT (+WHERE <filter>)
    `__lte` -> "less than or equal"
2. JOIN 
3. INSERT
4. DELETE

https://docs.djangoproject.com/en/3.0/intro/tutorial02/#s-playing-with-the-api

"""

"""#######################################
TESTING
#######################################"""
"""
* Nice features:
1. self.assertIs(), etc.
2. create separate DB (???)
"""

''' `model tests` vs `view tests`'''
#   # w `view tests` trzeba pushowac obiekty do bazy, a w `model tests` nie

"""`Client`"""
"""
    na jakiej bazie tutaj pracujemy? ->                                                                       na devowej
"""
# from less_Django.external_code.scripts_ import get_pseudo_client
# from django.urls import reverse
#
#
# path_to_project = "C:\\Users\\Lenovo\\Desktop\\PROJECTS\\PROGRAMMING\\top_proper\\sth-knowledge\\source\\less_Django\\my_own_name"
# some_url_pattern_name = 'polls:index'
# some_context_key = 'latest_question_list'
#
# client = get_pseudo_client(path_to_project)
# response = client.get(reverse(some_url_pattern_name))
# print(response.context[some_context_key])

"""running test script"""
# from less_Django.external_code.scripts_ import run_command_line
# app_name = "some_app_name"
#
#
# def test_scripts():
#     run_command_line([
#         PYTHON_PATH, MANAGE_PY, "test", app_name
#     ])

"""test template"""
# from django.test import TestCase
#
# class STHTests(TestCase):
#     def test_sth(self):
#         self.assertIs(True, True)



"""#######################################
LOGGING
#######################################"""
# import logging
# logger = logging.getLogger("anything, REALLY!")
# logger.warning("sth")


"""#######################################
TEMPLATES
#######################################"""
"""
1. Budowanie urli w `.html` wg. url patternsow w `.'py' -> 
              -> https://docs.djangoproject.com/en/3.0/intro/tutorial03/#s-removing-hardcoded-urls-in-templates do konca
"""