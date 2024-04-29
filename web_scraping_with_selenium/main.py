


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r'C:\Users\HP\Downloads\chromedriver-win64 (1)')

service.start()

driver = webdriver.Remote(service.service_url)

driver.get('https://www.adamchoi.co.uk/overs/detailed/');

time.sleep(5) # Let the user actually see something!

#driver.quit()