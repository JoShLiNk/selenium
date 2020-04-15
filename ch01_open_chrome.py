from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
driver=webdriver.Chrome(chrome_options=chrome_options)

driver.get("Http://testwisely.com/demo")
time.sleep(5)
driver.quit()