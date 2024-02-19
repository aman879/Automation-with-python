from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def get_driver():

    profile_path = r"C:\Users\aman9\AppData\Roaming\Mozilla\Firefox\Profiles\emtijyoa.default-release"
    options = webdriver.FirefoxOptions()
    options.profile = profile_path
    driver = webdriver.Firefox(options=options)
    driver.get("https://cyfrin.deform.cc/early-access?referral=pY63VWUvcX5y")
    return driver

def click_element(driver, path):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, path))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()

def wait_until_text_changes_to(driver, locator, target_text):
    def text_changes_to(driver):
        current_text = driver.find_element(by="xpath", value=locator).text
        return current_text == target_text
    
    WebDriverWait(driver, 100).until(text_changes_to)

def main():
    df = pd.read_csv('contacts.csv')
    for index, row in df.iterrows():
        print(row['name'])
        driver = get_driver()
        time.sleep(2)
        driver.find_element(by="xpath", value="/html/body/div[1]/main/div/div[2]/div/div/div/div/div/div[2]/form/fieldset/div[2]/div/input").send_keys(row['email'] + Keys.RETURN)
        time.sleep(5)
        click_element(driver=driver, path="html/body/div[1]/main/div/div[2]/div/div[1]/div/form/fieldset/div/div[2]/div/div/div/div[2]")
        click_element(driver=driver, path="/html/body/div[1]/main/div/div[2]/div/div[1]/div/form/fieldset/div/div[1]/div[1]/div[2]/div[1]/div[1]/label/div[1]")
        click_element(driver=driver, path="/html/body/div[1]/main/div/div[2]/div/div[1]/div/form/fieldset/div/div[1]/div[3]/div[2]/div[1]/div[1]/label/div[1]")
        click_element(driver=driver, path="/html/body/div[1]/main/div/div[2]/div/div[1]/div/form/fieldset/div/div[1]/div[4]/div[2]/div[1]/div[1]/label/div[1]")
        click_element(driver=driver, path="/html/body/div[1]/main/div/div[2]/div/div[1]/div/form/fieldset/div/div[1]/div[5]/div[2]/div[1]/div[4]/label/div[1]")
        click_element(driver=driver, path="/html/body/div[1]/main/div/div[2]/div/div[1]/div/form/fieldset/div/div[1]/div[6]/div[2]/div[1]/div[2]/label/div[1]")
        click_element(driver=driver, path="/html/body/div[1]/main/div/div[2]/div/div[1]/div/form/fieldset/div/div[1]/div[7]/div[2]/div[1]/div[3]/label/div[1]")

        wait_until_text_changes_to(driver, "html/body/div[1]/main/div/div[2]/div/div[1]/div/form/fieldset/div/div[2]/div/div/div/div[2]", "Captcha solved!")
        
        driver.find_element(by="xpath", value="/html/body/div[1]/main/div/div[2]/div/div[1]/div/form/fieldset/div/div[1]/div[8]/div[2]/div/div/input").send_keys(row['name'] + Keys.RETURN)
        click_element(driver=driver, path="/html/body/div[1]/main/div/div[2]/div/div[1]/div/form/fieldset/div/div[3]/button")
        driver.quit()
    return 1

print(main())