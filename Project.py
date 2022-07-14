from YandexDisc import YaUploader
from VkApi import VKUser
import json
import configparser


def main():
    while True:
        command = input('e - выгрузить фотографии на Яндекс.Диск'
                        '\nq - выйти \nВведите команду: ')
        if command == 'e':
            download_fotos_vk_to_ya()
        elif command == 'q':
            print('exit')
            break

def download_fotos_vk_to_ya():
    config = configparser.ConfigParser()
    config.read('setting.ini')
    VkUser = VKUser(config['VK']['vk_token'], config['VK']['version_vk'])
    input_user = input('Укажите имя пользователя или id, '
                 'чьи фотографии необходимо сохранить на Яндекс.Диск: ')
    try:
        target_user = VkUser.users_get(input_user)
        user_name = target_user["first_name"] + ' ' + target_user["last_name"]
    except:
        print('Нет такого пользователя')
        return
    quantity = input(f'Укажите количество фотографий пользователя {user_name} '
                     f'для сохранения\или любой символ, что-бы сохранить все фотографии: ')
    try:
        quantity = int(quantity)
    except:
        quantity = None
    result = VkUser.get_fotos(target_user['id'], quantity)
    json_file = []
    for res in result:
        json_file.append({"file_name": res[0], "size": res[2]})
    with open ('result.json', 'w') as data:
        json.dump(json_file, data)
    YaUser = YaUploader(config['Yandex']['yandex_token'])
    YaUser.upload(user_name, result)

if __name__ == '__main__':
    main()