

# NOTE plik trzeba bylo stworzyc


from django.urls import path

from . import views

# NOTE dodajemy widok do: apki
urlpatterns = [
    path('', views.index, name='index'),
]