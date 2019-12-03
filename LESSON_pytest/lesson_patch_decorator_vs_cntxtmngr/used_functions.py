
def function_to_replace():
    print("It should not be executed! 5/6")
    return "7 BAD"

def function_to_tmock():
    print("It should not be executed! 6/6")
    return "8 BAD"

def function_to_save():
    print("Executed 6/6")
    return "9 good"