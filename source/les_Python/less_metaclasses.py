"""##########################################
Basics
##########################################"""
''' under the hood'''
# class_ref = type("ClassName", (), {"arg1": "initial_value"})
# obj1 = object.__new__(class_ref)
# print(obj1, "\n", obj1.arg1)

''' new (default implicit form)'''
# class SomeClass:
#     def __new__(cls, *args, **kwargs):
#         print("count!")
#         return object.__new__(cls)
#
# alis = [SomeClass() for i in range(2)]



"""##########################################
Custom metaclass
##########################################"""
def do_whatever_with_class_metaattributes(arg1, arg2, arg3):
    # do whatever
    return arg1, arg2, arg3

def do_whatever_during_definition():
    print("It is executed during definition, lol")

def some_metaclass(future_class_name, future_class_parents, future_class_attr):
    # FEATURE 1
    future_class_name, future_class_parents, future_class_attr = do_whatever_with_class_metaattributes(
        future_class_name, future_class_parents, future_class_attr
    )

    # FEATURE 2
    do_whatever_during_definition()

    return type(future_class_name, future_class_parents, future_class_attr)


class SomeClass(metaclass=some_metaclass):
    def __init__(self):
        self.attr1 = "some_val"



''' klasa metaclass'''
'''
a porpo linii: "class Foo(metaclass=UpperAttrMetaclass):"
mysle, ze w momencie "static" jest uzywana __new__ z metalasy i dostaje takie argumenty, jakich potrzebuje
'''
# class UpperAttrMetaclass(type):
#
#     def __new__(cls, clsname, bases, dct):
#
#         uppercase_attr = {}
#         for name, val in dct.items():
#             if not name.startswith('__'):
#                 uppercase_attr[name.upper()] = val
#             else:
#                 uppercase_attr[name] = val
#
#         return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)
#         # TODO niby jest __new__ i nie wiemy, co sie dzieje, ale gdzie tam wyjze jest metaklasa, ktora dziedziczy wprost
#         # TODO z "type" ( w naszym przypadku od razu). Wlascienie ona returnuje zwykle: type(clsname, (), dct), czyli zwraca
#         # TODO klasa, a o to chodzilo
#
#
# class Foo(metaclass=UpperAttrMetaclass):
#     bar = 'bip'
# # TODO powyzsze znaczy to samo, co ponizsze
# # Foo = UpperAttrMetaclass("Foo", (), {"bar":"bip"})
#
# print(Foo)
# print(type(Foo))
# print(type(type(Foo)))
# print(hasattr(Foo, 'bar'))
# print(hasattr(Foo, 'BAR'))
#
# f = Foo()
# print(f.BAR)
