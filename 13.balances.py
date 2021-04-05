import time

from selenium import webdriver  # импортируем webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
display = Display(visible=0, size=(1024, 768))
display.start()
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get('https://defirex.org/')
driver.implicitly_wait(10)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

users_balance = driver.find_element_by_css_selector('.mat-menu-trigger.ng-star-inserted').click()
on_ETH = driver.find_element_by_css_selector('.cdk-overlay-pane>.mat-menu-panel>.mat-menu-content>:nth-child(1)')
time.sleep(2)
on_ETH.click()
time.sleep(2)
DAI_funds = driver.find_element_by_link_text('DAI funds holders')
time.sleep(2)
DAI_funds.click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xfACd9A6fD887855d9432F7a080911b26d9DCAE01"
driver.close()
driver.switch_to.window(current_window)
time.sleep(2)
users_balance = driver.find_element_by_css_selector('.mat-menu-trigger.ng-star-inserted').click()
on_ETH = driver.find_element_by_css_selector('.cdk-overlay-pane>.mat-menu-panel>.mat-menu-content>:nth-child(1)')
time.sleep(2)
on_ETH.click()
ETH_funds = driver.find_element_by_link_text('ETH funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xF145A9e7Edc6D5a27BBdd16E4E29F5Fe56671A22"

driver.quit()
