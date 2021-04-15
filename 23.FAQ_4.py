import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

How_profit = driver.find_element_by_id('mat-expansion-panel-header-3').click()

balance_on_compound = driver.find_element_by_id('Balance_on_Compound').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://compound.finance/governance/address/0x0BCbAb2FeCC30B7341132B4Ebb36d352E035f1bD"
driver.close()
driver.switch_to.window(current_window)


balance_on_Etherscan = driver.find_element_by_id('Balance_on_Etherscan').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)

assert driver.current_url == "https://etherscan.io/address/0x0bcbab2fecc30b7341132b4ebb36d352e035f1bd#tokentxns"
driver.close()
driver.switch_to.window(current_window)

balance_on_BSC = driver.find_element_by_id('Balance_on_BSC').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)

assert driver.current_url == "https://bscscan.com/address/0xca0648c5b4cea7d185e09fcc932f5b0179c95f17#tokentxns"
driver.quit()
