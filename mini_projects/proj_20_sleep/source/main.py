import os


BROWSERS_NAMES = [
    "chrome.exe",
    "firefox.exe"
]

def close_app(app_name):
    os.system("TASKKILL /F /IM " + app_name)

def close_browsers(browsers_names):
    for browser_name in browsers_names:
        close_app(browser_name)

if __name__ == "__main__":
    close_browsers(BROWSERS_NAMES)
