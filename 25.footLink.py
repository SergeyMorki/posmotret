import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

footLink_audit = driver.find_element_by_id('footLink_audit').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/pessimistic-io/audits/blob/main/DeFireX%20Security%20Audit%20by%20Pessimistic%20Public.pdf"
driver.close()
driver.switch_to.window(current_window)

footLink_contract = driver.find_element_by_id('footLink_contract').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/address/0xb942ca22e0eb0f2524f53f999ae33fd3b2d58e3e#code"
driver.close()
driver.switch_to.window(current_window)

footLink_github = driver.find_element_by_id('footLink_github').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/DeFireX"
driver.close()
driver.switch_to.window(current_window)

footLink_licence = driver.find_element_by_id('footLink_licence').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert 'www.teatmik.ee' in driver.current_url
driver.close()
driver.switch_to.window(current_window)
driver.quit()