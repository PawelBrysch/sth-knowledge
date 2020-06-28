import re

def get_tasks(string):
    splitted = string.split("name")
    splitted2 = ["name" + elem for elem in splitted]
    res = [re.search(r"name.*creator", elem) for elem in splitted2]
    res2 = [elem.string for elem in res if elem is not None]
    res3 = list(filter(lambda x: "creator" in x, res2))
    return res3

path= rf"C:\Users\devoted_w\Desktop\app.clickup.com.har"
with open(path, "r", encoding="utf8") as infile:
    lines = infile.readlines()

elo = list(filter(lambda x: "twierdzenia" in x, lines))
with_name = list(filter(lambda x: "name" in x, lines))
with_name_and_id = list(filter(lambda x: "id" in x, with_name))
only_long = list(filter(lambda x: len(x) > 130, with_name_and_id))
with_tasks = list(filter(lambda x: "tasks" in x, only_long))
with_ALGEBRA = list(filter(lambda x: "ALGEBRA" in x, with_tasks))


with_covariance = list(filter(lambda x: "Covariance" in x, only_long))
chosen_one = with_covariance[2]
res = get_tasks(chosen_one)
# splitted = chosen_one.split("name")
# splitted2 = ["name" + elem for elem in splitted]
# res = [re.search(r"name.*creator", elem) for elem in splitted2]
# res2 = [elem.string for elem in res if elem is not None]
# res3 = list(filter(lambda x: "creator" in x, res2))

res2 = [get_tasks(elem) for elem in with_ALGEBRA]
res3 = [get_tasks(elem) for elem in with_tasks]