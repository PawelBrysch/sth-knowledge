"""#################################
LVL 0
#################################"""
''' another error without `except`'''
# def func(a):
#     try:
#         a[2]
#         a.items()
#         return("True")
#     except TypeError:
#         return("False")
#
# iterable_=[1,2,3]
# print("func, ", func(iterable_))

''' if error inside `except`'''
# def func(a):
#     try:
#         a[2]
#     except TypeError:
#         a.items()
#     finally:
#         print("back at home :)")
#
# bb = 2
# print("func, ", func(bb))


''' czy `try` leci do konca'''
# def func(a):
#     try:
#         a[2]
#         return("True")
#     except TypeError:
#         return("False")
#     finally:
#         print("END")
#
# iterable_=[1,2,3]
# print(func(iterable_))
#
# print("\n")
#
# not_iterable = 2
# print(func(not_iterable))


''' czy `try` cofa to, do czego doszlo?'''
# a = 2
# number = 7
#
# try:
#     number += 1
#     b=a[2]
# except:
#     pass
#
# print(number)
# # #->8

"""#################################
LVL 1
#################################"""
''' exception in outer context'''
# def method_that_will_rise_exception(arg_):
#     arg_[2]
#
# def func(a):
#     try:
#         method_that_will_rise_exception(a)
#     except TypeError:
#         return("ERROR")
#
# aa=[1,2,3]
# print(func(aa))
#
# print("\n")
#
# bb = 2
# print(func(bb))

"""#################################
'''Exception'''
#################################"""
#TODO 1 w sumie po co takie "czyste" exception
#TODO 2 czy except Expcetion wylapie konkretne errory? (moze to odp. na TODO 1)
# def method_that_raise_exception():
#     raise Exception("Exception label")
#
# try:
#     method_that_raise_exception()
# except Exception:
#     print('handled!')

"""#################################
assert
#################################"""
'''
czy assert da sie zastapic raise? ->                                                 TAK( raise AssertionError (w ifie))
jaka jest przewaga assert? ->                                                                       krotszy do napisania
'''
# assert 2 == 2
# assert 2 == 3

