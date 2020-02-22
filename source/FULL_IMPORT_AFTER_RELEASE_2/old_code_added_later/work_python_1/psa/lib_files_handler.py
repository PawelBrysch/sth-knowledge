import os
import shutil

def get_current_location():
    return os.path.dirname(os.path.abspath(__file__))

def remove_file(full_path):
    os.remove(full_path)


def remove_directory(full_path):
    shutil.rmtree(full_path)


def filenames_in_directory(path0):
    return os.listdir(path0)


def remove_files_from_directory(dirpath, list_of_exceptions):
    list_of_filenames = filenames_in_directory(dirpath)
    for filename in list_of_filenames:
        if True not in [filename.endswith(exception) for exception in list_of_exceptions]:
            fullpath = dirpath + "\\" + filename
            try:
                remove_file(fullpath)
            except WindowsError:
                remove_directory(fullpath)





