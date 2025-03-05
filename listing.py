import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('TOKEN-BOT')

urlhoro = 'https://ignio.com/r/export/utf/xml/daily/com.xml'


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
    btn01 = types.KeyboardButton('♈️ Овен')
    btn02 = types.KeyboardButton('♉️ Телец')
    btn03 = types.KeyboardButton('♊️ Близнецы')
    btn04 = types.KeyboardButton('♋️ Рак')
    btn05 = types.KeyboardButton('♌️ Лев')
    btn06 = types.KeyboardButton('♍️ Дева')
    btn07 = types.KeyboardButton('♎️ Весы')
    btn08 = types.KeyboardButton('♏️ Скорпион')
    btn09 = types.KeyboardButton('♐️ Стрелец')
    btn10 = types.KeyboardButton('♑️ Козерог')
    btn11 = types.KeyboardButton('♒️ Водолей')
    btn12 = types.KeyboardButton('♓️ Рыбы')
    markup.add(btn01,btn02,btn03)
    markup.add(btn04,btn05,btn06)
    markup.add(btn07,btn08,btn09)
    markup.add(btn10,btn11,btn12)
    bot.send_message(message.from_user.id, '👋 <b> Добро пожаловать! </b> \n  Выбери свой знак зодиака:', parse_mode='html',reply_markup=markup)

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.from_user.id, ' <b>Скрипт написал Alex Karden -</b> https://github.com/alexkarden.\nДанные для гороскопов берутся с сайта ignio.com.', parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    content = requests.get(urlhoro).text
    soup = BeautifulSoup(content, 'xml')
    date = soup.find_all('date')
    todaydate = str(date)[14:24]
    tomorrowdate = str(date)[36:46]
    tomorrowdate2 = str(date)[60:70]

    if message.text == '♈️ Овен':
        horo = soup.find_all('aries')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id, f'🔯 <b>Гороскоп на сегодня</b>\n\n♈️ <b>Овен на {todaydate}</b> {today} \n♈️ <b>Овен на завтра {tomorrowdate}</b> {tomorrow}\n♈️ <b>Овен на послезавтра {tomorrowdate2}</b> {tomorrow2}', parse_mode='html')

    elif message.text == '♉️ Телец':
        horo = soup.find_all('taurus')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id, f'🔯 <b>Гороскоп на сегодня</b>\n\n♉️ <b>Телец на {todaydate}</b> {today} \n♉️ <b>Телец на завтра {tomorrowdate}</b> {tomorrow}\n♉️ <b>Телец на послезавтра {tomorrowdate2}</b> {tomorrow2}', parse_mode='html')

    elif message.text == '♊️ Близнецы':
        horo = soup.find_all('gemini')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id, f'🔯 <b>Гороскоп на сегодня</b>\n\n♊️ <b>Близнецы на {todaydate}</b> {today} \n♊️ <b>Близнецы на завтра {tomorrowdate}</b> {tomorrow}\n♊️ <b>Близнецы на послезавтра {tomorrowdate2}</b> {tomorrow2}', parse_mode='html')

    elif message.text == '♋️ Рак':
        horo = soup.find_all('cancer')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id, f'🔯 <b>Гороскоп на сегодня</b>\n\n♋️ <b>Рак на {todaydate}</b> {today} \n♋️ <b>Рак на завтра {tomorrowdate}</b> {tomorrow}\n♋️ <b>Рак на послезавтра {tomorrowdate2}</b> {tomorrow2}', parse_mode='html')

    elif message.text == '♌️ Лев':
        horo = soup.find_all('leo')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id, f'🔯 <b>Гороскоп на сегодня</b>\n\n♌️ <b>Лев на {todaydate}</b> {today} \n♌️ <b>Лев на завтра {tomorrowdate}</b> {tomorrow}\n♌️ <b>Лев на послезавтра {tomorrowdate2}</b> {tomorrow2}', parse_mode='html')

    elif message.text == '♍️ Дева':
        horo = soup.find_all('virgo')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id, f'🔯 <b>Гороскоп на сегодня</b>\n\n♍️ <b>Дева на {todaydate}</b> {today} \n♍️ <b>Дева на завтра {tomorrowdate}</b> {tomorrow}\n♍️ <b>Дева на послезавтра {tomorrowdate2}</b> {tomorrow2}', parse_mode='html')

    elif message.text == '♎️ Весы':
        horo = soup.find_all('libra')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id,f'🔯 <b>Гороскоп на сегодня</b>\n\n♎️ <b>Весы на {todaydate}</b> {today} \n♎️ <b>Весы на завтра {tomorrowdate}</b> {tomorrow}\n♎️ <b>Весы на послезавтра {tomorrowdate2}</b> {tomorrow2}',parse_mode='html')

    elif message.text == '♏️ Скорпион':
        horo = soup.find_all('scorpio')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id,f'🔯 <b>Гороскоп на сегодня</b>\n\n♏️ <b>Скорпион на {todaydate}</b> {today} \n♏️ <b>Скорпион на завтра {tomorrowdate}</b> {tomorrow}\n♏️ <b>Скорпион на послезавтра {tomorrowdate2}</b> {tomorrow2}',parse_mode='html')

    elif message.text == '♐️ Стрелец':
        horo = soup.find_all('sagittarius')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id,f'🔯 <b>Гороскоп на сегодня</b>\n\n♐️ <b>Стрелец на {todaydate}</b> {today} \n♐️ <b>Стрелец на завтра {tomorrowdate}</b> {tomorrow}\n♐️ <b>Стрелец на послезавтра {tomorrowdate2}</b> {tomorrow2}',parse_mode='html')

    elif message.text == '♑️ Козерог':
        horo = soup.find_all('capricorn')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id,f'🔯 <b>Гороскоп на сегодня</b>\n\n♑️ <b>Козерог на {todaydate}</b> {today} \n♑️ <b>Козерог на завтра {tomorrowdate}</b> {tomorrow}\n♑️ <b>Козерог на послезавтра {tomorrowdate2}</b> {tomorrow2}',parse_mode='html')

    elif message.text == '♒️ Водолей':
        horo = soup.find_all('aquarius')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id,f'🔯 <b>Гороскоп на сегодня</b>\n\n♒️ <b>Водолей на {todaydate}</b> {today} \n♒️ <b>Водолей на завтра {tomorrowdate}</b> {tomorrow}\n♒️ <b>Водолей на послезавтра {tomorrowdate2}</b> {tomorrow2}',parse_mode='html')

    elif message.text == '♓️ Рыбы':
        horo = soup.find_all('pisces')
        for item in horo:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        bot.send_message(message.from_user.id,f'🔯 <b>Гороскоп на сегодня</b>\n\n♓️ <b>Рыбы на {todaydate}</b> {today} \n♓️ <b>Рыбы на завтра {tomorrowdate}</b> {tomorrow}\n♓️ <b>Рыбы на послезавтра {tomorrowdate2}</b> {tomorrow2}',parse_mode='html')



    else:
        bot.send_message(message.from_user.id, 'Что-то пошло не так,  воспользуйтесь клавиатурой ниже')






@bot.message_handler(content_types=['photo', 'video', 'audio', 'document'])
def start(message):
    bot.send_message(message.chat.id, '😀 Спасибо за сообщение, но лучше воспользуйтесь клавиатурой ниже')







bot.polling(none_stop=True)
