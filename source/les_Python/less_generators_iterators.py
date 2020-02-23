"""CUSTOM ITERABLES"""
'''
next() vs .__next() ->                                                                                       bez roznicy
'''
# class vector:
#     def __init__(self, xx, yy):
#         self.x = xx
#         self.y = yy
#
#     def __iter__(self):
#         print("iter")
#         self.index = 0
#         return self
#
#     def __next__(self):
#         print("next")
#         if self.index < 2:
#             if self.index == 0:
#                 result = self.x
#             else:
#                 result = self.y
#             self.index += 1
#             return result
#         else:
#             raise StopIteration
#
# obj_ = vector(4,7)
#
# # IMPLICIT
# for elem in obj_:
#     print(elem)
#
# # EXPLICIT
# iterator_ = obj_.__iter__()
# while True:
#     try:
#         next_element = iterator_.__next__()
#         print(next_element)
#     except StopIteration:
#         break


'''
"list" to nie jest "iterator", mimo ze "iterable" , wiec nie mozemy uzyc next()
Ale mamy na to iteratory
'''
# simple_list = [1, 2, 3]
# my_iterator = iter(simple_list)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
#
# for elem in my_iterator:
#     print("elo")



'''przyklady '''
# def createGenerator():
#    mylist = range(3)
#    print("poczatek")
#    for i in mylist:
#        print("petla")
#        yield i*i
#
# # #IMPORTANT ()!
# # mygenerator = createGenerator() # create a generator
# # print(mygenerator) # mygenerator is an object!
# # for i in mygenerator:
# #     print("wypisuje", i)
#
# # print(next(mygenerator))
# # print(next(mygenerator))
# # print(next(mygenerator))


# def mygen():
#     print("POCZATEK")
#     for a in range(3):
#         print("poczetek petli")
#         if True:
#             print("czworka")
#             yield 4
#
#         print("srodek")
#         if True:
#             print("siodemka")
#             yield 7
# My_generator = mygen()
# for i in My_generator:
#     print("wypisuje", i)


'''###########################'''
''' Generators'''
'''###########################'''
# ############INFO!!!############
# genetatora mozna zrobic z comprehensions i wtedy przypomina tupla.
# Tupla nie da sie z comprehensions
