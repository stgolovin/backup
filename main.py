import json

import requests
from pprint import pprint


class VK():
    
    def __init__(self, access_token, user_id, version='5.131' ):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'users_id': self.id, 'album_id': 'profile', 'extended': 1}
        response = requests.get(url, params={**self.params, **params})
        data = response.json()
        vk.edit_photo(data)
        # vk.write_to_json(data)
        # vk.download_photo_by_url()
        return data

    def write_to_json(self, data):
        filename = 'photo_list'
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def download_photo_by_url(self):
        url = 'https://sun9-16.userapi.com/c10095/u15018025/-6/y_223e687b.jpg'
        r = requests.get(url)
        if r.status_code == 200:
            with open('image.png', 'wb') as f:
                for chunk in r:
                    f.write(chunk)

    def edit_photo(self, data):
        super_dict = {}
        for chunk in data['response']['items']:
            pass
            # pprint(chunk['sizes'][-1])
            # pprint(chunk)
        pprint(data['response']['items'][0])

        




access_token = 'vk1.a.DJVUVP8utyToTH3vMKR1Y0FBD5l7-2i1mEWj9olxkOCom4-' \
               'LSLgsQPiGp5L9EGM_utzKUfnziyJ2BKVqBlgRy86mkUWMeqjs2ENDRdp' \
               'Weubvc5wkpvjCdR37sH8gXbb1shJ5caBpjNmxZJ0zSfDQjYz5y2aAOsEL' \
               '9MukougnJUksxhxOz-r2Zkl87AW3wa7Y3TZtqA4PkAHDyFBWkxldNg'
user_id = '51476467'
vk = VK(access_token, user_id)

if __name__ == '__main__':
    vk.users_info()
