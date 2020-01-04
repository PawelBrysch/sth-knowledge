'''#########################
inspect.unwrap
#########################'''
'''
what is important?                                                           the decorator have to use "functools.wraps"
'''
# import time
# from inspect import unwrap
# from functools import wraps
#
# def benchmark(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         t = time.clock()
#         res = func(*args, **kwargs)
#         print("B {0} {1}".format(func.__name__, time.clock()-t))
#         return res
#     return wrapper
#
# @benchmark
# def suma(arg1, arg2):
#     print("Just func")
#     wynik = arg1 + arg2
#     return wynik
#
# print(unwrap(suma)(2, 3))

'''#########################
getattribute
#########################'''
'''
dodatkowe zastosowanie->                            pobranie funkcji z klasy (czyli nie trzeba z obiektu (co oczywiste))
'''


'''#########################
globale dziwnie dzialaja
#########################'''
def verify_function():
    return unwrap_func in ["elo", "siema"]

unwrap_func = "elo"

print(verify_function())



