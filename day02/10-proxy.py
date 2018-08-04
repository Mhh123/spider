import urllib.request

url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'

# 创建handler
handler = urllib.request.ProxyHandler(proxies={
    'http': '124.193.37.5:8888'
})
# 根据handler创建一个opener
opener = urllib.request.build_opener(handler)

response = opener.open(url)

with open('dali.html', 'wb') as fp:
    fp.write(response.read())
