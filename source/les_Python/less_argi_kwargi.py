'''#########################
CASE 1. Assigment
#########################'''
'''
dziala gdy za duzo refek? ->                                                                                         NIE
dziala gdy za malo refek? ->                                                                                         NIE
lista tez?->                                                                                                         TAK
czy `_` ma jakies specjalne wlasciwosci? ->                                                                          NIE
'''
# *a, b = (1,2,3,4,5)
# print(a, b) ##->                                                                                        [1, 2, 3, 4] 5

# a, *b = (1,2,3,4,5)
# print(a, b) ##->                                                                                        1 [2, 3, 4, 5]

# a, *b, c = (1,2,3,4,5)
# print(a,b,c) ##->                                                                                          1 [2,3,4] 5

''' underscore'''
# _, *_, _ = [1,2,3,4,5]
# print(_) ##->                                                                                                  [3,4,5]

# _, _, *_ = [1,2,3,4,5]
# print(_) ##->                                                                                                        5


'''#########################
CASE 2. Call <args & kwargs>
#########################'''
'''Dict unpacking'''
# def func_(arg1, arg2):
#     print(arg1+arg2)
#
# dict1 = {"arg1":2, "arg2":3}
# func_(**dict1)

''' Tuple unpacking'''
# def pretty_func(arg1, arg2, *rest_of_args):
#     list_or_args = [arg1, arg2, *rest_of_args]
#     print(list_or_args)
#
# showcase = ("Pawel", "Brysch", 11, 11, 1994)
# pretty_func(*showcase)

''' Body - of function, inside'''
# def func(a,b,c, *args, **kwargs):
#     just_classic_tuple = args
#     just_classic_dict = kwargs
#
#     for arg in just_classic_tuple:
#         print("another arg:", arg)
#
#     for key, value in just_classic_dict.items():
#         print("another keyword arg: {0}: {1}".format(key, value))
#
# func(1,2,3,4,e=5)

''' Errors - calls'''
# def func(a,b,c, *args):
#     print(a,b,c)
#
#     for arg in args:
#         print("another arg:", arg)
#
# func(1,2,3,4,e=5)
# # #->brak kwargsow
#
# func(1,2,3,4,b=5)
# # #->"b" juz byl
#
# func(b=1,2,3,4,5)
# # #->po slownikowych nie mozna juz zwyklych

''' MIXED - dict unpacks onto 1) normal arguments, 2) **kwargs'''
# def pretty_func(name, surname, **scam):
#     print(name, surname)
#     print("and scam")
#
#     for elem in scam.values():
#         print(elem)
#
# showcase = {"name":"Pawel", "surname":"Brysch", "scam1":11, "scam2":12, "scam3":13}
# pretty_func(**showcase)
# # #->OK
"""---# additionaly, the order is mixed"""
# showcase = {"name":"Pawel", "scam1":11, "scam2":12, "surname":"Brysch", "scam3":13}
# pretty_func(**showcase)
# # #->OK (o dziwo)
# nowe repo tym razem po ssh

