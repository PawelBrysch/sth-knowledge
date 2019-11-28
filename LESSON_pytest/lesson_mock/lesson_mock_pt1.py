"""                                                                                                                  """

"""######################
GENERAL
######################"""
'''
patch() -aby patch zadzialam w tym samym module->                                                musimy dodac "__main__"
        -jaka sciezke dac za string?->               https://docs.python.org/3/library/unittest.mock.html#where-to-patch

patch.object() - czy mokuje tylko DANY OBIEKTY, a klasy juz nie?->                                                   NIE

mock_open - w koncu po co?->                        chyba tylko, by nie pisac krotkich pliczkow (dlugie raczej odpadaja)
'''


'''######################
SIDE_EFFECT vs RETURN_VALUE
######################'''
'''
co przeslania->                                                 side_effect przeslania niezaleznie od kolejnosci dodania
czy mozna wstawic jako argument dla patch?->                                                                         TAK
'''


'''######################
MOCK(SPEC = CLASS_OR_FUNC)
######################'''
'''
co nam to daje?->    wywali AttributeError, jak wywolamy atrybut, ktorego nie ma dana klasa (w celu testow regresywnych)
a sprawdza argumenty?->                                                                                              NIE
'''


'''###################
MOCK.RETURN_VALUE - how to use it?
###################'''
'''
czy w ponizszym przykladzie zamiast "class_method.return_value" mozemy podmienic cale "class_method"?->              TAK
'''
# from unittest.mock import patch
# from LESSON_pytest.lesson_mock.location_one import some_function
#
#
# with patch('LESSON_pytest.lesson_mock.location_one.Foo') as mock:
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
PATCH() vs PATCH.OBJEKT()
###################'''
'''
czy jest jakichs sposob na patch(), by jednak nie dawal [mocked, mocked, mocked]?->                          ja nie znam
'''
# +--------+----------------+---------------------------------------+
# | patch  | patch.object() |                                       |
# +--------+----------------+---------------------------------------+
# | mocked | mocked         |  external_method_using_mocked_method  |
# | mocked | mocked         |  internal_method_using_mocked_method  |
# | mocked | mocked         |  using_mocked_method_in_testcase      |
# +--------+----------------+---------------------------------------+

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
# from LESSON_pytest.lesson_mock.location_one import use_os_and_print_getcwd_external
# from unittest.mock import patch
# import os
#
# def use_os_and_print_getcwd_internal():
#     print(os.getcwd())
#
# with patch.object(os, 'getcwd', return_value="mocked_value"):
#     use_os_and_print_getcwd_external()
#     use_os_and_print_getcwd_internal()
#     print(os.getcwd() + "\n")
#
#
# with patch("LESSON_pytest.lesson_mock.location_one.os.getcwd", return_value="mocked_value"):
#     use_os_and_print_getcwd_external()
#     use_os_and_print_getcwd_internal()
#     print(os.getcwd()+"\n")
#
# with patch("os.getcwd", return_value="mocked_value"):
#     use_os_and_print_getcwd_external()
#     use_os_and_print_getcwd_internal()
#     print(os.getcwd()+"\n")
#
# with patch("__main__.os.getcwd", return_value="mocked_value"):
#     use_os_and_print_getcwd_external()
#     use_os_and_print_getcwd_internal()
#     print(os.getcwd()+"\n")
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #








