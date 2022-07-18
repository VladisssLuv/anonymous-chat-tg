import telebot
from botDB import DataBaseBot
from config import TOKKEN

bot = telebot.TeleBot(TOKKEN)
base = DataBaseBot()

@bot.message_handler(commands=['start'])
def start_message(m):
    bot.send_message(m.chat.id, "Я анонимный чат бот\nчтобы найти собеседника используй команду /find\nПриятого общения")
    if(base.get_status(m.chat.id) == None):
        base.add(m.chat.id, False, False, 0)

@bot.message_handler(commands=['find'])
def start_dialog(m):
    bot.send_message(m.chat.id, "идёт поиск собеседника...")
    companion_id = base.find_dialog()
    if companion_id == None:
        base.set_status(m.chat.id, True)
        base.set_in_dialog(m.chat.id, False)
    else:
        base.set_status(companion_id, False)
        base.set_in_dialog(m.chat.id, True)
        base.set_in_dialog(companion_id, True)
        base.set_id_companion(m.chat.id, companion_id)
        base.set_id_companion(companion_id, m.chat.id)

        mess = "собеседний найден\n /stop - прервать общение"
        bot.send_message(m.chat.id, mess)
        bot.send_message(companion_id, mess)
       

@bot.message_handler(commands=['stop'], func=lambda m: base.get_in_dialog(m.chat.id) == True)
def stop_dialog(m):
    companion_id = base.get_id_companion(m.chat.id)
    base.set_id_companion(m.chat.id, 0)
    base.set_id_companion(companion_id, 0)
    base.set_status(m.chat.id, False)
    base.set_status(companion_id, False)
    base.set_in_dialog(m.chat.id, False)
    base.set_in_dialog(companion_id, False)

    mess = "общение прервано\n /find - поиск нового"
    bot.send_message(m.chat.id, mess)
    bot.send_message(companion_id, mess)

@bot.message_handler(content_types=['text'], func=lambda m: base.get_in_dialog(m.chat.id) == False)
def mess(m):
    if base.get_status(m.chat.id) == True:
        bot.send_message(m.chat.id, "всё ещё ищем собеседника...")
    else:
        bot.send_message(m.chat.id, "чтобы начать поиска собеседнийка используйте команду /find")

@bot.message_handler(content_types=['text'], func=lambda m: base.get_status(m.chat.id) == False and base.get_in_dialog(m.chat.id) == True)
def dialog(m):
    bot.send_message(base.get_id_companion(m.chat.id), m.text)

bot.polling()