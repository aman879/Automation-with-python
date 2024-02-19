from selenium import webdriver
import time

def get_email_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://dropmail.me/en/")
    return driver

def get_name_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://randomwordgenerator.com/name.php")
    return driver

def main():
    i = 0
    while(i < 5):
        email_driver = get_email_driver()
        time.sleep(2)
        email = email_driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div/div/span[1]").text
        name_driver = get_name_driver()
        name = name_driver.find_element(by="xpath", value="/html/body/div[2]/div/div[3]/div/div/div[2]/div/ol/li/div/span").text
        content = name+","+email
        print(content)
        with open('contacts.csv', 'a') as file:
            file.write(content + '\n')
        i+=1
    return 1

print(main())