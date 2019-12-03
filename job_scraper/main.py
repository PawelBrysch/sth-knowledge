import requests
from bs4 import BeautifulSoup
import io
import json
from random import randint
from time import sleep




'''help'''
# pracuj_main = "https://www.pracuj.pl/praca/python;kw"
# source_code = requests.get(pracuj_main)
# soup = BeautifulSoup(source_code.text, "html.parser")
# offer_class = "offer-details__title-link"
# list_of_links = soup.find_all("a", {"class": offer_class})
# list_of_jsons = soup.find_all("script", {"type": "application/ld+json"})


def get_size_of_script(script):
    try:
        result = len(script.contents[0])
    except:
        result = 0
    return result


def get_json_from_url(url_):
    source_code =  requests.get(url_)
    soup = BeautifulSoup(source_code.text, "html.parser")
    scripts = soup.find_all("script")
    wanted_script = max(scripts, key=get_size_of_script)
    script_as_string = wanted_script.contents[0]
    left_idx = script_as_string.find("{")
    right_idx = script_as_string.rfind("}")
    json_as_string = script_as_string[left_idx:right_idx + 1]
    json_ = json.loads(json_as_string)
    return json_


def get_offers_from_pracujpl(list_of_urls):
    offers = []
    for url_ in list_of_urls:
        json_ = get_json_from_url(url_)
        list_of_dicts = json_["offers"]
        offers += list_of_dicts
        sleep(randint(10, 30))
    return offers


list_of_urls = [
    "https://www.pracuj.pl/praca/python;kw",
    "https://www.pracuj.pl/praca/python;kw?pn=2",
    "https://www.pracuj.pl/praca/python;kw?pn=3",
    "https://www.pracuj.pl/praca/python;kw?pn=4",
    "https://www.pracuj.pl/praca/python;kw?pn=5",
    "https://www.pracuj.pl/praca/python;kw?pn=6",
    "https://www.pracuj.pl/praca/python;kw?pn=7",
    "https://www.pracuj.pl/praca/python;kw?pn=8"]


# offers = get_offers_from_pracujpl(list_of_urls)
# with open("z_pracujpl.txt", "w") as file_:
#     json.dump({"offers": offers}, file_)
with open("z_pracujpl.txt", "r") as file_:
    copy = json.load(file_)



