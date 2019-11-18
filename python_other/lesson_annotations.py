'''#################
Minimum po argumencie
#################'''
# class czlowiek:
#     def __init__(self, leng):
#         self.dlugosc_penisa  = leng
#
#
# adam = czlowiek(12)
# bartek = czlowiek(10)
# cezek = czlowiek(14)
#
#
# min_ = min([adam, bartek, cezek], key=lambda x: x.dlugosc_penisa)
#
# print(min_.dlugosc_penisa)


'''#################
Annotations
#################'''
'''
po co one sa?->                                                                       by podswietlac podczas CompileTime
jak sprawdzamy, czy wszystko dziala?->                                                    mypy (nakladka na interpreter)
czy reczna zmiana __annotations__ dziala?->                                                                          NIE
'''

# #TODO 1 - po co jest reczna zmiana __annotations__
# import random
#
# alis = ["0", 0, None]
# blis = ["0", "1", "2"]
#
# def print_str(arg:'str'):
#     print(arg)
#
# class SomeClass:
#     some_arg1: 'str' = "s7"
#     some_arg2: 'int' = 7
#
#     some_arg3 = blis[random.randint(0, 2)]
#     # __annotations__["some_arg3"] = "int"
#
#
# SomeClass.__annotations__["some_arg3"] = "int"
# print(SomeClass.__annotations__)
#
# print_str(SomeClass.some_arg1)
# # print_str(SomeClass.some_arg2)
# print_str(SomeClass.some_arg3)


'''#################
PEP8
#################'''
'''
jak piszemy nazwe modulu?->                                                                              ciag lowercasow
chcemy po prostu wyjsc z funkcji->                                                                           return None
czego nie robic w try?->                                                                              returnowac od razu
'''
''' mnozenie '''
# x = x*2 - 1
# c = (a+b) * (a-b)

''' annotations '''
# def munge(input: 'str', sep: 'str' = None, limit=1000) -> 'str':
#     return "sth"

''' underscores '''
# list_ = []
# _private_method = len

