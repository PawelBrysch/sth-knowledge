"""#####################
GENERAL
#####################"""
'''
czy musza byc naraz `metaclass` i `abstracmethod`->                                                                  TAK
'''
# from abc import abstractmethod, ABCMeta
#
# class Animal(metaclass=ABCMeta):
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Cat(Animal):
#     def wash_hair(self):
#         pass
#
# try:
#     animal = Animal()
# except TypeError:
#     print("Nie utworzymy klasy, bo w koncu wirtualna.")
#
# try:
#     cat = Cat()
# except TypeError:
#     print("Kot jest xle zdefiniowany, wiec nawet NIE UTWORZYMY!!!")

