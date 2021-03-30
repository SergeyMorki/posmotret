import time

from selenium import webdriver  # импортируем webdriver

display = Display(visible=0, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

users_balance = driver.find_element_by_css_selector('.statistic_box>.stat>:nth-child(2)>:nth-child(1)>:nth-child(2)')
href = users_balance.get_attribute('href')
time.sleep(3)
assert href == 'https://etherscan.io/token/0xfacd9a6fd887855d9432f7a080911b26d9dcae01#balances'
driver.quit()
