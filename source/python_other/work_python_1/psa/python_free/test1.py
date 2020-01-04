import unittest
from template2 import convert_to_regex


class TestName(unittest.TestCase):

    def test_convert_to_regex(self):
        self.assertEqual(convert_to_regex(0), "[ ]+")
        self.assertEqual(convert_to_regex(1), "[ ]+[\w]+[ ]+")
        self.assertEqual(convert_to_regex(2), "[ ]+[\w]+[ ]+[\w]+[ ]+")
        self.assertEqual(convert_to_regex(3), "[ ]+[\w]+[ ]+[\w]+[ ]+[\w]+[ ]+")




if __name__ == '__main__':
    unittest.main()