'''##########################
Wyslanie parametru
##########################'''
import requests
parameter = {"rel_rhy":"jingle"}
request = requests.get('https://api.datamuse.com/words', parameter)

people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)