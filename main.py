from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service("/Users/breakthealgo/Downloads/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)

    driver.\
        execute_cdp_cmd('Network.setUserAgentOverride',{"userAgent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'})

    driver.get("https://twitter.com/i/flow/login")

    username = "breakingthealgo"
    password = "thebesttutorial"

    WebDriverWait(driver, 20)\
        .until(expected_conditions.
               element_to_be_clickable((By.XPATH, "//input[@type='text']")))\
        .send_keys(username)

    time.sleep(2)

    WebDriverWait(driver, 20) \
        .until(expected_conditions.
               element_to_be_clickable((By.XPATH, "//input[@type='text']"))) \
        .send_keys(Keys.RETURN)

    time.sleep(2)

    WebDriverWait(driver, 20) \
        .until(expected_conditions.
               element_to_be_clickable((By.XPATH, "//input[@type='password']"))) \
        .send_keys(password)

    time.sleep(2)

    WebDriverWait(driver, 20) \
        .until(expected_conditions.
               element_to_be_clickable((By.XPATH, "//input[@type='password']"))) \
        .send_keys(Keys.RETURN)

    time.sleep(10)



