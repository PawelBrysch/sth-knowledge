'''
brak __iter__() -> nie zrobi sie for, bo obiekt nie jest iterable
brak __next__() -> nie zrobi sie for, iter nie zwrocil iteratora. Zwraca sam siebie, wiec wniosek z tego taki, ze
                   stajemy sie iteratorem dopiero, gdy mamy funkcje next

mamy obydwa -> next() zadziala, ale pewnie zle, bo potrzebuje, by itera przedtem wlaczyc (ale tylko do ustawienia warunkow
               poczatkowych petli
'''
# class vector:
#     def __init__(self, xx, yy):
#         self.x = xx
#         self.y = yy
#
#
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
# vec1 = vector(4,7)
#
# for elem in vec1:
#     print("wypisuje", elem)
#
# print(" ")
#
# vec1.__iter__()
# print(next(vec1))
# print(next(vec1))

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