from pprint import pprint
from YandexDisc import YaUploader
from Vk import VKUser
import json

token_vk = ''
token_yd = ''
User_id = '552934290'
quantity = 5

VkUser = VKUser(token_vk)
result = VkUser.get_fotos(User_id, quantity)
json_file = []
for res in result:
    json_file.append({"file_name": res[0], "size": res[3]})
with open ('result.json', 'w') as data:
    json.dump(json_file, data)

YaUser = YaUploader(token_yd)
YaUser.upload(User_id, result)