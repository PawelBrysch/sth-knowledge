
''' new '''
''' args, kwargs w new sa raczej nieobowiazkowe, ale nie zaomnimy ich napisac
'''
# class SomeClass:
#     classArg = 1
#
#     def __new__(cls, *args, **kwargs):
#         print("new")
#         return object.__new__(cls)
#
#
#     def __init__(self, aa):
#         print("init")
#         self.arg1 = aa
#
#
# obj1 = SomeClass(11)
# obj2 = SomeClass(12)



''' method metaclass -> (str, tuple, dict)'''
# def upper_attr(future_class_name, future_class_parents, future_class_attr):
#
#     uppercase_attr = {}
#     for name, val in future_class_attr.items():
#         if not name.startswith('__'):
#             uppercase_attr[name.upper()] = val
#         else:
#             uppercase_attr[name] = val
#
#     return type(future_class_name, future_class_parents, uppercase_attr)
#
#
# class Foo( metaclass=upper_attr):
#     bar = 'bip'
#
#
# print(hasattr(Foo, 'bar'))
# print(hasattr(Foo, 'BAR'))
#
# f = Foo()
# print(f.BAR)

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
