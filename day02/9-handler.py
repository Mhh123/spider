import urllib.request

url = 'http://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                  'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

#  首先创建一个handler
handler = urllib.request.HTTPHandler()
#  通过handelr创建一个opener
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(url=url, headers=headers)

response = opener.open(request)

print(response.read().decode(encoding='utf-8'))
