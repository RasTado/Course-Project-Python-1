import requests
import time
from progress.bar import IncrementalBar


class YaUploader:

    def __init__ (self, token_y):
        self.token_y = token_y
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'OAuth {}'.format(self.token_y)}

    def _create_directory(self, user):
        create_directory_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        requests.put(create_directory_url, headers = self.headers,
                     params = {'path': f'/netology'})
        requests.put(create_directory_url, headers = self.headers,
                     params = {'path': f'/netology/{user}'})

    def upload(self, user, result):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self._create_directory(user)
        bar = IncrementalBar('Countdown', max = len(result))
        for fotos in result:
            names = str(fotos[0])
            params = {'path': f'/netology/{user}/{names}',
                      'url': fotos[1]}
            requests.post(upload_url, headers = self.headers, params = params)
            bar.next()
            time.sleep(1)
        bar.finish()