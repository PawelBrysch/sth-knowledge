'''
BigEndian vs LittleEndian - ocb?-> o kolejnosc bitow w bajcie (ale nie o kolejnosc bajtow)
what is the purpose of the code below?->                                                       easy access to bits/bytes
'''
# from ctypes import BigEndianStructure, LittleEndianStructure, Structure, Union, c_uint16
#
# # class Flags_bits(BigEndianStructure):
# class Flags_bits(LittleEndianStructure):
#     _fields_ = [("bit15", c_uint16, 1),
#                 ("bit14", c_uint16, 1),
#                 ("bit13", c_uint16, 1),
#                 ("bit12", c_uint16, 1),
#                 ("bit11", c_uint16, 1),
#                 ("bit10", c_uint16, 1),
#                 ("bit9", c_uint16, 1),
#                 ("bit8", c_uint16, 1),
#                 ("bit7", c_uint16, 1),
#                 ("bit6", c_uint16, 1),
#                 ("bit5", c_uint16, 1),
#                 ("bit4", c_uint16, 1),
#                 ("bit3", c_uint16, 1),
#                 ("bit2", c_uint16, 1),
#                 ("bit1", c_uint16, 1),
#                 ("bit0", c_uint16, 1), ]
#
# class Flags_bytes(Structure):
#     _fields_ = [("byte1", c_uint16, 8),
#                 ("byte0", c_uint16, 8), ]
#
#
# class Relays(Union):
#     memory = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     _fields_ = [("bits", Flags_bits),
#                 ("bytes", Flags_bytes),
#                 ("word", c_uint16)]
#
# relay1 = Relays()
#
# # 11111000 11000000 -> 63680
# # 11111000          -> 248
# #          11000000 -> 192
#
# relay1.word = 63680
#
# print(relay1.word)
# print("\n")
# print(relay1.bits.bit0)
# print(relay1.bits.bit1)
# print(relay1.bits.bit2)
# print(relay1.bits.bit3)
# print(relay1.bits.bit4)
# print(relay1.bits.bit5)
# print(relay1.bits.bit6)
# print(relay1.bits.bit7)
# print(relay1.bits.bit8)
# print(relay1.bits.bit9)
# print(relay1.bits.bit10)
# print(relay1.bits.bit11)
# print(relay1.bits.bit12)
# print(relay1.bits.bit13)
# print(relay1.bits.bit14)
# print(relay1.bits.bit15)
# print("\n")
# print(relay1.bytes.byte0)
# print(relay1.bytes.byte1)

