import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

logo = driver.find_element_by_css_selector('.col-xl-2.col-lg-2.col-md-2.col-sm-6.col-6.logo_box').click()

Guarantees = driver.find_element_by_css_selector('.mat-focus-indicator>.mat-button-wrapper')
Guarantees.click()

balance_on_Etherscan = driver.find_element_by_link_text('Check balance on Etherscan').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
driver.quit()