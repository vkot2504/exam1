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
    return bot.send_message(some_id, "Вот уже и утро наступило! Не правда ли?! Пора выбрать котика, умоляющего поставить мне пятерочку за экзамен. Жду в ответ цифру от 0-5. P.S.-интереснее присылать цифры по порядку. Но Вы просили пользователю дать возможность выбрать котиков.")

if __name__ == "__main__":
    schedule.every().day.at("09:00").do(function_to_run)
    
Thread(target=schedule_checker).start() 
   


    

@bot.message_handler(content_types=['text'])
def text(message):
    chatId=message.chat.id
    text= message.text.lower ()
    print (text)
    if text == 'start':
        bot.send_message(message.chat.id, '11Доброго времени суток, Карим Аммарович! Вы попали в бот Вашего студента- Межанова Василия. Каждый день в определенное время (я выставил 9 часов утра) бот будет спрашивать у Вас, какого котика Вы хотите увидеть сегодня. Котиков я сделал не так много, все же тут актуальнее именно механизм бота. P.S. Фотография котика на аватарке бота взята из открытого источника.')
    elif text == '1':
        p= open('1.png', 'rb')
        bot.send_photo(message.chat.id,p)
    elif text == '2':
        p= open('2.png', 'rb')
        bot.send_photo(message.chat.id,p)
    elif text == '3':
        p= open('3.png', 'rb')
        bot.send_photo(message.chat.id,p)
    elif text == '4':
        p= open('4.png', 'rb')
        bot.send_photo(message.chat.id,p)
    elif text == '5':
        p= open('5.png', 'rb')
        bot.send_photo(message.chat.id,p)

    

        
    
    





bot.polling(none_stop=True)