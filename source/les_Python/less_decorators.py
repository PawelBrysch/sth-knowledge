
''' simplyest decorator'''
# def shout(word="yes"):
#     return word.capitalize()+"!"
#
# scream = shout
#
# def doSomethingBefore(func):
#     print("I do something before then I call the function you gave me")
#     print(func())
#
# doSomethingBefore(scream)
# #-> ???

'''########'''
''' next'''
'''########'''
def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Before the function runs")
        a_function_to_decorate()
        print("After the function runs")
    return the_wrapper_around_the_original_function

''' @(-), lose(+/-)'''
# def a_stand_alone_function():
#     print("I am a stand alone function, don't you dare modify me")
#
# # #BEFORE
# a_stand_alone_function()
#
# # #AFTER 1
# a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
# a_stand_alone_function()


'''@(+), lose(+)'''
# @my_shiny_new_decorator
# def a_stand_alone_function():
#     print("I am a stand alone function, don't you dare modify me")
#
# a_stand_alone_function()

'''@(+), lose(-)'''
# def a_stand_alone_function():
#     print("I am a stand alone function, don't you dare modify me")
#
# @my_shiny_new_decorator
# def a_stand_alone_function_decorated():
#     return a_stand_alone_function()
#
# a_stand_alone_function_decorated()


'''########'''
''' additional arguments'''
'''########'''
# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(number):
#         for i in range(number):
#             function_to_decorate()
#     return a_wrapper_accepting_arguments
#
#
# @a_decorator_passing_arguments
# def print_soup():
#     print("soup")
#
#
# print_soup(10)


'''########'''
''' methods -> 'self' is important(2 places -> wrapper defition and when method is used inside wrapper)'''
'''########'''
# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self, lie):
#         lie = lie - 3
#         method_to_decorate(self, lie)
#     return wrapper
#
#
# class Lucy(object):
#
#     def __init__(self):
#         self.age = 32
#
#     @method_friendly_decorator
#     def sayYourAge(self, lie):
#         print("I am {0}, what did you think?".format(self.age + lie))
#
# l = Lucy()
# l.sayYourAge(0)

'''########'''
''' arguments-blind, function_or_method-blind decorator'''
'''########'''
# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
#         print("Do sth")
#         function_to_decorate(*args, **kwargs)
#     return a_wrapper_accepting_arbitrary_arguments
#
# @a_decorator_passing_arbitrary_arguments
# def some_func(a, b):
#     print(a, b)
#
#
# some_func(2, 3)
#
# class SomeClass:
#     def __init__(self):
#         self.some_str = "some_str"
#
#     @a_decorator_passing_arbitrary_arguments
#     def some_method(self, c, d, e):
#         print(self.some_str, c, d, e)
#
#
# some_object = SomeClass()
# some_object.some_method(4, 5, 6)


'''########'''
''' passing external arguments into decorator'''
'''########'''
''' Zalozmy, ze chcemy, aby to, jak dekorator udekoruje od czegos zalezalo, ale nie wiemy ile to bedzie wynosic, bo np.
musi sie wpierw gdzies policzyc. Jak przekazac to do dekoratora, skoro on 
MUSI MIEC TYLKO JEDEN ARGUMENT (FUNKCJE)
'''
# CALCULATED_VALUE = 3 #from import
#
# def decorator_maker_with_arguments(important_arg):
#
#     def my_decorator(func):
#         def wrapped():
#             print("Wazny argument wynosi:", important_arg)
#             func()
#
#         return wrapped
#
#     return my_decorator
#
# @decorator_maker_with_arguments(CALCULATED_VALUE)
# def decorated_function_with_arguments():
#     print("I am the decorated function")
#
# decorated_function_with_arguments()

'''########'''
''' jak owracpowac, gdy funkcja ma miec return?'''
'''########'''
# def my_shiny_new_decorator(a_function_to_decorate):
#     def the_wrapper_around_the_original_function():
#         print("Before the function runs")
#         res = a_function_to_decorate()
#         print("After the function runs")
#         return res
#     return the_wrapper_around_the_original_function
#
#
# @my_shiny_new_decorator
# def a_stand_alone_function():
#     return "elo"
#
#
# print(a_stand_alone_function())

'''########'''
''' useful decorators'''
'''########'''
# def benchmark(func):
#     """
#     A decorator that prints the time a function takes
#     to execute.
#     """
#     import time
#     def wrapper(*args, **kwargs):
#         t = time.clock()
#         res = func(*args, **kwargs)
#         print("B {0} {1}".format(func.__name__, time.clock()-t))
#         return res
#     return wrapper
#
#
# def logging(func):
#     """
#     A decorator that logs the activity of the script.
#     (it actually just prints it, but it could be logging!)
#     """
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print("L {0} {1} {2}".format(func.__name__, args, kwargs))
#         return res
#     return wrapper
#
#
# def counter(func):
#     """
#     A decorator that counts and prints the number of times a function has been executed
#     """
#
#
#     def wrapper(*args, **kwargs):
#         wrapper.count = wrapper.count + 1
#         res = func(*args, **kwargs)
#         print("C {0} has been used: {1}x".format(func.__name__, wrapper.count))
#         return res
#     wrapper.count = 0
#     return wrapper
#
# @benchmark
# @logging
# @counter
# def reverse_string(string):
#     return str(reversed(string))
#
# print("R", reverse_string("Able was I ere I saw Elba"))


'''########'''
''' property'''
'''########'''
# class MiniClass:
#     def __init__(self):
#         self.hiddenArgument = 3
#
#
# class SomeClass:
#     def __init__(self):
#         self.stupid_arg = MiniClass()
#
#     @property
#     def pos(self):
#         return self.stupid_arg.hiddenArgument
#
#     @pos.setter
#     def pos(self, value):
#         self.stupid_arg.hiddenArgument = value
#
#     # @pos.getter
#     # def pos(self):
#     #     return self.stupid_arg.hiddenArgument
#
# some_obj = SomeClass()
#
# print(some_obj.stupid_arg.hiddenArgument)
# some_obj.pos = 5
#
# print(some_obj.stupid_arg.hiddenArgument)
# print(some_obj.pos)
'''
dekor 'property' - co bierze, co zwraca ? ->                                                 metode(getter) -> property
dekor 'pos.setter', itp - co biora, co zwracaja? ->                                         property->property
'''

