import requests

# 创建一个会话
s = requests.Session()
# 在往下所有的请求都使用s进行发送，就会自动携带cookie

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018611422744'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

data = {
    'email': '17701256561',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '95abcb2903c22a4246f26a43dd234c71e62a569f55a3463fd97dfede965a398e',
    'rkey': '5593c879e67fa248c7357ec9ad3ce8e6',
    'f': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dtmpx-K4dmSTbXIIhBudyANOUw-nlmFI1A9eZkPqy1B7%26wd%3D%26eqid%3De4ed4fb70000a886000000025b5eb451',
}

r = s.post(url=post_url, headers=headers, data=data)

get_url = 'http://www.renren.com/960481378/profile'

r = s.get(url=get_url, headers=headers)

print(r.text)

with open('pic/renren.html', 'w', encoding='utf-8') as fp:
    fp.write(r.text)
