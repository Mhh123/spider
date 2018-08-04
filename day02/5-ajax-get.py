import urllib.request
import urllib.parse

get_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
#start=0&limit=1
print('每页显示10部电影')
page = input('请输入第几页:')
start = (int(page)-1)*10
limit = 10

data = {
    'start':start,
    'limit':limit,
}

# 处理data
data = urllib.parse.urlencode(data)
get_url += data
print(get_url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                  'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

request = urllib.request.Request(get_url, headers=headers)
response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
