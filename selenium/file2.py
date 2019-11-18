'''
1.find_element_by_xpath()
2.elem.click()
3.quit()
'''

from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="D:\GlobalSDK\Selenium\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")



elem = driver.find_element_by_xpath("//*[@id='Tabbed']/a/button")
print(elem.text)
time.sleep(5)
# driver.


driver.close()
driver.quit()

# print(driver.page_source)