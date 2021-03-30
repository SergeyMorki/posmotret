import time

from selenium import webdriver  # импортируем webdriver

display = Display(visible=0, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

system_balance = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.statistic_box>.stat>:nth-child(1)>:nth-child(1)>.ng-star-inserted')))
href = system_balance.get_attribute('href')
time.sleep(3)
assert href == 'https://etherscan.io/address/0x0bcbab2fecc30b7341132b4ebb36d352e035f1bd'

users_balance = driver.find_element_by_css_selector('.statistic_box>.stat>:nth-child(2)>:nth-child(1)>:nth-child(2)')
href = users_balance.get_attribute('href')
time.sleep(3)
assert href == 'https://etherscan.io/token/0xfacd9a6fd887855d9432f7a080911b26d9dcae01#balances'

daily_profit = driver.find_element_by_css_selector('.statistic_box>.stat>:nth-child(3)>:nth-child(1)>:nth-child(2)')
href = daily_profit.get_attribute('href')
time.sleep(3)
assert href == 'https://compound.finance/governance/address/0x0BCbAb2FeCC30B7341132B4Ebb36d352E035f1bD'
driver.quit()
