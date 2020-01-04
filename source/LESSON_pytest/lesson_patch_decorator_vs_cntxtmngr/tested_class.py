from LESSON_pytest.lesson_patch_decorator_vs_cntxtmngr.used_class import UsedClass
from LESSON_pytest.lesson_patch_decorator_vs_cntxtmngr.used_functions import function_to_replace, function_to_save, function_to_tmock

class TestedClass:
    def own_method_to_replace(self):
        print("It should not be executed! 1/6")
        return "1 BAD"

    def own_method_to_tmock(self):
        print("It should not be executed! 2/6")
        return "2 BAD"

    def own_method_to_save(self):
        print("Executed 2/6")
        return "3 good"

    def tested_method(self):
        # helper = UsedClass()
        helper = UsedClass()

        result = []
        result.append(self.own_method_to_replace())
        result.append(self.own_method_to_tmock())
        result.append(self.own_method_to_save())
        result.append(helper.foreign_method_to_replace())
        result.append(helper.foreign_method_to_tmock())
        result.append(helper.foreign_method_to_save())
        result.append(function_to_replace())
        result.append(function_to_tmock())
        result.append(function_to_save())

        return result