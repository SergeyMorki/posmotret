import time

from selenium import webdriver  # импортируем webdriver
display = Display(visible=0, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

App = driver.find_element_by_link_text('App').click()
assert driver.current_url == "https://defirex.org/account"
driver.back()
display.stop()
driver.quit()
