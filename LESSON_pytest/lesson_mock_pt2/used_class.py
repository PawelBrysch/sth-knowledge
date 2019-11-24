class UsedClass:
    def foreign_method_to_replace(self):
        print("It should not be executed! 3/6")
        return "4 BAD"

    def foreign_method_to_tmock(self):
        print("It should not be executed! 4/6")
        return "5 BAD"

    def foreign_method_to_save(self):
        print("Executed 4/6")
        return "6 good"
