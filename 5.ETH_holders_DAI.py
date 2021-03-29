from selenium import webdriver  # импортируем webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
display = Display(visible=0, size=(1920, 768))  
display.start()
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get('https://defirex.org/')

menu = driver.find_element_by_css_selector('.slog>.mobile_button').click()
wait = WebDriverWait(driver, 15).until

wait(EC.element_to_be_clickable((By.CSS_SELECTOR,'.menu>.mat-menu-trigger>.warranty'))).click()

wait(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mat-menu-content>:nth-child(5)'))).click()

#eth_holders = driver.find_element_by_css_selector('.mat-menu-content>:nth-child(5)').click()
owners_DAI = driver.find_element_by_css_selector('#cdk-overlay-1>:nth-child(1)>:nth-child(1)>:nth-child(1)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xfACd9A6fD887855d9432F7a080911b26d9DCAE01#balances"
display.stop()
driver.quit()
