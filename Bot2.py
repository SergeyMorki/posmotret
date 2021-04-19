import telebot
from telebot import types
bot = telebot.TeleBot('1796101968:AAHOK-xIisX3bdfjc91yUAU-D-ehCsUSKG8')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "bot":
        bot.send_message(message.chat.id, 'Ты написал мне, вот полезности', reply_markup=first_keyboard())
    elif message.text == "Bot":
        bot.send_message(message.chat.id, 'Ты написал мне, вот полезности', reply_markup=first_keyboard())
    elif message.text == "бот":
        bot.send_message(message.chat.id, 'Ты написал мне, вот полезности', reply_markup=first_keyboard())
    elif message.text == "Бот":
        bot.send_message(message.chat.id, 'Ты написал мне, вот полезности', reply_markup=first_keyboard())
    elif message.text == "help":
        bot.send_message(message.chat.id, 'Ты написал мне, вот полезности', reply_markup=first_keyboard())
    elif message.text == "/Bot":
        bot.send_message(message.from_user.id, 'Ты написал мне, вот полезности', reply_markup=base_keyboard())
    elif message.text == "/bot":
        bot.send_message(message.from_user.id, 'Ты написал мне, вот полезности', reply_markup=base_keyboard())
    elif message.text == "/бот":
        bot.send_message(message.from_user.id, 'Ты написал мне, вот полезности', reply_markup=base_keyboard())
    elif message.text == "/Бот":
        bot.send_message(message.from_user.id, 'Ты написал мне, вот полезности', reply_markup=base_keyboard())
    elif message.text == "/help":
        bot.send_message(message.from_user.id, 'Ты написал мне, вот полезности', reply_markup=base_keyboard())
    elif message.text == "start":
        bot.send_message(message.chat.id, 'Ты написал мне, вот полезности', reply_markup=first_keyboard())
    elif message.text == "/start":
        bot.send_message(message.from_user.id, 'Вот полезности', reply_markup=base_keyboard())

def first_keyboard():
    keyboard_1 = [
        [
        types.InlineKeyboardButton(text="Помощник DeFireX", url="https://t.me/DefirexRuBot")
        ],
    ]
    return types.InlineKeyboardMarkup(keyboard_1)

def base_keyboard():
    keyboard = [
        [
            types.InlineKeyboardButton(text="Сайт DeFireX", url="https://defirex.org/"),
            types.InlineKeyboardButton(text="О DeFireX", callback_data=3),
        ],
        [
            types.InlineKeyboardButton(text="Ближайшие события", callback_data=2),
            types.InlineKeyboardButton(text="Гид. Как пользоваться?", callback_data=4),
        ],
        [
            types.InlineKeyboardButton(text="Обратные выкупы DFX", url="https://github.com/DeFireX/buybackDFX"),
        ],
    ]
    return types.InlineKeyboardMarkup(keyboard)

def base_inline_keyboard():
    keyboard1 = [
        [
            types.InlineKeyboardButton(text="О компании", url="https://wiki.defirex.org/ru/about.html"),
            types.InlineKeyboardButton(text="Гарантии", url="https://wiki.defirex.org/ru/guarantees.html"),
        ],
        [
            types.InlineKeyboardButton(text="Токен DFX", url="https://wiki.defirex.org/ru/dfxtoken.html"),
            types.InlineKeyboardButton(text="Доходные стратегии", url="https://wiki.defirex.org/ru/strategy.html"),
        ],
        [
            types.InlineKeyboardButton(text="Управление DFX", url="https://wiki.defirex.org/ru/governance.html"),
            types.InlineKeyboardButton(text="Контракты", url="https://wiki.defirex.org/ru/contracts.html"),
        ],
        [
            types.InlineKeyboardButton(text="Аудиты", url="https://wiki.defirex.org/ru/audits.html"),
            types.InlineKeyboardButton(text="FAQ", url="https://wiki.defirex.org/ru/faq.html"),
        ],
        [
            types.InlineKeyboardButton(text="Назад", callback_data=5)
        ]
    ]
    return types.InlineKeyboardMarkup(keyboard1)

def inline_keyboard():
    keyboard2 = [
        [
            types.InlineKeyboardButton(text="Пополнение Metamask", url="https://wiki.defirex.org/ru/instructionsRu.html#metamask"),
        ],
        [
            types.InlineKeyboardButton(text="Вывод монет", url="https://wiki.defirex.org/ru/instructionsRu.html#defirex"),
        ],
        [
            types.InlineKeyboardButton(text="Добавление кастомного токена в MetaMask", url="https://wiki.defirex.org/ru/instructionsRu.html#id2"),
        ],
        [
            types.InlineKeyboardButton(text="Перевод токенов из сети Eth в BSC сеть", url="https://wiki.defirex.org/ru/instructionsRu.html#metamask-ethereum-bsc"),
        ],
        [
            types.InlineKeyboardButton(text="Пополнение пула, стейкинг, фарминг", url="https://wiki.defirex.org/ru/instructionsRu.html#id3"),
        ],
        [
            types.InlineKeyboardButton(text="Фарминг в пуле DFX-BUSD", url="https://wiki.defirex.org/ru/instructionsRu.html#dfx-busd-pancakeswap-lp-cake-bsc"),
        ],
        [
            types.InlineKeyboardButton(text="Переключение Metamask на сеть Binance Smart Chain", url="https://wiki.defirex.org/ru/instructionsRu.html#metamask-binance-smart-chain"),
        ],
        [
            types.InlineKeyboardButton(text="Перевод DFX из Ethereum в BSC сеть", url="https://wiki.defirex.org/ru/instructionsRu.html#dfx-ethereum-bsc"),
        ],
        [
            types.InlineKeyboardButton(text="Работа сервиса в телефоне", url="https://wiki.defirex.org/ru/instructionsRu.html#id4"),
        ],
        [
            types.InlineKeyboardButton(text="Сервис на Trust Wallet в iOS", url="https://wiki.defirex.org/ru/instructionsRu.html#c-trust-wallet-ios"),
        ],
        [
            types.InlineKeyboardButton(text="Назад", callback_data=5)
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
        bot.send_message(call.message.chat.id,"Недавно:" + "\n" + "11.03.2021 - Листинг токена DFX на CoinMarketCap" + "\n" + "12.03.2021 - Завершения private-sale раундов" + "\n" +
                         "15.03.2021 - AirDrop 100.000 DFX" + "\n" + "20.03.2021 - Листинг на 1inch" + "\n" +
                         "31.03.2021 - Листинг на CoinGecko" + "\n" + " " + "\n"
                         "Уже скоро:" + "\n" + "20.04.2021 - Участие на международном форуме Blockchain Life 2021" + "\n" +
                         "Q1-Q2 2021 - Добавление пула BTC" + "\n" +
                         "Q2-Q4 2021 - Добавление новых пулов ETH, BNB и стейблкоинов")
    elif call.data == '1':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=base_keyboard())

bot.polling()