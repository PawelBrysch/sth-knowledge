# TODO MY! czesc mockowanej funkcji ma sie zadziac

# TODO patch decorator na testcasie

# TODO zamiana na classmethods i staticmethods
# TODO wszystko w jednej lokacji
# TODO "import" zamiast "from import"

'''
1. czy //patch(class) as mock// mockuje zupelnie wszystko?->                                                         TAK
'''


from LESSON_pytest.lesson_mock_pt2.tested_class import TestedClass

from unittest.mock import patch

def replaced_own_method(self):
    print("Executed 1/6")
    return "1 good"

def replaced_foreign_method(self):
    print("Executed 3/6")
    return "4 good"

def replaced_function():
    print("Executed 5/6")
    return "7 good"



with patch("LESSON_pytest.lesson_mock_pt2.tested_class.TestedClass.own_method_to_replace", new=replaced_own_method), \
     patch("LESSON_pytest.lesson_mock_pt2.tested_class.TestedClass.own_method_to_tmock", return_value="2 good"), \
     patch("LESSON_pytest.lesson_mock_pt2.tested_class.UsedClass.foreign_method_to_replace", new=replaced_foreign_method), \
     patch("LESSON_pytest.lesson_mock_pt2.tested_class.UsedClass.foreign_method_to_tmock", return_value="5 good"), \
     patch("LESSON_pytest.lesson_mock_pt2.tested_class.function_to_replace", new=replaced_function), \
     patch("LESSON_pytest.lesson_mock_pt2.tested_class.function_to_tmock", return_value="8 good"):

    pass
    # obj = TestedClass()
    # print(obj.tested_method())


# obj = TestedClass()
# print(obj.tested_method())


'''
1. Jaka jest roznica generalnie?                                                      dziala tylko replace (stad lambdy)
'''
@patch("LESSON_pytest.lesson_mock_pt2.tested_class.TestedClass.own_method_to_replace", new=replaced_own_method)
@patch("LESSON_pytest.lesson_mock_pt2.tested_class.TestedClass.own_method_to_tmock", new=lambda self: "2 good")
@patch("LESSON_pytest.lesson_mock_pt2.tested_class.UsedClass.foreign_method_to_replace", new=replaced_foreign_method)
@patch("LESSON_pytest.lesson_mock_pt2.tested_class.UsedClass.foreign_method_to_tmock", new=lambda self: "5 good")
@patch("LESSON_pytest.lesson_mock_pt2.tested_class.function_to_replace", new=replaced_function)
@patch("LESSON_pytest.lesson_mock_pt2.tested_class.function_to_tmock", new=lambda: "8 good")
def test():
    obj = TestedClass()
    res = obj.tested_method()
    assert res == ['1 good', '2 good', '3 good', '4 good', '5 good', '6 good', '7 good', '8 good', '9 good']

test()