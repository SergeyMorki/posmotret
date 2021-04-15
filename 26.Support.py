import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

footLink_support = driver.find_element_by_id('footLink_support').click()
time.sleep(2)
send_message_sup = driver.find_element_by_css_selector('.input-group-append>.custom_button.green').click()
close_allert_sup = driver.find_element_by_css_selector('.mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary').click()
close_support = driver.find_element_by_css_selector('.mat-icon.notranslate.material-icons.mat-icon-no-color').click()
driver.quit()

