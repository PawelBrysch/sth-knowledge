''' enumerate zamiast range()'''
# alist = ['her', 'name', 'is', 'rio']
# for index, value in enumerate(alist):
#     print(index, value)


''' underscore'''
# _,_,*_ = [1,2,3,4,5]
# print(_)
# # #-> [3,4,5]

''' list of tuples jako rozbudowany slownik'''
# tuple1 = ("pawel",25,"M")
# tuple2 = ("maks", 22, "K")
#
# list_of_tuples = [tuple1, tuple2]
#
# for name, age, gender in list_of_tuples:
#     print(name, age, gender)


'''###########################'''
''' Slicing'''
'''###########################'''
# pyString = 'Python'
# sObject = slice(3)
# print(pyString[sObject])
# # #-> Pyt
#
# pyString = '1234567890'
# print(pyString[slice(1,6,3)])
# #-> 25
#
# pyString = 'Python'
# print(pyString[:2])
# #-> Py
#
# pyString = 'Python'
# print(pyString[2:])
# #-> thon
#
# pyString = 'Python'
# print(pyString[::-1])
# #-> nohTYp

'''###########################'''
''' Comprehensions'''
'''###########################'''
# ############INFO!!!############
# genetatora mozna zrobic z comprehensions i wtedy przypomina tupla.
# Tupla nie da sie z comprehensions

# for i in range(3):
#     print(i)
# # #-> 0,1,2
#
# a = {n: n**2 for n in range(5)}
# for elem in a.keys():
#     print(elem)
# for elem in a.values():
#     print(elem)
# for key, value in a.items():
#     print(key, value)


'''###########################'''
''' Unpacking tuple (and list)'''
'''############################'''

''' 2 lub 4 nie zadziala -> 'list' tak samo'''
# my_tuple = ("ala", 1, "kota")
# a, b, c  = my_tuple

''' 'list' tak samo'''
''' *a, b -> analogicznie'''
# my_tuple = ("ala", 1, "kota")
# a, *b  = my_tuple
# print(type(b))
# #-> 'list'

# a, *b, c = (1,2,3,4,5)
# print(a,b,c)
# #-> 1 [2,3,4] 5

'''###########################'''
''' .join()'''
'''###########################'''
# my_list = ["Hello", "world", "elo"]
# print("-".join(my_list) )
#  #-> works
#
# my_list = [2,3,4]
# print("-".join(my_list) )
#  #-> X (expected str, int found)

''' % vs .format()'''
'''###########################'''
# name = [1,2,3]
# print("hi there %s" % name)
# print("hi there {0}".format(name))
# #-> OK

''' 1st advantage'''
# name = (1,2,3)
# print("hi there %s" % name)
# print("hi there {0}".format(name))
# # #-> error

# name = (1,2,3)
# print("hi there %s" % (name,))
# print("hi there {0}".format(name))
# # #-> OK, ale jak to wyglada

''' 2st advantage'''
# tu = (10,11,12,13,14,15,16)
# print('{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu))


''' * how to use format'''
# print("{0} {1} {0} {1} {2}".format("Pawel", "Brysch", "Hurra"))

'''#####################'''
''' break/continue - dzialaja analogicznie, pytanie, na ktora petle'''
'''#####################'''
# for i in range(5):
#     print("gora")
#     if i<10:
#         print("Srodek")
#         if i ==2:
#             continue
#         print("dol")
#     print("sam dol")

'''#################'''
''' exec, eval'''
'''#################'''
# s = "print(\"Hello, World!\")"
#
# print(exec(s))
# print(eval(s))
#
# print("\n")
#
# s = "2+4"
#
# print(exec(s))
# print(eval(s))


'''#############################'''
''' why not my_obj._MyClass__atr'''
'''#############################'''
''' 
to samo ma miejsce w przypadku dokonywania tych assignemtow w ciele klasy (w sensie z uzyciem self.
wniosek->                                                                               self.__class__._MyClass__atr
'''
# class RLCN:
#     static_var = 5
#
#
# rlcn = RLCN()
# print(id(RLCN.static_var), id(rlcn.static_var))
# print(RLCN.static_var, rlcn.static_var)
#
# RLCN.static_var =12
# print(id(RLCN.static_var), id(rlcn.static_var))
# print(RLCN.static_var, rlcn.static_var)
#
# rlcn.static_var =40
# print(id(RLCN.static_var), id(rlcn.static_var))
# print(RLCN.static_var, rlcn.static_var)


'''#############################'''
''' ellipsis as a sentinel'''
'''#############################'''

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

'''#############################'''
''' kolejny sposob dodanie do slownika'''
'''#############################'''
# adict = {"ala":4, "ma":5, "kota":6}
# bdict = {"szla":7, "baba":8, "po":9, "lodzie":10}
# adict.update(bdict)
# print(adict)


'''###################'''
''' getatrr###########'''
'''###################'''
'''
co zlego, jesli dodamy getatrrr ->                                              przestanie wyrzucac attribute errory
po co trzeci argument? ->                                          zwraca, co ma byc zwrocone, gdy jest proszone o cos niewlasciweo (w sumie mozna to zrobic na returnie __getattr__, ale wtedy trzeba go pisac)

#IMPORTANT
Zastosowania 
1. wraz ze setatrr mozemy zmienic atrybut na pochodny i zachowac zawartosc
2. mozemy sie bawic na nazwach (dispatcher)

OStatecznie wnioski:
1.  nie ma znaczenia, czy uzywamy kropki, czy setattr/getattr
2. WAZNE jest tylko __geattrr__, gdyz jak nie jest zdefiniowany, to kod się wykrzacza
'''
# class SomeClass:
#     def __init__(self):
#         self.arg1 = 7
#         self.arg2 = 11
#
#
#     def __getattr__(self, name):
#         print("ktos poprosil o argument, ktorego nie ma ")
#         return 200
#
#     def __getattribute__(self, name):
#         print("ktos poprosil o jakikowiek arguemtn")
#         return object.__getattribute__(self, name)
#
#     def __setattr__(self, name, val):
#         print("ustawiamy atrybut")
#         return object.__setattr__(self, name, val)
#
#
# obj = SomeClass()
#
# print(getattr(obj, "arg1"), "\n")
# print(getattr(obj, "arg3"), "\n")
# print(obj.arg1, "\n")
# print(obj.arg3, "\n")
#
# obj.arg1 = 2
# setattr(obj, "arg1", 3)
#
# obj.arg6 = 4
# setattr(obj, "arg7", 5)

