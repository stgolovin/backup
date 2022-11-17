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
        return response.json()

access_token = 'vk1.a.DJVUVP8utyToTH3vMKR1Y0FBD5l7-2i1mEWj9olxkOCom4-' \
               'LSLgsQPiGp5L9EGM_utzKUfnziyJ2BKVqBlgRy86mkUWMeqjs2ENDRdp' \
               'Weubvc5wkpvjCdR37sH8gXbb1shJ5caBpjNmxZJ0zSfDQjYz5y2aAOsEL' \
               '9MukougnJUksxhxOz-r2Zkl87AW3wa7Y3TZtqA4PkAHDyFBWkxldNg'
user_id = '51476467'
vk = VK(access_token, user_id)
# data = vk.users_info()


if __name__ == '__main__':
    pprint(vk.users_info())

