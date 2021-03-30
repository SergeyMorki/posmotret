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
driver.implicitly_wait(5)

Install_MTM = driver.find_element_by_id('Open_Modal_install_Metamask').click()
close_alert_mtm = driver.find_element_by_css_selector('.mat-focus-indicator.mat-button.mat-button-base>.mat-button-wrapper').click()
driver.quit()
