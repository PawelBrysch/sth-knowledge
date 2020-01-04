import win32com.client as win32
from win32gui import GetWindowText, GetForegroundWindow
import time
import ntpath
import urllib


def get_basename_from_path(fullpath):
    return ntpath.basename(fullpath)


def string_from_url(url_0):
    return urllib.unquote(str(url_0))


def get_paths_of_explorer_windows():
    clsid = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}' #Valid for IE as well!
    shellwindows = win32.Dispatch(clsid)
    paths = []
    try:
        for window in range(shellwindows.Count):
            window_URL = shellwindows[window].LocationURL
            window_dir = window_URL.split("///")[1].replace("/", "\\")
            paths.append(window_dir)
    except:
        pass
    del shellwindows
    return paths


def get_foldername_of_foreground_window(test_mode=False):
    if test_mode:
        time.sleep(5)
    return GetWindowText(GetForegroundWindow())


def get_path_to_foreground_window(test_mode=False):
    paths_of_windows = get_paths_of_explorer_windows()
    folder_name_of_foreground_window = get_foldername_of_foreground_window(test_mode)
    paths_of_windows = list(map(string_from_url, paths_of_windows))
    possible_results = [elem for elem in paths_of_windows
                        if folder_name_of_foreground_window == get_basename_from_path(elem)]
    return possible_results[0]





