'''
1.driver.back() [and .forward()]->                                                                      strona przod/tyl
2. driver.find_element_by_name("userName").send_keys("ohcyrb")
3. driver.implicitly_wait(seconds)->                          czeka na zaladowanie sie DOM (time.sleep() freezuje chyba)
'''

from lesson_selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\GlobalSDK\Selenium\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
# driver.implicitly_wait(seconds)
assert "Welcome: Mercury Tours" in driver.title
