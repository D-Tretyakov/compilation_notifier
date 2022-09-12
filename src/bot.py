import requests

class Bot:
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
        self.url = f'https://api.telegram.org/bot{self.token}'

    def get_update(self):
        req = requests.post(f'{self.url}/getUpdates')
        parsed = req.json()
        print(parsed)

    def notify(self):
        params = {'chat_id': self.user_id, 'text': 'Build finished!'}
        req = requests.post(f'{self.url}/sendMessage', params=params)
        parsed = req.json()
        print(parsed)
