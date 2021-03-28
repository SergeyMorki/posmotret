import time

from selenium import webdriver  # импортируем webdriver
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 1200))  
display.start()
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

logo = driver.find_element_by_css_selector('.col-xl-2.col-lg-2.col-md-2.col-sm-6.col-6.logo_box').click()
time.sleep(5)
Guarantees = driver.find_element_by_css_selector('.mat-ripple.mat-button-ripple.mat-button-ripple-round').click()

balance_on_Etherscan = driver.find_element_by_link_text('Check balance on Etherscan').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
driver.quit()
