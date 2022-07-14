from pprint import pprint
from YandexDisc import YaUploader
from VkApi import VKUser
import json
import configparser


if __name__ == '__main__':
    user = input('Укажите имя пользователя или id, чьи фотографии необходимо сохранить в облаке: ')
    quantity = input('Укажите количество фотографий для сохранения\или оставьте пусто, что-бы сохранить все фотографии: ')
    if quantity == '':
        quantity = None
    else:
        quantity = int(quantity)
    config = configparser.ConfigParser()
    config.read('setting.ini')
    VkUser = VKUser(config['VK']['vk_token'], config['VK']['version_vk'])
    result = VkUser.get_fotos(user, quantity)
    json_file = []
    for res in result:
        json_file.append({"file_name": res[0], "size": res[3]})
    with open ('result.json', 'w') as data:
        json.dump(json_file, data)
    YaUser = YaUploader(config['Yandex']['yandex_token'])
    YaUser.upload(user, result)