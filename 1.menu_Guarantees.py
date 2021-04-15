import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()

driver.get('https://defirex.org/')
driver.implicitly_wait(5)

menu = driver.find_element_by_class_name('mobile_button').click()
Guarantees = driver.find_element_by_link_text('Guarantees').click()
balance_on_Etherscan = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(1)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/address/0x0bcbab2fecc30b7341132b4ebb36d352e035f1bd"
driver.close()
driver.switch_to.window(current_window)


Guarantees = driver.find_element_by_link_text('Guarantees').click()
profit = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(2)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://compound.finance/governance/address/0x0BCbAb2FeCC30B7341132B4Ebb36d352E035f1bD"
driver.close()
driver.switch_to.window(current_window)


Guarantees = driver.find_element_by_link_text('Guarantees').click()
audit = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(3)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/pessimistic-io/audits/blob/main/DeFireX%20Security%20Audit%20by%20Pessimistic%20Public.pdf"
driver.close()
driver.switch_to.window(current_window)


Guarantees = driver.find_element_by_link_text('Guarantees').click()
git = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(4)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/DeFireX"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(6)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://bscscan.com/token/0x308853AeC7cF0ECF133ed19C0c1fb3b35f5a4E7B#balances"
driver.close()
driver.switch_to.window(current_window)


Guarantees = driver.find_element_by_link_text('Guarantees').click()
work = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(7)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://defirex.medium.com/how-it-works-6db8679052ad"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
own_DAI = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(5)').click()
Funds_Owners_DAI = driver.find_element_by_link_text('Funds Owners DAI').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xfACd9A6fD887855d9432F7a080911b26d9DCAE01#balances"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
own_ETH = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(5)').click()
Funds_Owners_ETH = driver.find_element_by_link_text('Funds Owners ETH').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xF145A9e7Edc6D5a27BBdd16E4E29F5Fe56671A22#balances"

driver.quit()