import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()

driver.get('https://defirex.org/')
driver.implicitly_wait(5)

menu = driver.find_element_by_class_name('mobile_button').click()
pools = driver.find_element_by_link_text('Pools').click()
time.sleep(2)
close = driver.find_element_by_css_selector('.first_level>.close').click()
DFX_BUSD = driver.find_element_by_css_selector('.header>.lp').click()

menu = driver.find_element_by_class_name('mobile_button').click()
wiki = driver.find_element_by_link_text('Wiki').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://wiki.defirex.org/"
driver.close()
driver.switch_to.window(current_window)

DFX_Airdrop = driver.find_element_by_link_text('DFX Airdrop').click()
current_window = driver.current_window_handle
assert driver.current_url == "https://defirex.org/airdrop-dfx"
buy = driver.find_element_by_link_text('Buy DFX').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://app.1inch.io/#/56/swap/BUSD/DFX"

driver.quit()
