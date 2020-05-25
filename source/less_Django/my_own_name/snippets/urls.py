from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),
]

# NOTE
"""
czy jak wylaczymy, to juz nie ma jsonów? ->                                                                NIE, dalej są
"""
# urlpatterns = format_suffix_patterns(urlpatterns)