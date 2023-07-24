import schedule 
import telebot
from time import sleep
from threading import Thread






TOKEN = '6025323622:AAHAWeqAHWmiSUflt-0Od0C5s1jhodMNMO4'
bot = telebot.TeleBot(TOKEN)
some_id = 254073195

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    return bot.send_message(some_id, 'Сегодня не можем не порадовать вас скидкой 50% на отправку груза во Владивосток и Санкт-Петербург! Спешите, предложение ограничено!')
if __name__ == "__main__":
    schedule.every().day.at("07:15").do(function_to_run)
    Thread(target=schedule_checker).start() 




@bot.message_handler(content_types=['text'])
def text(message):
    chatId=message.chat.id
    text= message.text.lower ()
    print (text)
    if text == 'start':
        bot.send_message(message.chat.id, 'Доброго времени суток, Вы попали в телеграм бот транспортной компании Межанова Василия. Здесь будут анонсироваться все акции')

bot.polling()
    
    

