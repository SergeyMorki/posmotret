import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

Guarantees = driver.find_element_by_css_selector('.mat-focus-indicator>.mat-button-wrapper')
Guarantees.click()
eth_holders = driver.find_element_by_css_selector('.mat-menu-content>:nth-child(5)').click()
owners_DAI = driver.find_element_by_css_selector('#cdk-overlay-1>:nth-child(1)>:nth-child(1)>:nth-child(1)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xfACd9A6fD887855d9432F7a080911b26d9DCAE01#balances"
driver.quit()