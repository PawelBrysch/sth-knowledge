import re

list_of_strings = []
list_of_strings.append("_MetaData_elo.txt")
list_of_strings.append("_MetaData_elo.txXt")
list_of_strings.append("_MetaData_elo.tt")
list_of_strings.append("_MetaDxata_elo.txt")
list_of_strings.append("_MetaData_elo.txt _MetaData_elo.txt")
list_of_strings.append("_MetaData_elo.txt, _MetaData_elo.txt")
list_of_strings.append("_MetaData_elo.txt \n _MetaData_elo.txt")

for elem in list_of_strings:
    print elem, " ", re.findall("_MetaData_(.*).txt", elem)