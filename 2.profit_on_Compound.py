import time

from selenium import webdriver  # импортируем webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
display = Display(visible=0, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
driver.implicitly_wait(10)

menu = driver.find_element_by_css_selector('.slog>.mobile_button').click()
wait = WebDriverWait(driver, 15).until
wait(EC.element_to_be_clickable((By.CSS_SELECTOR,'.menu>.mat-menu-trigger>.warranty'))).click()

balance_on_Compound = driver.find_element_by_link_text('Check profit on Compound').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://compound.finance/governance/address/0x0BCbAb2FeCC30B7341132B4Ebb36d352E035f1bD"
display.stop()
driver.quit()
