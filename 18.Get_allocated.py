import time

from selenium import webdriver  # импортируем webdriver

display = Display(visible=0, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

time.sleep(1)
get_allocation = driver.find_element_by_css_selector('.pools>:nth-child(4)>:nth-child(3)').click()
pole = driver.find_element_by_id('mat-input-0').send_keys('defirextest@gmail.com')
send = driver.find_element_by_css_selector('.input-group>.custom_button').click()
ok_alert_error = driver.find_element_by_css_selector('.mat-focus-indicator.mat-raised-button.mat-button-base').click()
close_allocation = driver.find_element_by_css_selector('.mat-icon.notranslate.material-icons.mat-icon-no-color').click()
driver.quit()
