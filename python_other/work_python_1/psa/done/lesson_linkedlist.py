from collections import deque
from linkedlist import *

def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print("B {0} {1}".format(func.__name__, time.clock()-t))
        return time.clock()-t
    return wrapper


size = 1000000
K = 100

lis0 = []
linked = LinkedList()

for i in range(size):
    lis0.append(i)
    linked.add_to_back(i)

dlis = deque(lis0)


@benchmark
def delete_array():
    global lis0
    global K
    lis0.remove(K)


@benchmark
def delete_deque():
    global dlis
    global K
    dlis.remove(K)

@benchmark
def delete_linked_list():
    global linked
    global K

    found = linked.find_first(K)
    linked.remove(found)


result = []
for i in range(1, 999999, 100000):
    K = i
    result.append([delete_array(), delete_deque(), delete_linked_list()])


