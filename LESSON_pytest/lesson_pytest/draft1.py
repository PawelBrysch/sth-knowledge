'''#########################
    HOW TO USE it?-> pytest -vs draft1.py

    TL:DR
    1. "Fixture" dzialaja jednoczesnie jako "prepare()" i jako "tidy()"
    2. moga miec dowolny "scope" (na 1 test, na wszystkie testy w klasie, na wszystkie testy w module)
    3. sypanie errorow nie robi im żadnego problemu
#########################'''

'''
kiedy fixture byloby mustem?                                               gdyby obowiazywala zasada "1 test - 1 assert"
    dlaczego?->                                                                      bo mozna nia podac liste argumentow
    a jak to zrobic prosciej?->                                                                       mark.parametrize()

zatem, czym ogolnie jest fixture?->                                                                    context managerem
po co je yieldujemy?->                                                                     taki dodatkowy ficzer, a co !
'''

# TODO porownaj: 1) pliki (readlines i bez) 2) JSONy
# TODO tworze plik i odpalam wybrane testy z roznych: 1) klas w tym samym module 2) modulow
# TODO if na test (np wczesniejszy test)

# TODO #future co, gdy fixture sie sypnie (finalizer)
# TODO #wtf  czy mark dziala jak testy sa w klasie


'''########'''
''' Error testing'''
'''########'''
# import pytest
#
# def raise_error():
#     return 1/0
#
# class TestClass(object):
#     def test_div_zero_exception(self):
#         with pytest.raises(ZeroDivisionError) as message:
#             print("\n## Widac")
#             raise_error()
#             print("\n## Nie widac")
#
#         print("## O dziwo message zostal \"wyrzucony\" poza kontekst: \n", message)


'''#########################
Fixture [test level]
#########################'''
# TODO jak zrobic normalne importy?
from pytest import fixture, mark
# from LESSON_pytest.lesson_pytest.external_module import divide

def raise_error():
    return 1/0

class TestClass():
    @fixture
    def fixture_for_one_test(self):
        print("\n## PREPARE")
        yield [1, 2, 3]
        print("\n## TIDY")

    def test_with_fixture_as_argument(self, fixture_for_one_test):
        value_passed = fixture_for_one_test
        print("value_passed: ", value_passed)
        assert True

    @mark.usefixtures("fixture_for_one_test")
    def test_with_fixture_as_decorator(self):
        # raise_error()
        assert True

    def test_without_fixture(self):
        assert True


'''#########################
 Fixture [class level]
#########################'''
'''
jest drugi sposob umieszczenia fixture->          jak metoda klasy, jednak z "@fixture(autouse=True)" zamiast "@fixture"
'''
# from pytest import fixture, mark
#
# def raise_error():
#     return 1/0
#
# @fixture
# def preparing_fixture():
#     print("\n## PREPARE")
#     yield "what to do with that value?"
#     print("\n## TIDY")
#
# @mark.usefixtures("preparing_fixture")
# class TestIntermediateClass(object):
#     def test1(self):
#         print("# test1")
#         assert True
#
#     def test2(self):
#         print("# test2 - with error")
#         # val_ = raise_error()
#         assert True
#
#     def test3(self):
#         print("# test3")
#         assert True


'''########'''
''' Fixture [module level]'''
'''########'''
'''
jak zrobic "wlacznik" dla fixture typu "module"?->                        pytestmark = mark.usefixtures("nazwa_fixtury")
'''
# TODO zbadac uzycie tego wlacznika
# from pytest import fixture
#
# @fixture(scope="module", autouse=True)
# def fixture_raz_na_modul():
#     print("\n## PREPARE - module level")
#     yield "sth"
#     print("\n##TIDY - module level")
#
# def raise_error():
#     return 1/0
#
# class TestClass1(object):
#     def test1_1(self):
#         print("\n## test1.1")
#         assert True
#
#     def test1_2(self):
#         print("\n## test1.2")
#         assert True
#
# class TestClass(object):
#     def test2_1(self):
#         print("\n## test2.1 - with optional error")
#         # raise_error()
#         assert True
#
#     def test2_2(self):
#         print("\n## test2.2")
#         assert True

########################################################################################################################

# if __name__ == '__main__':
#     pytest.main()