def message(s):
    print(s)

def alterContents(myIterable):
    return [i for i in myIterable if i % 2 == 0]

def combine(messageFunc, itFunc):
    messageFunc("Printing the Iterable")
    a = itFunc(range(1, 20))
    return set(a)



message(2)
