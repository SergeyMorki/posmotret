import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)


What_is = driver.find_element_by_id('mat-expansion-panel-header-0')
What_is.click()
What_is.click()

code_on_github = driver.find_element_by_id('source_github').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/DeFireX"
driver.close()
driver.switch_to.window(current_window)

owners_in_ETH = driver.find_element_by_id('funds_owners_eth')
owners_in_ETH.click()

owners_DAI = driver.find_element_by_css_selector('.mat-menu-content>:nth-child(1)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xfACd9A6fD887855d9432F7a080911b26d9DCAE01#balances"
driver.close()
driver.switch_to.window(current_window)

owners_in_ETH.click()

owners_ETH = driver.find_element_by_css_selector('.mat-menu-content>:nth-child(2)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xF145A9e7Edc6D5a27BBdd16E4E29F5Fe56671A22#balances"
driver.close()
driver.switch_to.window(current_window)

owners_in_BSC = driver.find_element_by_id('funds_owners_bsc')
link_owners_BSC = owners_in_BSC.get_attribute('href')
assert link_owners_BSC == 'https://bscscan.com/token/0x308853AeC7cF0ECF133ed19C0c1fb3b35f5a4E7B#balances'

driver.quit()
