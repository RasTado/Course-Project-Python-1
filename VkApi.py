import requests
import datetime


class VKUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token_v, version='5.131'):
        self.params = {'access_token': token_v,
                       'v': version}

    def users_get(self, user_id=None):
        users_get_url = self.url + 'users.get'
        users_get_params = {'user_ids': user_id,
                            'fields': 'education,sex'}
        req_users_get = requests.get(users_get_url,
                                     params = self.params | users_get_params).json()
        return req_users_get['response'][0]['id']

    def get_fotos(self, user=None, count=None):
        get_fotos_url = self.url + 'photos.get'
        get_fotos_param = {'owner_id': self.users_get(user),
                           'album_id': 'profile',
                           'extended': '1',
                           'rev': '1',
                           'count': count}
        req_get_fotos = requests.get(get_fotos_url,
                                     params = self.params | get_fotos_param).json()
        dict_fotos = []
        likes_dict = []
        for data_vk_fotos in req_get_fotos['response']['items']:
            name_likes_foto = data_vk_fotos['likes']['count']
            name_date_foto = str(datetime.datetime.fromtimestamp(data_vk_fotos['date']).strftime('%Y-%m-%d'))
            max_size = 0
            for n, fotos_size in enumerate(data_vk_fotos['sizes']):
                size = fotos_size['width'] * fotos_size['height']
                if fotos_size['width'] * fotos_size['height'] > max_size:
                    max_size = fotos_size['width'] * fotos_size['height']
                    max_size_place = n
            url_largest_foto = data_vk_fotos['sizes'][max_size_place]['url']
            url_largest_foto_type = data_vk_fotos['sizes'][max_size_place]['type']
            if name_likes_foto not in likes_dict:
                dict_foto = name_likes_foto, url_largest_foto, url_largest_foto_type
                dict_fotos.append(dict_foto)
                likes_dict.append(name_likes_foto)
            else:
                dict_foto = f'{name_likes_foto} {name_date_foto}', url_largest_foto, url_largest_foto_type
                dict_fotos.append(dict_foto)
        return dict_fotos