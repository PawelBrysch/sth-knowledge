"""###################################################
        _____ _______ ______
 |        |   |______    |
 |_____ __|__ ______|    |
###################################################"""
''' enumerate zamiast range()'''
# alist = ['her', 'name', 'is', 'rio']
# for index, value in enumerate(alist):
#     print(index, value)

''' Slicing'''
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



"""###################################################
 ______  _____ _______ _______
 |    \\   |   |          |   
 |_____/ __|__ |_____     |   
###################################################"""
''' list of tuples jako rozbudowany slownik'''
# tuple1 = ("pawel",25,"M")
# tuple2 = ("maks", 22, "K")
#
# list_of_tuples = [tuple1, tuple2]
#
# for name, age, gender in list_of_tuples:
#     print(name, age, gender)

'''comprehension'''
# a = {n: n**2 for n in range(5)}
# #NIE!:
# a = dict(n: n**2 for n in range(5))

'''#############################'''
''' kolejny sposob dodanie do slownika'''
'''#############################'''
# adict = {"ala":4, "ma":5, "kota":6}
# bdict = {"szla":7, "baba":8, "po":9, "lodzie":10}
# adict.update(bdict)
# print(adict)


"""###################################################
 ______  _______  _____  _     _ _______
 |    \\ |______ |   __| |     | |______
 |_____/ |______ |___\\| |_____| |______ 
###################################################"""
# from collections import deque
#
# a = deque([4,5,6])
#
# a.popleft()
# a.append(7)
#
# print(a)
# if a:
#     print("puste")
#
# a.popleft()
# a.popleft()
# a.popleft()
#
# if a:
#     print("puste2")
#
#
# stack = [4,5,6]
# stack.pop()
# stack.append(7)
# print(stack)