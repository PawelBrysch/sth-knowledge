'''#########################
range
#########################'''
# for i in range(3):
#     print(i)
# # #-> 0,1,2


'''#########################
.format
#########################'''
# print("{0} {1} {0} {1} {2}".format("Pawel", "Brysch", "Hurra"))


'''#########################
.join()
#########################'''
# my_list = ["Hello", "world", "elo"]
# print("-".join(my_list) )
#  #-> works
#
# my_list = [2,3,4]
# print("-".join(my_list) )
#  #-> X (expected str, int found)


'''#########################
ellipsis
#########################'''
''' nothing'''
# def myfunc(value = []):
#
#     value.append(1)
#     return value
#
# print(myfunc())
# print(myfunc())
# print(myfunc())


''' None'''
# def myfunc(value=None):
#     if value is None:
#         value = []
#
#     value.append(1)
#     return value
#
# print(myfunc())
# print(myfunc())
# print(myfunc())


''' None has special purpose -> sentinel use'''
# sentinel = object()
# def myfunc(value=sentinel):
#     if value is sentinel:
#         value = []
#
#     if value is None:
#         value = [6,6,6]
#
#     value.append(1)
#     return value
#
# print(myfunc())
# print(myfunc())
# print(myfunc())
# print(myfunc(None))

''' None has special purpose -> "..." use'''
# def myfunc(value=...):
#     if value is ...:
#         value = []
#
#     if value is None:
#         value = [6,6,6]
#
#     value.append(1)
#     return value
#
# print(myfunc())
# print(myfunc())
# print(myfunc())
# print(myfunc(None))


'''#########################
getattr()
#########################'''
"""1. BRAK ATTRIBUTE ERRORA"""
#
#
#
"""2. UZYCIE METODY NAWET, GDY NIE ISTNIEJE"""
# adict = {"ala":1, "ma":2, "kota":3}
# bdict = 2
#
# print(getattr(adict, "get", lambda arg: None)("ala"))
# print(getattr(bdict, "get", lambda arg: None)("ala"))
"""3. PODMIANA ATRYBUTU NA PODOBNY Z KLASY POCHODNEJ"""
#
#
#


'''#########################
__getattr__, __setattr__, __getattribute__
#########################'''
'''
`obj.attr` vs setattr() & getattr() - jest roznica? ->                                                               NIE
`if str(name) != "__class__":` - ock? ->                                                                        NIE WIEM 
'''
# class SomeClass:
#     def __init__(self):
#         self.arg_that_exists = "some_val"
#
#     def __getattr__(self, name):
#         print("Instead of attribute error")
#         return "Some fancy value"
#
#     def __getattribute__(self, name):
#         if str(name) != "__class__":
#             print("Before getting", name)
#         return object.__getattribute__(self, name)
#
#     def __setattr__(self, name, val):
#         print("Before setting")
#         return object.__setattr__(self, name, val)
#
# print(" A")
# obj = SomeClass()
# print("\n", "B")
# obj.arg_that_exists = "new_val"
# print("\n", "C")
# some_ref1 = obj.arg_that_exists
# print("\n", "D")
# some_ref2 = obj.arg_that_not_exists
# print("\n", "E")
# obj.another_arg_that_not_exists = "some_val"

