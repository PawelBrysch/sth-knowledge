"""###########################
Find n'th occurence.
###########################"""
import re
pattern = re.compile(r"sth")
second_occurence = re.search(pattern, "source").group(2)
