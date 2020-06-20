# TODO 1. getElementBy

'''
1. boilerplate
2. driver.current_url
3. driver.page_source
'''
from lesson_selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\GlobalSDK\Selenium\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)

# driver.close()