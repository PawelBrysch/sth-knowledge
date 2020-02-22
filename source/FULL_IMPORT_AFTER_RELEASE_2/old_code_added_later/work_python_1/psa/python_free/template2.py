'''
TODO:
1. jak to w koncu jest closure z tymi funkcjami?
2. jakeis named tuple factors/indices
'''

import re
# import textract
# import copy
#
# def get_parts(path_):
#     bytetext = textract.process(path_)
#     text = str(bytetext)
#     parts = re.findall(r">[^>]+>", text)
#     return parts


# print(get_parts(rf"C:\Users\Lenovo\Desktop\ENGLISH\writings\writing3.docx"))
# str1 = "Ala ma  kota o matko"
# parts = re.findall(r"Ala[ ]+[\w]+[ ]+kota", str1)

def create_list_of_regexes_with_various_number_of_words_between(pregex):
    pass

def convert_to_regex(number_of_words):
    result = r""
    for i in range(number_of_words):
        result += r"[ ]+[\w]+"
    result += r"[ ]+"
    return result

pregex = "trend (2) on  big (2) increase"
words = pregex.split()

# Find Factors
list_of_factors = []
list_of_indices = []
for index, word in enumerate(words):
    match = re.search(r"\((\w)\)", word)
    if match:
        list_of_factors.append(int(match.group(1)))
        list_of_indices.append(index)

# Add space when necessary
for index, _ in enumerate(words[:-1]):
    if index not in list_of_indices and index+1 not in list_of_indices:
        words[index] += " "

# Create regexes of various length
case = len(list_of_factors)
list_of_regexes = []
for factor1 in range(list_of_factors[0]+1):
    for factor2 in range(list_of_factors[1]+1):
        words[list_of_indices[0]] = convert_to_regex(factor1)
        words[list_of_indices[1]] = convert_to_regex(factor2)
        list_of_regexes.append("".join(words))