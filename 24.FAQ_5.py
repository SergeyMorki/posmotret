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

time.sleep(1)
audit_secure = driver.find_element_by_id('mat-expansion-panel-header-4').click()
time.sleep(2)
audit_secure = driver.find_element_by_id('Audit').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/pessimistic-io/audits/blob/main/DeFireX%20Security%20Audit%20by%20Pessimistic%20Public.pdf"
driver.close()
driver.switch_to.window(current_window)

audit_secure = driver.find_element_by_id('guide').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://defirex.org/assets/data/autonome_client_instruction_en.pdf"
driver.close()
driver.switch_to.window(current_window)

client_download = driver.find_element_by_id('autonome_client')
zip = client_download.get_attribute('href')
assert zip == "https://defirex.org/assets/data/autonome-client.zip"
driver.quit()

