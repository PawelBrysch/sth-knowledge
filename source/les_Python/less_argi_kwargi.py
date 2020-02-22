
''' szybkie triki'''
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

''' ostatni '''
# def func(a,b,c, *args, **kwargs):
#     print(a,b,c)
#
#     for arg in args:
#         print("another arg:", arg)
#
#     for key, value in kwargs.items():
#         print("another keyword arg: {0}: {1}".format(key, value))
#
# func(1,2,3,4,e=5)
# #->ok


''' mixed option - args'''
# def pretty_func(name, surname, *scam):
#     print(name, surname)
#     print("and scam")
#
#     for elem in scam:
#         print(elem)
#
# showcase = ("Pawel", "Brysch", 11, 11, 1994)
#
# pretty_func(*showcase)

''' mixed option - kwargs'''
# def pretty_func(name, surname, **scam):
#     print(name, surname)
#     print("and scam")
#
#     for elem in scam.values():
#         print(elem)
#
# # showcase = {"name":"Pawel", "surname":"Brysch", "scam1":11, "scam2":12, "scam3":13}
# # pretty_func(**showcase)
# # # #->OK
#
# #TODO
# # showcase = {"name":"Pawel", "scam1":11, "scam2":12, "surname":"Brysch", "scam3":13}
# # pretty_func(**showcase)
# # # #->OK (o dziwo)

''' przekmin jeszcze raz, co sie po klei dzieje'''
# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
#         for arg in args:
#             print("another arg:", arg)
#
#         for key, value in kwargs.items():
#             print("another keyword arg: {0}: {1}".format(key, value))
#
#
#         function_to_decorate(*args, **kwargs)
#     return a_wrapper_accepting_arbitrary_arguments
#
#
# class SomeClass:
#     def __init__(self):
#         self.some_str = "some_str"
#
#     @a_decorator_passing_arbitrary_arguments
#     def some_method(self, *args):
#         for arg in args:
#             print("next arg:", arg)
#
#
# some_object = SomeClass()
# some_object.some_method(1,2,3)