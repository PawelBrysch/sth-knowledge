from ctypes import Structure, c_uint16

class Int(Structure):
    _fields_ = [("first_16", c_uint16, 4),
                ("second_16", c_uint16, 16)]


print Int
print Int.first_16
print Int.second_16

myint = Int()
print "\n"

myint.first_16 = 7
myint.second_16 = 8

print myint
print myint.first_16
print myint.second_16



"""
    Trzeci argument naprawde ogranicza
"""
# number = 1
# for i in range(20):
#     number = 2 * number
#     myint.first_16 = number
#     print i+1, myint.first_16
#
#
# print "\n"
#
# number = 1
# for i in range(20):
#     number = 2 * number
#     myint.second_16 = number
#     print i+1, myint.second_16


"""
    Znaczenie maja LSB przekazywanej liczby
"""
# number = 0
# for i in range(100):
#     number = number + 1
#     myint.first_16 = number
#     print i+1, myint.first_16

"""
    (Chyba) nie da sie iterowac po tym "_fields_"
"""
#print myint._fields_[0].value
# for elem in myint._fields_:
#     print myint.elem