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
on_ETH = driver.find_element_by_link_text('Users balances on Ethereum')
time.sleep(2)
on_ETH.click()
DAI_funds = driver.find_element_by_link_text('DAI funds holders')
time.sleep(2)
DAI_funds.click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xfACd9A6fD887855d9432F7a080911b26d9DCAE01"
driver.close()
driver.switch_to.window(current_window)
users_balance = driver.find_element_by_css_selector('.mat-menu-trigger.ng-star-inserted').click()
time.sleep(2)
ETH_funds = driver.find_element_by_link_text('Users balances on BSC').click()
time.sleep(2)
DAI_funds = driver.find_element_by_link_text('DAI funds holders').click()

new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0x308853AeC7cF0ECF133ed19C0c1fb3b35f5a4E7B"
driver.close()
driver.switch_to.window(current_window)
time.sleep(2)

users_balance = driver.find_element_by_css_selector('.mat-menu-trigger.ng-star-inserted').click()
ETH_funds = driver.find_element_by_link_text('Users balances on BSC').click()
DAI_funds = driver.find_element_by_link_text('BUSD funds holders').click()

new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0x987f04DecE1c5AE9E69cF4F93D00bBE2cA5Af98c"
driver.close()
driver.switch_to.window(current_window)
time.sleep(2)
users_balance = driver.find_element_by_css_selector('.mat-menu-trigger.ng-star-inserted').click()
ETH_funds = driver.find_element_by_link_text('Users balances on BSC').click()
time.sleep(1)
DAI_funds = driver.find_element_by_link_text('USDT funds holders').click()

new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0xb7552a0463515BDa8B47ab7503ca893E52c58Df8"
driver.close()
driver.switch_to.window(current_window)
time.sleep(2)
users_balance = driver.find_element_by_css_selector('.mat-menu-trigger.ng-star-inserted').click()
ETH_funds = driver.find_element_by_link_text('Users balances on BSC').click()
time.sleep(2)
DAI_funds = driver.find_element_by_link_text('DFXBUSD funds holders').click()

new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0xE7FF9AcEB3767B4514d403D1486B5D7f1b787989"
driver.close()
driver.switch_to.window(current_window)
time.sleep(2)
users_balance = driver.find_element_by_css_selector('.mat-menu-trigger.ng-star-inserted').click()
ETH_funds = driver.find_element_by_link_text('Users balances on BSC').click()
time.sleep(2)
DAI_funds = driver.find_element_by_link_text('DFX funds holders').click()

new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0x11340dC94E32310FA07CF9ae4cd8924c3cD483fe"
driver.close()
driver.switch_to.window(current_window)

driver.quit()
