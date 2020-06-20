import lesson_requests
from lesson_requests.auth import HTTPBasicAuth
import json

url = "https://jirafortests.atlassian.net/rest/api/3/project/10000/components"

auth = HTTPBasicAuth('pawel.brysch@gmail.com', 'XdBRpmvYfEavbfSIIwqn1BEF')

headers = {
   "Accept": "application/json"
}

response = lesson_requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(response.text)