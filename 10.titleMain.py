import time

from selenium import webdriver  # импортируем webdriver

display = Display(visible=0, size=(1920, 1080))  
display.start()
driver1 = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver == driver1
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

App = driver.find_element_by_css_selector('.col-xl-6>.titleMain')
a = App.text
b = ("Earn 4x more with" + "\n" + "Compound risk-free!" + "\n" + "We have reduced fees for launching farming by more than 100 times together with Binance Smart Chain" + "\n" + "How it works")
assert a == b
driver.quit()
