#ces commandes sont liees l'application sous test
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
titre_page=driver.title
print(titre_page)
url_page=driver.current_url
print(url_page)
code_source=driver.page_source
print(code_source)

time.sleep(4)
driver.close()