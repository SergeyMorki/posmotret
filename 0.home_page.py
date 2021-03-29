import time

from selenium import webdriver  # импортируем webdriver
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1920, 1080))  
display.start()
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

logo = driver.find_element_by_css_selector('.col-xl-2.col-lg-2.col-md-2.col-sm-6.col-6.logo_box').click()
menu = driver.find_element_by_css_selector('.slog>.mobile_button').click()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 15).until
wait(EC.element_to_be_clickable((By.CSS_SELECTOR,'.menu>.mat-menu-trigger'))).click()

wait(EC.element_to_be_clickable((By.CSS_SELECTOR,'.mat-menu-content>:nth-child(1)'))).click()

new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
driver.quit()
