import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()

driver.get('https://defirex.org/')
driver.implicitly_wait(5)

check = driver.find_element_by_link_text('Check balance on Etherscan').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/address/0x0bcbab2fecc30b7341132b4ebb36d352e035f1bd#tokentxns"
driver.close()
driver.switch_to.window(current_window)

read = driver.find_element_by_link_text('Read the Security Audit').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/pessimistic-io/audits/blob/main/DeFireX%20Security%20Audit%20by%20Pessimistic%20Public.pdf"
driver.close()
driver.switch_to.window(current_window)

see = driver.find_element_by_link_text('See code on GitHub').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/DeFireX"
driver.close()
driver.switch_to.window(current_window)

guide = driver.find_element_by_link_text('See guide').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://defirex.org/assets/data/autonome_client_instruction_en.pdf"
driver.close()
driver.switch_to.window(current_window)

driver.quit()
