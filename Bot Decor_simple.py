from requests import *
import re
from telebot import *
from telebot.types import (
InlineKeyboardMarkup as Mk ,
InlineKeyboardButton as btn)
bot = TeleBot(input("5911061931:AAGSgzXHr6mDMLzle0vdxRE_ksr5BJmD87M : "))
dev = Mk().add(btn(text='• Developer •',url='t.me/DevNoxi'))
@bot.message_handler(commands=['start'])
def start(msg):
	bot.send_message(msg.chat.id,'''• اهلا بك 
في بوت الزخرفة ؛)
- قم بأرسال اسمك بـ اللغة العربي او الانجليزي !''',reply_markup=dev)
@bot.message_handler(content_types=['text'])
def main(msg):
	ii = 0;text = msg.text
	try:
		res = get(f"http://xn--ogbjjc1f.com/inc/php/fancy-fonts.php?q={text}").text
		for i in range(22):
			ii += 1
			x = re.findall(f'input type="text" class="ResultName" id="username{ii}" value="(.*?)" readonly',res)
			if x == []:pass
			else:
				bot.send_message(msg.chat.id,f'`{x[0]}`',
				parse_mode='Markdown')
		bot.reply_to(msg,f"""- تم زخرفة الإسم {text} .
- أرسل أسم أخر للزخرفة ..""",
		reply_markup=dev)
#			print(x[0])
	except:pass
bot.infinity_polling()
