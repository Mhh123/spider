import urllib.request
import urllib.parse

post_url = 'http://fanyi.baidu.com/sug'
word = input('请输入您要查询到单词')
data = {
    'kw': word,
}

#  对表单数据进行处理，先转化为字符串，再转化为字节格式
data = urllib.parse.urlencode(data).encode('utf8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                  'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

request = urllib.request.Request(post_url, headers=headers)
response = urllib.request.urlopen(request, data=data)

print(response.read().decode('utf8'))
