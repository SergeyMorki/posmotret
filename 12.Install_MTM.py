import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

Install_MTM = driver.find_element_by_id('Open_Modal_install_Metamask').click()
close_alert_mtm = driver.find_element_by_css_selector('.mat-focus-indicator.mat-button.mat-button-base>.mat-button-wrapper').click()
driver.quit()
