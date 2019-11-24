''' template2
var = 1
alis = [1,2 ,3]
def some_func():
    print "elo"
adict = {"a":1, "b":2}
'''

from done import lib_execution_handler

a = lib_execution_handler.__dict__
a1 = a["alis"]
b=1