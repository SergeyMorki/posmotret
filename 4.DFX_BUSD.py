import time

from selenium import webdriver  # импортируем webdriver

driver = webdriver.Chrome()

driver.get('https://defirex.org/')
driver.implicitly_wait(5)
#pools = .pools.curr1.ng-star-inserted
DFX_BUSD = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(1)').click()
buy_DFX = driver.find_element_by_link_text('Buy DFX and BUSD tokens 50/50').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://exchange.pancakeswap.finance/#/swap?inputCurrency=0xe9e7cea3dedca5984780bafc599bd69add087d56&outputCurrency=0x74b3abb94e9e1ecc25bd77d6872949b4a9b2aacf"
driver.close()
driver.switch_to.window(current_window)

add_liq = driver.find_element_by_link_text('Add Liquidity and Get DFX-BUSD-LP tokens on PancakeSwap').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://exchange.pancakeswap.finance/#/add/0xe9e7cea3dedca5984780bafc599bd69add087d56/0x74b3abb94e9e1ecc25bd77d6872949b4a9b2aacf"
driver.close()
driver.switch_to.window(current_window)

supply_DFX = driver.find_element_by_link_text('Supply DFX-BUSD-LP tokens on DeFireX').click()
add_liq_PS = driver.find_element_by_link_text('Add Liquidity using PancakeSwap').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://exchange.pancakeswap.finance/#/add/0xe9e7cea3dedca5984780bafc599bd69add087d56/0x74b3abb94e9e1ecc25bd77d6872949b4a9b2aacf"
driver.close()
driver.switch_to.window(current_window)

add_liq_Defirex = driver.find_element_by_link_text('Add Liquidity using DeFireX').click()
max = driver.find_element_by_css_selector('.mat-form-field-suffix.ng-star-inserted').click()
input1 = driver.find_element_by_id('mat-input-12')
input1.click()
input1.send_keys(123)
input2 = driver.find_element_by_id('mat-input-13')
input2.click()
input2.send_keys(123)
message1 = driver.find_element_by_css_selector('.input-group>.description>:nth-child(1)').text
assert message1 == 'Insufficient BUSD balance'
message2 = driver.find_element_by_css_selector('.input-group>.description>:nth-child(2)').text
assert message2 == 'Insufficient DFX balance'

close = driver.find_element_by_css_selector('.mat-dialog-actions>:nth-child(1)>:nth-child(1)').click()

info = driver.find_element_by_css_selector('.header>.lp>:nth-child(2)>:nth-child(1)>:nth-child(1)').click()
time.sleep(1)
info_ok = driver.find_element_by_css_selector('.mat-focus-indicator.mat-raised-button.mat-button-base.mat-primary').click()
DFX_BUSD = driver.find_element_by_css_selector('.pools.curr1.ng-star-inserted>:nth-child(1)').click()
withdraw = driver.find_element_by_css_selector('.dep>.mat-tab-group.mat-primary>.mat-tab-header>.mat-tab-label-container>.mat-tab-list>.mat-tab-labels>:nth-child(2)').click()
MAX_withdraw = driver.find_element_by_link_text('MAX withdraw and Get DFX-BUSD-LP tokens').click()
Change_DFX_BUSD = driver.find_element_by_link_text('Change DFX-BUSD-LP token on PancakeSwap -> get DFX and BUSD').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://exchange.pancakeswap.finance/#/pool"
driver.close()
driver.switch_to.window(current_window)

driver.quit()




