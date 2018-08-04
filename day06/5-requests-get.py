import requests

# url = 'http://www.baidu.com'

#  定制请求头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
"""
r = requests.get(url=url, headers=headers)

#  修改字符集
r.encoding = 'utf-8'

#  获取响应字符串内容
# print(r.text)
print(r.headers)
print(r.url)
print(r.status_code)
"""

# url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=丑女'
url = 'https://www.baidu.com/s?'

data = {
    'ie': 'utf-8',
    'wd': '丑女'
}

r = requests.get(url=url, headers=headers, params=data)
# print(r.text)
print(r.content)
with open('pic/chounv.html', 'wb') as fp:
    fp.write(r.content)
