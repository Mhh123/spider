import urllib.request
import urllib.parse

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

cname = input('亲输入要查的城市:')

data = {
    'cname':cname,
    'pid':'',
    'pageIndex':'1',
    'pageSize':'10',
}


#处理data
data = urllib.parse.urlencode(data).encode('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                  'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

request = urllib.request.Request(post_url, headers=headers)
response = urllib.request.urlopen(request,data=data)


print(response.read().decode('utf8'))
