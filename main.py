import json

import requests
import random
from time import time, sleep


class FiveSms:
    def __init__(self, token):
        self.api_key = token
        self.country = ['russia', 'ukraine', 'belarus', 'kazakhstan']
        self.operator = 'any'
        self.service = 'telegram'
        self.phone = None
        self.id = None
        self.head = {
            'Authorization': 'Bearer ' + self.api_key,
            'Accept': 'application/json',
        }

    def get_phone(self):
        if float(self.balance()) < 20.0:
            print('Недосточно средств.')
            return False

        for country in self.country:
            response = requests.get(
                'https://5sim.net/v1/user/buy/activation/' + country + '/' + self.operator + '/' + self.service,
                headers=self.head)
            try:
                response = json.loads(response.text)
            except:
                continue

            if 'phone' in response and 'id' in response:
                break
        else:
            return False

        self.phone = response['phone']
        self.id = int(response['id'])
        print(phone)
        return self.phone

    def set_status(self, status=False):
        if status:
            requests.get('https://5sim.net/v1/user/finish/' + str(self.id), headers=self.head)

        elif not status:
            requests.get('https://5sim.net/v1/user/ban/' + str(self.id), headers=self.head)

        else:
            return False

        return True

    def get_code(self, timeout=120):
        start = time()
        while True:
            response = requests.get('https://5sim.net/v1/user/check/' + str(self.id), headers=self.head)
            try:
                response = json.loads(response.text)
            except:
                continue

            if response['sms']:
                code = response['sms']['code']
                self.set_status(status=True)
                print(code)
                return code

            if time() - start > timeout:
                self.set_status(status=False)
                return False
            sleep(1)

    def balance(self):
        response = requests.get('https://5sim.net/v1/user/profile', headers=self.head)
        try:
            json.loads(response.text)['balance']
        except:
            return 0
        return float(json.loads(response.text)['balance'])


if __name__ == '__main__':
    api = FiveSms('YOUR API KEY')
    api.balance()
    phone = api.get_phone()
    if phone:
        code = api.get_code()
    else:
        print('No free phone.')
