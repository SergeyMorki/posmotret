import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://defirex.org/')
driver.implicitly_wait(5)
#pools = .pools.curr1.ng-star-inserted
pool = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(2)').click()
input2 = driver.find_element_by_css_selector('.active>.moreInfo>.dep>.mat-tab-group>.mat-tab-body-wrapper>.mat-tab-body-active>:nth-child(1)>:nth-child(2)>.input>:nth-child(1)')
input2.send_keys('123')

pool1 = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(3)').click()
input3 = driver.find_element_by_css_selector('.active>.moreInfo>.dep>.mat-tab-group>.mat-tab-body-wrapper>.mat-tab-body-active>:nth-child(1)>:nth-child(1)>:nth-child(1)>:nth-child(1)')
input3.send_keys('123')

pool2 = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(4)').click()
input3 = driver.find_element_by_css_selector('.active>.moreInfo>.dep>.mat-tab-group>.mat-tab-body-wrapper>.mat-tab-body-active>:nth-child(1)>:nth-child(2)>.input>:nth-child(1)')
input3.send_keys('123')

pool3 = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(5)').click()
input3 = driver.find_element_by_css_selector('.active>.moreInfo>.dep>.mat-tab-group>.mat-tab-body-wrapper>.mat-tab-body-active>:nth-child(1)>:nth-child(1)>.input>:nth-child(1)')
input3.send_keys('123')

driver.quit()