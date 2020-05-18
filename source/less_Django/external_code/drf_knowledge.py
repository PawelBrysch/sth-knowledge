"""#####################################
HTTP METHODS dispatcher
#####################################"""
"""dispatcher (link below)"""
# from less_Django.my_own_name.snippets import views

"""`client`"""
# TODO czy czasem nie ida static files za kazdym razem, gdy nie ma .json w URL
# from less_Django.external_code.scripts_ import get_printable_json_or_status_code as get_pjosc
#
# new_record = {
#     "id": 9, #optional if posts
#     "title": "",
#     "code": "print(\"hello, 6th world\")",
#     "linenos": False,
#     "language": "python",
#     "style": "friendly"
# }
#
# all_records = get_pjosc("GET", r"/snippets.json")
# record_putted_in_this_line_v1 = get_pjosc("POST", r"/snippets/", json=new_record)
# status_after_deleting = get_pjosc("DELETE", r"/snippets/2/", json=new_record)
# record_putted_in_this_line_v2 = get_pjosc("PUT", r"/snippets/9/", json=new_record)



"""#####################################
API view vs CLASS_BASED view
#####################################"""
"links"
# API -> https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#pulling-it-all-together
# CLASS -> https://www.django-rest-framework.org/tutorial/3-class-based-views/




"""#####################################
`DOUBLE` views
#####################################"""
"""--> urls.py"""
# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = ...
# urlpatterns = format_suffix_patterns(urlpatterns)
"""--> views.py"""
# def some_view(request, format=None):
#     return ...


"""#####################################
SIMPLER ALTERNATIVES
#####################################"""
"""from rest_framework.response import Response"""
# from django.http import JsonResponse

"""serializer = SomeModelSerializer(data=request.data)"""
# data = JSONParser().parse(request)



