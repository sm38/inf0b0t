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

def main():  
    query_text = {"www":"1", "kkk":"4", "bbb":"8"} 
    update_id = last_update(get_updates_json(url))['update_id']
    chat_id =  get_chat_id(last_update(get_updates_json(url)))
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           message_text = last_update(get_updates_json(url))['message']['text']
           if message_text == '*':
              send_answer_query(chat_id, query_text)
           elif message_text == '**':
              send_mess(chat_id, 'Answer from *inf0b0t*'+chr(10)+'as JSON on message #'+format(update_id) + ' : '+chr(10) + query_text )
           else :  
              send_mess(chat_id, 'Answer from *inf0b0t*'+chr(10)+'on message #'+format(update_id) + ' : '+chr(10) + message_text)
           update_id += 1
        sleep(1)       

if __name__ == '__main__':  
    main()