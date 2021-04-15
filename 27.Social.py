import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

footLink_telegram = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'footLink_telegram'))).click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://t.me/defirex"
driver.close()
driver.switch_to.window(current_window)

footLink_medium = driver.find_element_by_id('footLink_medium').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
time.sleep(1)
assert driver.current_url == "https://defirex.medium.com/"
driver.close()
driver.switch_to.window(current_window)

footLink_discord = driver.find_element_by_id('footLink_discord').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
time.sleep(1)
assert 'discord' in driver.current_url
driver.close()
driver.switch_to.window(current_window)

footLink_twitter = driver.find_element_by_id('footLink_twitter').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://twitter.com/DeFireXorg"
driver.close()
driver.switch_to.window(current_window)
driver.quit()
