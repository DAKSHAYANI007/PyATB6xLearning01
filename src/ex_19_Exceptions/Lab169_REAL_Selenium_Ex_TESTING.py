#Handling exception with Selenium


from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.get("https://www.youtubbbbbe.com/")
    driver.find_element("id","not exist button")
except NoSuchElementException as nse:
    print("Element Not Found",nse.msg)