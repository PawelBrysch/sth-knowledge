''' long version'''
# class File():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.open_file = open(self.filename, self.mode)
#         return self.open_file
#
#     def __exit__(self, *args):
#         print("wychodze")
#         self.open_file.close()
"""
przewaga wersji long?->                                          mozna dac `return self` zamiast `return self.open_file`
"""

# IMPORTANT
''' short version'''
# from contextlib import contextmanager
#
# @contextmanager
# def File(path, mode):
#     the_file = open(path, mode)
#     yield the_file
#     the_file.close()

''' code '''
# files = []
# for _ in range(3):
#     with File('foo.txt', 'w') as infile:
#         infile.write('foo2')
#         files.append(infile)


"""#######################
Task killer
#######################"""
# from contextlib import contextmanager
# import threading
# # import thread
# import _thread
#
#
# class TimeoutException(Exception):
#     def __init__(self, msg=''):
#         self.msg = msg
#
#
# @contextmanager
# def time_limit(seconds, msg=''):
#     # timer = threading.Timer(seconds, lambda: thread.interrupt_main())
#     timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
#     timer.start()
#     try:
#         yield
#     except KeyboardInterrupt:
#         raise TimeoutException("Timed out for operation {}".format(msg))
#     finally:
#         # if the action ends in specified time, timer is canceled
#         timer.cancel()
#
#
# def execute_no_matter_how(method, time):
#     try:
#         with time_limit(time, 'sleep'):
#             method()
#     except TimeoutException:
#         return False
#     else:
#         return True
#
#
# def some_method():
#     cntr = 1
#     while(True):
#         cntr += 1
#         if cntr % 20000 == 0:
#             print(cntr)
#
# execute_no_matter_how(some_method, 2)