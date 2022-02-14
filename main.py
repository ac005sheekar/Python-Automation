import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("http://cse.iubat.edu/faculty/")
print(driver.title) #print page title


#search = driver.find_elements_by_name("s")
#search.send_keys("test")
#search.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()

