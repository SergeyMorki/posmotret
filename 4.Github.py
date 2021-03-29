from selenium import webdriver  # импортируем webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
display = Display(visible=1, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

menu = driver.find_element_by_css_selector('.slog>.mobile_button').click()
wait = WebDriverWait(driver, 15).until

wait(EC.element_to_be_clickable((By.CSS_SELECTOR,'.menu>.mat-menu-trigger>.warranty'))).click()

github = driver.find_element_by_css_selector('.mat-menu-content>[href="https://github.com/DeFireX"]').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/DeFireX"
driver.quit()
