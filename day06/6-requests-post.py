import requests

url = 'https://cn.bing.com/ttranslationlookup?&IG=E0F1F1D960024878BE36B9BF24010AE6&IID=translator.5036.2'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                  'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
formdata = {
    'from': 'zh-CHS',
    'to': 'en',
    'text': '小美女'
}

r = requests.post(url=url, headers=headers, data=formdata)
print(r.text)
# {"normalizedSource":"小美女","displaySource":"小美女","translations":[]}
print(r.content)
# b'{"normalizedSource":"\xe5\xb0\x8f\xe7\xbe\x8e\xe5\xa5\xb3","displaySource":"\xe5\xb0\x8f\xe7\xbe\x8e\xe5\xa5\xb3","translations":[]}'
with open('pic/biying-translate.html', 'w', encoding='utf-8') as fp:
    fp.write(r.text)
