from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

# NOTE sprawia, ze mozna miec dwie wersje responsa (.api i .json)
urlpatterns = format_suffix_patterns(urlpatterns)