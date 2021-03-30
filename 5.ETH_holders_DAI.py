from selenium import webdriver  # импортируем webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

display = Display(backend="xvfb")  
display.start()
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get('https://defirex.org/')

menu = driver.find_element_by_css_selector('.slog>.mobile_button').click()
wait = WebDriverWait(driver, 15).until

wait(EC.element_to_be_clickable((By.CSS_SELECTOR,'.menu>.mat-menu-trigger>.warranty'))).click()
wait(EC.element_to_be_clickable((By.CSS_SELECTOR,'.cdk-overlay-pane>.mat-menu-panel>.mat-menu-content>:nth-child(5)'))).click()

#eth_holders = driver.find_element_by_css_selector('.mat-menu-content>:nth-child(5)').click()
wait(EC.element_to_be_clickable((By.CSS_SELECTOR,'.cdk-overlay-pane>.mat-menu-panel>.mat-menu-content>[href="https://etherscan.io/token/0xF145A9e7Edc6D5a27BBdd16E4E29F5Fe56671A22#balances"]'))).click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xfACd9A6fD887855d9432F7a080911b26d9DCAE01#balances"
display.stop()
driver.quit()
