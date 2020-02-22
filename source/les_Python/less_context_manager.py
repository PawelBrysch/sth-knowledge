
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
