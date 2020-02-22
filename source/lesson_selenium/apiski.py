'''##########################
Wyslanie parametru
##########################'''
import lesson_requests
parameter = {"rel_rhy":"jingle"}
request = lesson_requests.get('https://api.datamuse.com/words', parameter)

people = lesson_requests.get('http://api.open-notify.org/astros.json')
print(people.text)