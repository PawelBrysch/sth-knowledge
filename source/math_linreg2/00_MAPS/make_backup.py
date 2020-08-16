

# drawio -x -u -f xml -o backup/map.xml map.drawio

# from lxml import etree
#
from bs4 import BeautifulSoup
import re

path_ = "/home/devoted/PROJECTS/sth_knowledge_top/sth-knowledge/source/math_linreg2/00_MAPS/backup/map.xml"

# long
with open(path_, "r") as file_:
    text = file_.read()
# root = etree.XML(text)
# tree = etree.ElementTree(root)

soup = BeautifulSoup(text, 'xml')


'mxCell', 'style'
'UserObject', 'label'

from_images = [elem['style'] for elem in soup.find_all('mxCell', style=lambda x: x and 'snipboard' in x)]

# TODO dyskusja na 4programmers
from_images2 = [
    list(filter(
        lambda x: 'snipboard' in x,
        elem.split(';'))
    )[0][6:] for elem in from_images
]

# TODO tym bedzie najelegenaciej
from urlextract import URLExtract
extr = URLExtract()
extr.find_urls(from_links[2])

from_links = [elem['label'] for elem in soup.find_all('UserObject', label=lambda x: x and 'snipboard' in x)]
from_links2 = [BeautifulSoup(elem, 'xml').find('a')['href'] for elem in from_links]


parsed_attrs = from_links + from_images

elo = parsed_attrs[3]

# res1 = soup.find_all('mxCell', style=lambda x: x and 'snipboard' in x)
# res2 = soup.find_all('UserObject', label=lambda x: x and 'snipboard' in x)