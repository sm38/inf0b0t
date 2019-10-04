import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if message.text == 'ты попугай ?':
       ans_text = 'Да'
    else:
       ans_text = 'You typed: '+message.text    
    
    bot.send_message(message.chat.id, ans_text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
