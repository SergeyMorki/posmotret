import time

from selenium import webdriver  # импортируем webdriver

display = Display(visible=0, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

daily_profit = driver.find_element_by_css_selector('.statistic_box>.stat>:nth-child(3)>:nth-child(1)>:nth-child(2)')
href = daily_profit.get_attribute('href')
time.sleep(3)
assert href == 'https://compound.finance/governance/address/0x0BCbAb2FeCC30B7341132B4Ebb36d352E035f1bD'
driver.quit()
