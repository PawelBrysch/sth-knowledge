'''
1 . co robi `__new__()`?->                                  ustala, co bedzie returnowac konstruktor (na swoim returnie)
'''
# class ProperClass():
#     def __new__(cls, *args, **kwargs):
#         print("Creating Instance")
#         print(args, kwargs)
#         instance = object.__new__(cls)
#         return instance
#
#     def __init__(self, aa):
#         self.a = aa
#
# class MockedClass():
#     def __new__(cls, *args, **kwargs):
#         print("Creating Instance")
#         print(args, kwargs)
#         return "lol"
#
#     def __init__(self, aa):
#         self.a = aa
#
#
# p = ProperClass(5)
# print("was created: ", p, "\n")
# m = MockedClass(5)
# print("was created: ", m)