# NOTE trzeba stworzyc ten plik
from django.urls import path
from . import views
from less_Django.external_code.my_code import my_custom_request_handler

# NOTE - gdy nie ma byc dodatkowego komponentu url ->                                                 path('', ..., ...)
urlpatterns = [
    path('optional_url_component/', my_custom_request_handler, name='some_name'),
]