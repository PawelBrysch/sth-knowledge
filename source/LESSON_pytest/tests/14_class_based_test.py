import unittest
import pytest

class TestSimpleClass(unittest.TestCase):
    """
    Classes can still be used to organize collections of test cases, with
    each test being a Method on the Class, rather than a standalone function.
    """

    x = 1
    y = 2

    def regular_method(self):
        print("\n(This is a regular, non-test-case method.)")

    def test_two_checking_method(self):
        print("\nRunning TestSimpleClass.test_twos_method")
        assert self.x != 3
        assert self.y == 2

    # def test_two_checking_method2(self):
    #     print("\nRunning TestSimpleClass.test_twos_method")
    #     assert self.x != 3
    #     assert self.y == 2



if __name__ == '__main__':
    unittest.main ()