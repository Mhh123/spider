import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.baidu.com/'

#  如果不伪装，那么通过ua头部就暴露自己是爬虫程序，所以需要伪装ua
# response = urllib.request.urlopen(url)

# 伪装就是自己定制头部
# 将想定制的头部全部写到这里
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)
# 发送请求，获取响应
response = urllib.request.urlopen(request)