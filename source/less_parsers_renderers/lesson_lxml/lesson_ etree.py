# from functools import reduce
#
# print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))

from lxml import etree

'''#########################
SCRATCH -> TREE
#########################'''
# root
root = etree.Element("root5")
# 3 sposoby na dodawanie
root.append( etree.Element("child0") )
child2 = etree.SubElement(root, "child2")
root.insert(1, etree.Element("child1"))




'''#########################
NAVIGATION
#########################'''
child1_ref = root[1]

'''#########################
.. warning::
NEW SYNTAX !!!
#########################'''
'''
ostatni element o dziwo zostanie usuniety (powinien zostac skopiowany i zastapic pierwszy element)
'''
root[0] = root[-1]


'''#########################
PRINT
#########################'''
print(etree.tostring(root, pretty_print=True))


'''#########################
BASIC HTML "features"
#########################'''
child1_ref.tag = "some_tag"
child1_ref.attrib = {"some_attribute_1": 1, "some_attribute_2": 2} #akurat not writable (patrz nizej)
child1_ref.text = "innerHTML"


'''#########################
ATTRIBUTES
#########################'''
'''
czy attrib ma refencje?->                                                                                            TAK
to co robimy?->                                                                                        dict(root.attrib)
'''
dict_ = root.attrib
# +-----------------------------------------------------+----------------------------------------------------------+
# | # root["new_attribute"] = "new_value" #nie zadziala |           dict_["new_attribute"] = "new_value"           |
# +-----------------------------------------------------+----------------------------------------------------------+
# |     root.set("new_attribute", "new_value")          |   # dict_.set("new_attribute", "new_value")#nie zadziala |
# +-----------------------------------------------------+----------------------------------------------------------+
# |            root.get("new_attribute")                |                dict_.get("new_attribute")                |
# +-----------------------------------------------------+----------------------------------------------------------+


'''#########################
Z PLIKU
#########################'''
'''
dlaczego parse jest fajne?->                                                                    bo lyknie kazdy argument
'''
path_ = rf"C:\Users\Lenovo\Desktop\PROJECTS\django_top2\sth-knowledge\lesson_lxml"+"\sample_xml.xml"

# long
with open(path_, "r") as file_:
    text = file_.read()
root = etree.XML(text)
tree = etree.ElementTree(root)

# short
tree = etree.parse(path_)


'''#########################
RECURRENT CREATION
#########################'''
tree = etree.ElementTree(root)
root = tree.getroot()

