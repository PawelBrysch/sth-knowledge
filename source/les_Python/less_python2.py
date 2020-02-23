''' % vs .format()'''
'''###########################'''
# name = [1,2,3]
# print("hi there %s" % name)
# print("hi there {0}".format(name))
# #-> OK

''' 1st advantage'''
# name = (1,2,3)
# print("hi there %s" % name)
# print("hi there {0}".format(name))
# # #-> error

# name = (1,2,3)
# print("hi there %s" % (name,))
# print("hi there {0}".format(name))
# # #-> OK, ale jak to wyglada

''' 2st advantage'''
# tu = (10,11,12,13,14,15,16)
# print('{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu))


'''#################'''
''' exec, eval'''
'''#################'''
# s = "print(\"Hello, World!\")"
#
# print(exec(s))
# print(eval(s))
#
# print("\n")
#
# s = "2+4"
#
# print(exec(s))
# print(eval(s))