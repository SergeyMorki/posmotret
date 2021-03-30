import time

from selenium import webdriver  # импортируем webdriver

display = Display(visible=0, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

Install_MTM = driver.find_element_by_id('Open_Modal_install_Metamask').click()
close_alert_mtm = driver.find_element_by_css_selector('.mat-focus-indicator.mat-button.mat-button-base>.mat-button-wrapper').click()
driver.quit()
