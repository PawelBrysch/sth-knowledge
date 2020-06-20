import json
import itertools

W_LIMIT = 29.0

def total_feature(elem, feature):
    return sum([subelem[feature] for subelem in elem])

def my_measure(elem):
    return total_feature(elem, "slashdef") + total_feature(elem, "firedef")

with open(rf"C:\Users\Lenovo\Desktop\PROJECTS\django_top2\sth-knowledge\source\proj_armors\armors.json") as infile:
    json_ = json.load(infile)


helms = json_["helms"]
leggings = json_["leggings"]
chests = json_["chests"]
gauntlets = json_["gauntlets"]

exl_leggings = ['black_leggings-icon.png']
leggings = list(filter(
    lambda x: x["image"] not in exl_leggings,
    leggings
))

a = [helms, leggings, chests, gauntlets]
combinations = list(itertools.product(*a))

filtered_combinations = list(filter(
    lambda x: total_feature(x, "weight") <= W_LIMIT,
    combinations
))

res = max(filtered_combinations, key=lambda x: my_measure(x))
# total_feature(res, "weight")