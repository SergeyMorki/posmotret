import time

from selenium import webdriver  # импортируем webdriver

display = Display(visible=0, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
supply1 = driver.find_element_by_css_selector('.pools>:nth-child(1)>:nth-child(3)').click()
time.sleep(2)
assert driver.current_url == "https://defirex.org/account#eth"
driver.back()
time.sleep(2)
supply2 = driver.find_element_by_css_selector('.pools>:nth-child(2)>:nth-child(3)').click()
time.sleep(2)
assert driver.current_url == "https://defirex.org/account#eth"
driver.back()
supply3 = driver.find_element_by_css_selector('.pools>:nth-child(3)>:nth-child(3)').click()

driver.quit()
