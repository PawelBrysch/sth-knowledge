from enum import Enum


class MyEnum(Enum):
    val1 = "str1"
    val2 = "str2"



a1 = MyEnum.val1
b1 = "str1"
a2 = MyEnum.val2
b2 = "str2"

print(isinstance(a1, MyEnum))
print(isinstance(b1, MyEnum))
print(isinstance(a2, MyEnum))
print(isinstance(b2, MyEnum))