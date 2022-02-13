import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'ZWJkODFkZDktNjcyMi00OTA1LWJlNTctNGZhOTFjYjJkODcyOjBkOWViMDQ3OGMzMDQ5NmZiMDVhY2RkOGE3N2M3M2Yz'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    pass
    token = auth.text

    while True:
        word_to_translate = input('Введите слово для перевода: ')
        if word_to_translate:
            headers_translate = {'Authorization': 'Bearer ' + token}
            params_lingvo = {
                'text': word_to_translate,
                'srcLang': 1033,
                'dstLang': 1049
            }
            request_lingvo = requests.get(URL_TRANSLATE, headers=headers_translate, params=params_lingvo)

            response_lingvo = request_lingvo.json()
            try:
                print(response_lingvo['Translation']['Translation'])
            except:
                print('Не найдено вариантов для перевода')
else:
    print('Error!')
