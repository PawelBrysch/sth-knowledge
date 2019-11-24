






'''###################
Basic usage
###################'''
# TODO czy patch object po prostu ma byc robione na konkretnym obiekcie (tak, że reszta klasy jest ok)?
# TODO upewnic sie, czy builtin, albo package z globala moze byc robiony w tak prosty sposob (tj. bez calej sciezki)
# from unittest.mock import patch
# import os
#
#
# class AnotherClass:
#     @classmethod
#     def do_what_i_dont_want(self):
#         print("BAD. Some CUSTOM method is working now.")
#         return "BAD result from CUSTOM method"
#
#
# class MyClass:
#     def method_from_api(self):
#         print("GOOD. The method I'm testing")
#         result = AnotherClass.do_what_i_dont_want()
#         print(result)
#         if os.getcwd() is not None:
#             print("BAD. Some BUILTIN method is working now.")
#
#
# print("with patch:")
# with patch.object(AnotherClass, 'do_what_i_dont_want', return_value="GOOD result from the mock"), \
#      patch.object(os, 'getcwd', return_value=None) as some_alias:
#         my_obj = MyClass()
#         my_obj.method_from_api()
#
#
# print("\n" + "w/o patch:")
# my_obj = MyClass()
# my_obj.method_from_api()


'''###################
patch.object() vs patch()
###################'''
'''
patch:  pros-> 1) nie trzeba importowac
        
o czym nalezy pamietac? 1)                                  aby patch zadzialam w tym samym module musimy dodac __main__
                        2)                                                       sciezka importowania musi byc ABSOLUTNA
'''
# patch.object(AnotherClass, 'do_what_i_dont_want', return_value="GOOD result from the mock")
# patch("LESSON_pytest.lesson_mock.lesson_mock_module.AnotherClass.do_what_i_dont_want", return_value="GOOD result from the mock")


'''###################
patch(Class)
###################'''
'''
w jakim stopniu "zmockowana jest taka klasa? ->                                                         CHYBA calkowicie
to dobrze?->                                                                                                   chyba nie

"patchujemy" location_two, mimo iż klasa jest zaimplementowana w location_one \
            dlaczego?->                                                                                           bo tak
            czy ta zasada dziala zawsze?            NIE. Jesli w skrypcie z metoda jest "import module" zamiast "from \
                                                    module import sth" to robimy normalnie. Wytlumaczone tutaj:
                                                    https://docs.python.org/3/library/unittest.mock.html#where-to-patch
'''
# from unittest.mock import patch
# from LESSON_pytest.lesson_mock.location_two import some_function
#
#
# with patch('LESSON_pytest.lesson_mock.location_two.Foo') as mock:
#     mock.class_attribute = 'mocked             CLASS ATTRIBUTE'
#     mock.class_method.return_value = 'mocked result      CLASS METHOD'
#     mock.return_value.instance_attribute = 'mocked             INSTANCE ATTRIBUTE'
#     mock.return_value.instance_method.return_value = 'mocked result      INSTANCE METHOD'
#
#     print("with patch:")
#     some_function()
#
#
# print("\n without patch:")
# some_function()


'''###################
podmiana CALEJ metody, a nie tylko return
###################'''
# from unittest.mock import patch
# from LESSON_pytest.lesson_mock.location_two import some_function_which_only_calls_instance_method
#
# def custom_mocking_method():
#     print("inside CUSTOM mocking method")
#     return "result from CUSTOM mocking METHOD"
#
# with patch('LESSON_pytest.lesson_mock.location_two.Foo') as mock:
#     mock.return_value.instance_method = custom_mocking_method
#
#     print("with patch:")
#     some_function_which_only_calls_instance_method()
#
#
# print("\n without patch:")
# some_function_which_only_calls_instance_method()




