import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

App = driver.find_element_by_link_text('App').click()
assert driver.current_url == "https://defirex.org/account"
driver.back()
driver.quit()