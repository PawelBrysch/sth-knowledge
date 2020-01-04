import multiprocessing

result_nonshared = []

def calc_square(numbers, array, queue):
    global result_nonshared
    pass

counter = 0

print "before", counter, id(counter), __name__
counter += 1

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=calc_square, args=(1,2,3)) #argumenty sa kopiowane
    p1.start()
    p1.join()
    print "inside", counter, id(counter), __name__
    counter += 1


print "after", counter, id(counter), __name__
counter += 1




