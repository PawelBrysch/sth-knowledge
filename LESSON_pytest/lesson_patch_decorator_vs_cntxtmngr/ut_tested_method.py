# from LESSON_pytest.lesson_patch_decorator_vs_cntxtmngr.tested_class import TestedClass
# from unittest.mock import patch
# def replaced_own_method(self):
#     print("Executed 1/6")
#     return "1 good"
# def replaced_foreign_method(self):
#     print("Executed 3/6")
#     return "4 good"
# def replaced_function():
#     print("Executed 5/6")
#     return "7 good"
# PATH_TO_PACKAGE = "LESSON_pytest.lesson_patch_decorator_vs_cntxtmngr"
"""
██╗      ██████╗  ██████╗ ██╗  ██╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗    ██╗██╗██╗
██║     ██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║    ██║██║██║
██║     ██║   ██║██║   ██║█████╔╝     ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║    ██║██║██║
██║     ██║   ██║██║   ██║██╔═██╗     ██║  ██║██║   ██║██║███╗██║██║╚██╗██║    ╚═╝╚═╝╚═╝
███████╗╚██████╔╝╚██████╔╝██║  ██╗    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║    ██╗██╗██╗
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝    ╚═╝╚═╝╚═╝
"""
'''
jaka jest roznica generalnie?                                      w dekoratorze nie dziala "return_value" (stad lambdy)
'''
#
#
# with patch(PATH_TO_PACKAGE + ".tested_class.TestedClass.own_method_to_replace", new=replaced_own_method), \
#      patch(PATH_TO_PACKAGE + ".tested_class.TestedClass.own_method_to_tmock", return_value="2 good"), \
#      patch(PATH_TO_PACKAGE + ".tested_class.UsedClass.foreign_method_to_replace", new=replaced_foreign_method), \
#      patch(PATH_TO_PACKAGE + ".tested_class.UsedClass.foreign_method_to_tmock", return_value="5 good"), \
#      patch(PATH_TO_PACKAGE + ".tested_class.function_to_replace", new=replaced_function), \
#      patch(PATH_TO_PACKAGE + ".tested_class.function_to_tmock", return_value="8 good"):
#
#     obj = TestedClass()
#     print(obj.tested_method())
#
# @patch(PATH_TO_PACKAGE + ".tested_class.TestedClass.own_method_to_replace", new=replaced_own_method)
# @patch(PATH_TO_PACKAGE + ".tested_class.TestedClass.own_method_to_tmock", new=lambda self: "2 good")
# @patch(PATH_TO_PACKAGE + ".tested_class.UsedClass.foreign_method_to_replace", new=replaced_foreign_method)
# @patch(PATH_TO_PACKAGE + ".tested_class.UsedClass.foreign_method_to_tmock", new=lambda self: "5 good")
# @patch(PATH_TO_PACKAGE + ".tested_class.function_to_replace", new=replaced_function)
# @patch(PATH_TO_PACKAGE + ".tested_class.function_to_tmock", new=lambda: "8 good")
# def test():
#     obj = TestedClass()
#     res = obj.tested_method()
#     assert res == ['1 good', '2 good', '3 good', '4 good', '5 good', '6 good', '7 good', '8 good', '9 good']
#
# test()



