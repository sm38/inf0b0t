import telebot
import requests
from time import sleep

url = "https://api.telegram.org/bot902753904:AAHy0XRihb92qKe5HGDxmHChsuCGXw4r_Ic/"


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    parse_mode = 'Markdown'
    params = {'chat_id': chat, 'text': text, 'parse_mode': parse_mode}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def send_answer_query(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'answerInlineQuery', data=params)
    return response
    
def work_it(chat)
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


def main():  
    query_text = {"www":"1", "kkk":"4", "bbb":"8"} 
    update_id = last_update(get_updates_json(url))['update_id']
    chat_id =  get_chat_id(last_update(get_updates_json(url)))
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           message_text = last_update(get_updates_json(url))['message']['text']
           if message_text[:4] == 'WORK':
              do_work(chat_id);
           elif message_text == '456':
              send_mess(chat_id, 'Answer from *inf0b0t*'+chr(10)+'as JSON on message #'+format(update_id) + ' : '+chr(10) + query_text )
           elif message_text == '789':
              send_mess(chat_id, 'Answer from *inf0b0t*'+chr(10)+'on message #'+format(update_id) + ' : '+chr(10) + 'three-star cognak - good chioce !' )
           else :  
              send_mess(chat_id, 'Answer from *inf0b0t*'+chr(10)+'on message #'+format(update_id) + ' : '+chr(10) + message_text)
           update_id += 1
        sleep(1)       

if __name__ == '__main__':  
    main()