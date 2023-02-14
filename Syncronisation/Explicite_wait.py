#import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import *

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#driver.implicitly_wait(20)
mywait=WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[Exception])
driver.get("https://google.ca")
#time.sleep(4)
#driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("selenium")
searchgoogle=mywait.until(EC.presence_of_element_located((By.NAME,"q")))
#searchgoogle=driver.find_element(By.NAME,"q")
searchgoogle.send_keys("selenium")
searchgoogle.submit()
#time.sleep(3)
#resultlink=driver.find_element(By.XPATH,'//h3[text()="Selenium"]')
resultlink=mywait.until(EC.presence_of_element_located((By.XPATH,'//h3[text()="Selenium"]')))
resultlink.click()
driver.close()