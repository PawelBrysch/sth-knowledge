PYTHON_PATH = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\venv\Scripts\python.exe"
MANAGE_PY = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\less_Django\my_own_name\manage.py"

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


"""#######################################
MODEL workflow
#######################################"""
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


"""#######################################
DATABASE API
#######################################"""
"""
1. SELECT (+WHERE)
2. JOIN 
3. INSERT
4. DELETE

https://docs.djangoproject.com/en/3.0/intro/tutorial02/#s-playing-with-the-api

"""

"""#######################################
TEMPLATES
#######################################"""
"""
1. Budowanie urli w `.html` wg. url patternsow w `.'py' -> 
              -> https://docs.djangoproject.com/en/3.0/intro/tutorial03/#s-removing-hardcoded-urls-in-templates do konca
"""