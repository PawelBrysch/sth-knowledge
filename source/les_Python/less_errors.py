
''' if error inside except'''
# def func(a):
#     try:
#         a[2]
#     except TypeError:
#         a.items()
#     finally:
#         print("back at home :)")
#
# bb = 2
# print("func, ", func(bb))


''' wheter "try" or "except" ''' #TODO look close at the "moment"
# def func(a):
#     try:
#         a[2]
#         print("momemet1")
#         return("git")
#     except TypeError:
#         print("momemet2")
#         return("t_error")
#     finally:
#         print("back at home :)")
#
# aa=[1,2,3]
# print("func, ", func(aa))
#
# print(" ")
#
# bb = 2
# print("func, ", func(bb))

''' wheter "try" or "except" ''' #TODO wersion without returns (obvious)
# def func(a):
#     try:
#         a[2]
#         print("momemet1")
#     except TypeError:
#         print("momemet2")
#     finally:
#         print("back at home :)")
#
# aa=[1,2,3]
# func(aa)
#
# print(" ")
#
# bb = 2
# func(bb)


''' when other error (that error also could be at outer region of code (eq. in some function)'''
# def func(a):
#     try:
#         a[2]
#         a.items()
#         return("git")
#     except TypeError:
#         return("t_error")
#
#     finally:
#         print("back at home :)")
#
# aa=[1,2,3]
# print("func, ", func(aa))


''' right exception in outer code'''
# def raise_exeptron(arg):
#     arg[2]
#
# def func(a):
#     try:
#         raise_exeptron(a)
#         return("git")
#     except TypeError:
#         return("t_error")
#     finally:
#         print("back at home :)")
#
# aa=[1,2,3]
# print("func, ", func(aa))
#
# print(" ")
#
# bb = 2
# print("func, ", func(bb))

''' czy try sie naprawde wykonuje?'''
# a=2
# number = 7
#
# try:
#     number += 1
#     b=a[2]
# except:
#     pass
#
# print(number)
# # #->8

''' czy zrobia sie wszystkie wyjatki, czy tylko pierwszy'''
# a=2
# b=3
#
# try:
#     c = a[2]
#     print("przeszedlem")
#     d = b.method()
# except TypeError as e:
#     print("t",e)
# except AttributeError as e:
#     print("a", e)
# #->8

''' raise exception'''
# import sys
#
# def linux_interaction():
#     if not 'linux' in sys.platform:
#         raise Exception("Function can only run on Linux systems.")
#     print('Doing something.')
#
#
# try:
#     linux_interaction()
# except Exception:
#     print('Linux function was not executed')


''' using "assert" '''
# import sys
#
# def linux_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     print('Doing something.')
#
# try:
#     linux_interaction()
# except AssertionError as error:
#     print(error)
#     print('The linux_interaction() function was not executed')

''' kiedy ponizszy jest OK?'''
# import logging
#
# def get_number():
#     return int('foo')
#
# try:
#     x = get_number()
# except Exception as ex:
#     logging.exception('Caught an error')
# #-> gdy jest to np. glowna petla systemu

'''
Exception-kiedy?
1.                                                  gdy uzywamy raise. TYLKO dla bledow, ktore sami CELOWO chcemy wywolac
Raise- kiedy?
1.                                                                                                      wraz z Exception
2.                                                                                                              reraise
Assert-kiedy?
1.                                                                                                      do debugowania


czy assert da sie zastapic raise?                                                          TAK( raise AssertionError (w ifie))
czy Excepion mozna zastapic konkretnym errorem?                                                                     mozna
czy mozna dodac wiadomosc do exception w momecie uzycia raise?                          Mozna, tak ja kdo innych errorow
jaka jest przewaga assert?                                                                          krotszy do napisania
czy "except Exception:"jest spoko?                                                          nie, tak samo jako "except:"
'''
#TODO to jak wyłapywac własne exception, skor onie moze my pisac "except Exception" ?





















