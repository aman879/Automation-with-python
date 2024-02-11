from selenium import webdriver
import time
from datetime import datetime as dt
import os

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    output = float(text.split(": ")[1])
    return output

def write_file(text, path):
    filename = f"{dt.now().strftime("%d-%m-%Y.%H-%M-%S")}.txt"
    with open(path + '/' + filename, 'w') as file:
        file.write(text)

def main():
    driver = get_driver()
    i = 0
    parent_dir = os.getcwd()
    new_path = "storedTime"
    path = os.path.join(parent_dir, new_path)
    os.mkdir(path)
    while (i < 2):
        time.sleep(2)
        element = clean_text(driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text)
        text = str(element)
        write_file(text, path)
        i += 1

print(main())

