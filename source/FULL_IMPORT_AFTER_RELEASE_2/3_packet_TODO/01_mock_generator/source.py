def some_generator():
    for i in range(5):
        yield i*i

def wrapper():
    generator_as_list = list(some_generator())
    length = len(generator_as_list)
    print(generator_as_list, length)