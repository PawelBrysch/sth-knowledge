import unittest

from lib_windows_analyser import get_basename_from_path

class TestAll(unittest.TestCase):

    def test_get_basename_from_path(self):
        self.assertEqual(get_basename_from_path("a/b/c"), "c")
        self.assertEqual(get_basename_from_path("a\b\c"), "c")
        self.assertEqual(get_basename_from_path("a//b//c"), "c")
        self.assertEqual(get_basename_from_path("a\\b\\c"), "c")

        # special char
        self.assertEqual(get_basename_from_path("a/n/c"), "c")
        self.assertEqual(get_basename_from_path("a\n\c"), "c")
        self.assertEqual(get_basename_from_path("a//n//c"), "c")
        self.assertEqual(get_basename_from_path("a\\n\\c"), "c")

        # slash at begin
        self.assertEqual(get_basename_from_path("/a/n/c"), "c")
        self.assertEqual(get_basename_from_path("\\a\n\c"), "c")
        self.assertEqual(get_basename_from_path("//a//n//c"), "c")
        self.assertEqual(get_basename_from_path("\\a\\n\\c"), "c")

        # just_slash
        self.assertEqual(get_basename_from_path("/c"), "c")
        self.assertEqual(get_basename_from_path("\c"), "c")
        self.assertEqual(get_basename_from_path("//c"), "c")
        self.assertEqual(get_basename_from_path("\\c"), "c")

        # nothing
        self.assertEqual(get_basename_from_path("c"), "c")
        self.assertEqual(get_basename_from_path("c"), "c")
        self.assertEqual(get_basename_from_path("c"), "c")
        self.assertEqual(get_basename_from_path("c"), "c")


if __name__ == '__main__':
    unittest.main()