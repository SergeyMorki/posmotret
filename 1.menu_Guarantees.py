import time

from selenium import webdriver  # импортируем webdriver


driver = webdriver.Chrome()
driver.get('https://defirex.org/')
driver.implicitly_wait(5)

menu = driver.find_element_by_class_name('mobile_button').click()
Guarantees = driver.find_element_by_link_text('Guarantees').click()
balance_on_Etherscan = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(1)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/address/0x0bcbab2fecc30b7341132b4ebb36d352e035f1bd"
driver.close()
driver.switch_to.window(current_window)


Guarantees = driver.find_element_by_link_text('Guarantees').click()
profit = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(2)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://compound.finance/governance/address/0x0BCbAb2FeCC30B7341132B4Ebb36d352E035f1bD"
driver.close()
driver.switch_to.window(current_window)


Guarantees = driver.find_element_by_link_text('Guarantees').click()
audit = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(3)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/pessimistic-io/audits/blob/main/DeFireX%20Security%20Audit%20by%20Pessimistic%20Public.pdf"
driver.close()
driver.switch_to.window(current_window)


Guarantees = driver.find_element_by_link_text('Guarantees').click()
git = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(4)').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://github.com/DeFireX"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_css_selector('#mat-menu-panel-0>:nth-child(1)>:nth-child(6)').click()
BUSDUSDT = driver.find_element_by_link_text('BUSD+USDT funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0x987f04DecE1c5AE9E69cF4F93D00bBE2cA5Af98c"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_css_selector('.cdk-overlay-pane>:nth-child(1)>:nth-child(1)>:nth-child(6)').click()
DFXBUSD = driver.find_element_by_link_text('DFX-BUSD funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0xe4743bee99d515a2C36C30B37e3756750fE24c9D"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_css_selector('.cdk-overlay-pane>:nth-child(1)>:nth-child(1)>:nth-child(6)').click()
DFX_funds = driver.find_element_by_link_text('DFX funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0x11340dC94E32310FA07CF9ae4cd8924c3cD483fe"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_css_selector('.cdk-overlay-pane>:nth-child(1)>:nth-child(1)>:nth-child(6').click()
btcb = driver.find_element_by_link_text('BTCB funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0x7CA1fEA7d198cEaE9A319B5EE89E860aAB7D82d7"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_link_text('BSC holders').click()
busd_holders = driver.find_element_by_link_text('BUSD funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0xAB2f29783265940305EA99573AA18bD301911a09"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_css_selector('.cdk-overlay-pane>:nth-child(1)>:nth-child(1)>:nth-child(6').click()
elipsis = driver.find_element_by_link_text('3POOL ELIPSIS funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0x5DaA08aF18104702d4a387027E09b9b83b0fc720"
driver.close()
driver.switch_to.window(current_window)


Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_css_selector('.cdk-overlay-pane>:nth-child(1)>:nth-child(1)>:nth-child(6').click()
nerve = driver.find_element_by_link_text('3POOL NERVE funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0x48bFdF75B1315A2D27293fAD7221790f3DfeA1b0"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_css_selector('.cdk-overlay-pane>:nth-child(1)>:nth-child(1)>:nth-child(6').click()
eth = driver.find_element_by_link_text('ETH funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0x735ba150d6A842B1feE3737F023fDdF781CfEaA0"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_css_selector('.cdk-overlay-pane>:nth-child(1)>:nth-child(1)>:nth-child(6').click()
xrp = driver.find_element_by_link_text('XRP funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0x2df142fc7e0f7164c90c9f93e3012d956c34c299"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
bsc_holders = driver.find_element_by_css_selector('.cdk-overlay-pane>:nth-child(1)>:nth-child(1)>:nth-child(6').click()
dott = driver.find_element_by_link_text('DOT funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://www.bscscan.com/token/0xaa954f2c619377a61380bfd084359e69d445a856"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
work = driver.find_element_by_link_text('How it works').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://defirex.medium.com/how-it-works-6db8679052ad"
driver.close()
driver.switch_to.window(current_window)

Guarantees = driver.find_element_by_link_text('Guarantees').click()
eth_holders = driver.find_element_by_link_text('Ethereum holders').click()
DAI_funds_holders = driver.find_element_by_link_text('DAI funds holders').click()
new_window = driver.window_handles[1]
current_window = driver.current_window_handle
driver.switch_to.window(new_window)
assert driver.current_url == "https://etherscan.io/token/0xfACd9A6fD887855d9432F7a080911b26d9DCAE01"
driver.close()
driver.switch_to.window(current_window)

driver.quit()