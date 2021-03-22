import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

time.sleep(1)
How_we_manage = driver.find_element_by_id('mat-expansion-panel-header-1')
How_we_manage.click()
driver.quit()