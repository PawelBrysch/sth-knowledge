import re

# string = "pawel jeden dwa trzy cztery brysch pawel piec szesc brysch pawel siedem brysch osiem  dziewiec"
#
# match = re.findall(r"pawel(?:\s+[^\s]+){,2}[\s]+brysch", string)


import re

words = [ ['a', 'the', 'one'], ['reason', 'reasons'], ['for', 'of'] ]

words = ['|'.join(x) for x in words]

a=2

pattern = r'({})[\s]+({})[\s]+({})'.format(*words)
# pattern = r'\b ({}) \s+ ({}) \s+ ({})'.format(*words)

string = "a reason to the reason of a reasons for"

# pattern = re.compile(pattern, re.X)

match = re.findall(pattern, string)

