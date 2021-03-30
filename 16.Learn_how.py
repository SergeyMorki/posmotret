import time

from selenium import webdriver  # импортируем webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

Learn1 = driver.find_element_by_id('learn1').click()
Learn2 = driver.find_element_by_id('learn2').click()
Learn3 = driver.find_element_by_id('learn3').click()
Learn4 = driver.find_element_by_id('learn4').click()

driver.quit()
