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
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           message_text = last_update(get_updates_json(url))['message']['text']
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'Answer from inf0b0t on message #'+format(update_id) + ' : ' + message_text)
           update_id += 1
        sleep(1)       

if __name__ == '__main__':  
    main()