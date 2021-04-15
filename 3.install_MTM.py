import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()

driver.get('https://defirex.org/')
driver.implicitly_wait(5)

install_Metamask = driver.find_element_by_id('Open_Modal_install_Metamask').click()
Setup_MetaMask = driver.find_element_by_css_selector('.mask_container>.ng-star-inserted>.custom_button.green').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://metamask.io/"
driver.close()
driver.quit()

