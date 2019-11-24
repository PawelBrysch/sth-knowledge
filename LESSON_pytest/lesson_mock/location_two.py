from LESSON_pytest.lesson_mock.location_one import Foo

def some_function():
    obj = Foo()

    print("class_.class_attribute:", Foo.class_attribute)
    print("class_.class_method:   ", Foo.class_method())
    print("obj.instance_attribute:", obj.instance_attribute)
    print("obj.instance_method:   ", obj.instance_method())


def some_function_which_only_calls_instance_method():
    obj = Foo()
    print("obj.instance_method:   ", obj.instance_method())