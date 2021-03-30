import time

from selenium import webdriver  # импортируем webdriver

display = Display(visible=0, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

Learn1 = driver.find_element_by_id('learn1').click()
Learn2 = driver.find_element_by_id('learn2').click()
Learn3 = driver.find_element_by_id('learn3').click()
Learn4 = driver.find_element_by_id('learn4').click()

driver.quit()
