'''#########################
functools.wraps, inspect.unwrap
#########################'''
#
#
#

'''#########################
DECORATORS
#########################'''
''' 2 ways of usage '''
# def my_shiny_new_decorator(a_function_to_decorate):
#     def the_wrapper_around_the_original_function():
#         print("Before the function runs")
#         to_return = a_function_to_decorate()
#         print("After the function runs")
#         return to_return
#     return the_wrapper_around_the_original_function
#
#
# def original_v1():
#     print("I am a stand alone function, don't you dare modify me")
#
# decorated_COPY_of_v1 = my_shiny_new_decorator(original_v1)
#
# @my_shiny_new_decorator
# def original_v2():
#     print("I am a stand alone function, don't you dare modify me")
#
#
# original_v1()
# print("\n")
# decorated_COPY_of_v1()
# print("\n")
# original_v2()


''' instance methods'''
# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self, arg_alias):
#         print("Additional feature")
#         method_to_decorate(self, arg_alias)
#     return wrapper
#
#
# class SomeClass():
#     def __init__(self):
#         self.attr = 1
#
#     @method_friendly_decorator
#     def some_method(self, arg_):
#         print(self.attr, arg_)
#
# some_obj = SomeClass()
# some_obj.some_method(2)

''' arguments - THE ONLY WAY'''
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


''' @decorator(arg_)'''
''' 
sens _>                                                             Zalozmy, ze chcemy, aby to, jak dekorator udekoruje 
                                                                    od czegos zalezalo, ale nie wiemy ile to bedzie 
                                                                    wynosic, bo np. musi sie wpierw gdzies policzyc. 
                                                                    Jak przekazac to do dekoratora, skoro on MUSI MIEC 
                                                                    TYLKO JEDEN ARGUMENT (FUNKCJE)?
'''
# CALCULATED_VALUE = 3 #from import
#
# def decorator_maker_with_arguments(important_arg):
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


'''######################
USEFUL DECORATORS
######################'''
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


'''######################
PROPERTIES
######################'''
'''
dekor 'property' - co bierze, co zwraca ? ->                                                 metode(getter) -> property
dekor 'pos.setter', itp - co biora, co zwracaja? ->                                         property->property
'''
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
#
# some_obj.pos = 5
# print(some_obj.stupid_arg.hiddenArgument, some_obj.pos)

