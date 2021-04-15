import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

How_the_defirex = driver.find_element_by_id('mat-expansion-panel-header-2').click()

medium = driver.find_element_by_id('article_medium').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://defirex.medium.com/how-it-works-6db8679052ad"
driver.quit()
