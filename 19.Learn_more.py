import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

time.sleep(1)
learn_more = driver.find_element_by_id('explore5').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://defirex.medium.com/dfx-token-airdrop-for-active-users-of-the-defirex-platform-2bec6b973cc6"
driver.quit()
