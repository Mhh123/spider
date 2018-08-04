import requests

lis = [
    {'http': '124.193.37.5:8888'},
    {'http': '218.60.8.83:3129'},
    {'http': '221.228.17.172:8181'},
    {'http': '113.200.56.13:8010'},
    {'http': '114.113.126.87:80'},
    {'http': '182.110.12.145:31773'},
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'

while len(lis):
    try:
        proxy = lis.pop()
        r = requests.get(url=url, headers=headers, proxies=proxy)
        break
    except Exception as e:
        print(e)

print(r.content)

with open('pic/daili1.html', 'wb') as fp:
    fp.write(r.content)

#  打开daili.html
#  页面显示  本机IP: 113.200.56.1陕西省西安市 联通
#  证明使用了代理，访问；因为本地ip是北京是联通
