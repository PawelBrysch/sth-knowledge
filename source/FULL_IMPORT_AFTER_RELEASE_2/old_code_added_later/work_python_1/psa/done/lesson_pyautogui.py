import pyautogui
from pywinauto import Application
from time import sleep


app = Application().start(r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
sleep(2)
maximise_button_location = pyautogui.locateOnScreen('pyautogui_images\\maximise.png')
if maximise_button_location is not None:
    pyautogui.click(maximise_button_location, pause=2.)

pyautogui.typewrite('https://en.wikipedia.org/wiki/Relay')
pyautogui.press('enter', pause=2.)
pyautogui.moveTo(1000, 600)
pyautogui.scroll(-1000, pause=1.)
im = pyautogui.screenshot(region=(0,0, 300, 400))
im.save("pyautogui_images\\temp\\siemanko.png")
