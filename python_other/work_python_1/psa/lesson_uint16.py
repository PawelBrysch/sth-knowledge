import ctypes

a = ctypes.c_uint16()
# a = ctypes.c_int()

number = 1

for i in range(20):
    number = 2 * number
    a.value = number
    print i+1, a.value