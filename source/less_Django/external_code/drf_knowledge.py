

"""#####################################
HTTP METHODS dispatcher
#####################################"""
"""link below"""
# from less_Django.my_own_name.snippets import views

"""#####################################
??? 
#####################################"""
from less_Django.external_code.scripts_ import get_printable_json
import requests

# TODO ujednolic te metode
json_ = get_printable_json("GET", r"/snippets.json")
print(json_)

# url_ = r"http://127.0.0.1:8000/snippets/"
#
#
# snippet = {
#     # "id": 7,
#     "title": "",
#     "code": "print(\"hello, THIRD world\")",
#     "linenos": False,
#     "language": "python",
#     "style": "friendly"
# }
# r = requests.post(url_, json=snippet)



