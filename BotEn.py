import telebot
from telebot import types
bot = telebot.TeleBot('1706660828:AAHP5MA4HA1Q0ZAkBAFAw2W8Qd8pJWLbcP0')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "bot":
        bot.send_message(message.chat.id, 'You wrote me. Usefull links are here', reply_markup=first_keyboard())
    elif message.text == "Bot":
        bot.send_message(message.chat.id, 'You wrote me. Usefull links are here', reply_markup=first_keyboard())
    elif message.text == "help":
        bot.send_message(message.chat.id, 'You wrote me. Usefull links are here', reply_markup=first_keyboard())
    elif message.text == "start":
        bot.send_message(message.chat.id, 'You wrote me. Usefull links are here', reply_markup=first_keyboard())
    elif message.text == "/bot":
        bot.send_message(message.chat.id, 'Usefull links are here', reply_markup=base_keyboard())
    elif message.text == "/Bot":
        bot.send_message(message.chat.id, 'Usefull links are here', reply_markup=base_keyboard())
    elif message.text == "/help":
        bot.send_message(message.chat.id, 'Usefull links are here', reply_markup=base_keyboard())
    elif message.text == "/start":
        bot.send_message(message.from_user.id, 'You wrote me. Usefull links are here', reply_markup=base_keyboard())

def first_keyboard():
    keyboard_1 = [
        [
        types.InlineKeyboardButton(text="DeFireX assistant", url="https://t.me/DefirexEnBot")
        ],
    ]
    return types.InlineKeyboardMarkup(keyboard_1)
def base_keyboard():
    keyboard = [
        [
            types.InlineKeyboardButton(text="Site DeFireX", url="https://defirex.org/"),
            types.InlineKeyboardButton(text="About Defirex", callback_data=3),
        ],
        [
            types.InlineKeyboardButton(text="Upcoming events", callback_data=2),
            types.InlineKeyboardButton(text="Guide (How to use?)", callback_data=4),
        ],
        [
            types.InlineKeyboardButton(text="DFX buybacks history", url="https://github.com/DeFireX/buybackDFX"),
        ],
    ]
    return types.InlineKeyboardMarkup(keyboard)

def base_inline_keyboard():
    keyboard1 = [
        [
            types.InlineKeyboardButton(text="About", url="https://wiki.defirex.org/about.html"),
            types.InlineKeyboardButton(text="Guarantees & Proof", url="https://wiki.defirex.org/guarantees.html"),
        ],
        [
            types.InlineKeyboardButton(text="DFX token", url="https://wiki.defirex.org/dfxtoken.html"),
            types.InlineKeyboardButton(text="Pools & Earn Strategy", url="https://wiki.defirex.org/strategy.html"),
        ],
        [
            types.InlineKeyboardButton(text="Governance (DFX)", url="https://wiki.defirex.org/governance.html"),
            types.InlineKeyboardButton(text="Contracts", url="https://wiki.defirex.org/contracts.html"),
        ],
        [
            types.InlineKeyboardButton(text="Audits", url="https://wiki.defirex.org/audits.html"),
            types.InlineKeyboardButton(text="FAQ", url="https://wiki.defirex.org/faq.html")
        ],
        [
            types.InlineKeyboardButton(text="Back", callback_data=5)
        ]
    ]
    return types.InlineKeyboardMarkup(keyboard1)

def inline_keyboard():
    keyboard2 = [
        [
            types.InlineKeyboardButton(text="Replenishment MetaMask", url="https://wiki.defirex.org/instructions.html"),
        ],
        [
            types.InlineKeyboardButton(text="Withdrawal", url="https://wiki.defirex.org/instructions.html#how-to-withdrawn-funds-from-defirex")
        ],
        [
            types.InlineKeyboardButton(text="Adding a custom token to MetaMask", url="https://wiki.defirex.org/instructions.html#how-to-add-a-custom-token-to-metamask-wallet"),
        ],
        [
            types.InlineKeyboardButton(text="Transfering tokens from Eth network to BSC network in MetaMask", url="https://wiki.defirex.org/instructions.html#how-to-transfer-tokens-from-ethereum-network-to-bsc-network-in-metamask")
        ],
        [
            types.InlineKeyboardButton(text="Start staking and farming", url="https://wiki.defirex.org/instructions.html#how-to-replenish-the-pool-and-start-staking-and-farming"),
        ],
        [
            types.InlineKeyboardButton(text="Start DFX-BUSD farming", url="https://wiki.defirex.org/instructions.html#how-to-start-dfx-busd-farming-guide-how-to-add-liquidity-to-pancakeswap-lp-cake-bsc")
        ],
        [
            types.InlineKeyboardButton(text="Switch MetaMask to Binance Smart Chain", url="https://wiki.defirex.org/instructions.html#how-to-switch-metamask-to-binance-smart-chain"),
        ],
        [
            types.InlineKeyboardButton(text="Transfer DFX from Eth to BSC", url="https://wiki.defirex.org/instructions.html#how-to-transfer-dfx-from-ethereum-to-bsc")
        ],
        [
            types.InlineKeyboardButton(text="Use DeFireX on phone", url="https://wiki.defirex.org/ru/instructionsRu.html#id4")
        ],
        [
            types.InlineKeyboardButton(text="Use Trust Wallet on iOS", url="https://wiki.defirex.org/ru/instructionsRu.html#c-trust-wallet-ios")
        ],
        [
            types.InlineKeyboardButton(text="Back", callback_data=5)
        ]
    ]
    return types.InlineKeyboardMarkup(keyboard2)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == '3':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=base_inline_keyboard())
    elif call.data == '4':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=inline_keyboard())
    elif call.data == '5':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=base_keyboard())
    elif call.data == '2':
        bot.send_message(call.message.chat.id, "Recently:" + "\n" +
                         "11.03.2021 - Listed DFX token on CoinMarketCap" + "\n" + "12.03.2021 - Ended private-sale rounds" + "\n" +
                         "15.03.2021 - AirDrop 100.000 DFX" + "\n" + "20.03.2021 - Listed on 1inch" + "\n" + "31.03.2021 - Listed on CoinGecko"
                         " " + "\n" + "In future:" + "\n" + "20.04.2021 - Participation in the international forum Blockchain Life 2021" + "\n"
                         "Q1-Q2 2021 - Add BTC pool" + "\n" +
                         "Q1-Q4 2021 - Add new pools ETH, BNB and stable coins", reply_markup=base_keyboard())

    elif call.data == '1':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=base_keyboard())

bot.polling()