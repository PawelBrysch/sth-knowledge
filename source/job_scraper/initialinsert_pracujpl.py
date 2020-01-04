import psycopg2
import json

with open("z_pracujpl.txt", "r") as file_:
    copy = json.load(file_)


class Element:
    def __init__(self, name, url):
        self.name = name
        self.url = url


domain = "https://www.pracuj.pl"
elements = []
for dict_ in copy["offers"]:
    elem = Element(dict_["jobTitle"], domain + dict_["offers"][0]["offerUrl"])
    elements.append(elem)

con = psycopg2.connect(
    # host = ""
    database="first_db",
    user="devoted",
    password="Janina123")
cur = con.cursor()


for elem in elements:
    cur.execute(f"INSERT INTO offers VALUES (DEFAULT, \'{elem.name}\', \'{elem.url}\', \'WAITS_FOR_FILTER\')")
con.commit()


cur.close()
con.close()


with open("outputs\\names", "w") as file_:
    for elem in elements:
        file_.write(elem.name + "\n")