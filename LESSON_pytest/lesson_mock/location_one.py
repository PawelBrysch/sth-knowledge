import os
from LESSON_pytest.lesson_mock.location_two import Foo


def some_function():
    obj = Foo()
    print("class_.class_attribute:", Foo.class_attribute)
    print("class_.class_method:   ", Foo.class_method())
    print("obj.instance_attribute:", obj.instance_attribute)
    print("obj.instance_method:   ", obj.instance_method())


def use_os_and_print_getcwd_external():
    print(os.getcwd())


