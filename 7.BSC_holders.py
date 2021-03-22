import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

Guarantees = driver.find_element_by_css_selector('.mat-focus-indicator>.mat-button-wrapper')
Guarantees.click()
BSC_holders = driver.find_element_by_css_selector('.mat-menu-content>:nth-child(6)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://bscscan.com/token/0x308853AeC7cF0ECF133ed19C0c1fb3b35f5a4E7B#balances"
driver.quit()
