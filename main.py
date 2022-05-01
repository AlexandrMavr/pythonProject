import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file: str, file: str):
        """Метод загружает файл на яндекс диск"""
        res = requests.get(f'{URL}/upload?path={file}', headers=headers).json()
        with open(path_to_file, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
            except KeyError:
                pprint(res)

if __name__ == '__main__':
    # Получить путь к загружаемому файлу, имя файла, токен
    path_to_file = r'...'
    file = '...'
    token = '...'
    URL = 'https://cloud-api.yandex.net/v1/disk/resources' #постоянный URL
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, file)
