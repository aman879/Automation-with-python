from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.coursera.org/login")
    return driver

def main():
    driver = get_driver()
    driver.find_element(by="id", value="email").send_keys("aman9693kumar@gmail.com")
    time.sleep(2)
    driver.find_element(by="id", value="password").send_keys("Shaurya@123" + Keys.RETURN)
    time.sleep(2)

print(main())