from time import sleep

from enotify.config import Config

import requests


class Bot:
    def __init__(self):
        data = Config.read()
        self.token = data['token']
        self.user_id = data['user_id']
        
        if self.token is None:
            raise RuntimeError('No bot token was specified! Use -t flag!')
        
        self.url = f'https://api.telegram.org/bot{self.token}'
        self.timeout = 10

    def get_user_id(self, username):      
        for _ in range(self.timeout):
            response = requests.get(f'{self.url}/getUpdates')
            parsed = response.json()
            if not self.response_ok(parsed):
                return

            for entry in parsed['result']:
                data = entry['message']['from']
                if data['username'] == username:
                    user_id = data['id']
                    
                    return str(user_id)

            sleep(1)

    def notify(self):
        if self.user_id is None:
            raise RuntimeError('No user id was specified! Use -i or -g flag!')

        params = {'chat_id': self.user_id, 'text': 'Build finished!'}
        response = requests.post(f'{self.url}/sendMessage', params=params)
        parsed = response.json()
        if not self.response_ok(parsed):
            return

    def response_ok(self, parsed):
        status_ok = parsed['ok']
        if not status_ok:
            print('Error from Telegram API')
            print(f'error_code: {parsed["error_code"]}')
            print(f'description: {parsed["description"]}')

            return False

        return True