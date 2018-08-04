import urllib.request
import urllib.parse

# 让代码保存cookie
import http.cookiejar
#创建一个cookiejar对象，用来保存cookie
ck =http.cookiejar.CookieJar()
# 根据cookiejar对象创建一个handler
handler = urllib.request.HTTPCookieProcessor(cookiejar=ck)
#根据handler创建opener
opener = urllib.request.build_opener(handler)
#  再往下所有的请求都还自动携带cookie

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201863939363'

#
# GET /click?J={%22ID%22:%22967106461%22,%22R%22:%22http%3A%2F%2Fzhibo.renren.com%2Ftop%22,%22X%22:143,%22Y%22:171,%22T%22:%22div%22,%22U%22:%22http%3A%2F%2Fwww.renren.com%2F967106461%2Fprofile%22}&t=0.9133371330395754 HTTP/1.1
# Host: dj.renren.com
# Connection: keep-alive
# Accept: image/webp,image/apng,image/*,*/*;q=0.8
# Referer: http://zhibo.renren.com/top
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9
# Cookie: ick_login=ad45689c-cf1d-4efa-a180-77f582a76fde; anonymid=jk0gqq8e-imjv31; depovince=GW; _r01_=1; t=cd2c32b6ce84ca471e86d8bd7e3289751; societyguester=cd2c32b6ce84ca471e86d8bd7e3289751; id=967106461; xnsid=30e67207; jebe_key=94d9a879-e473-48cf-ab68-65d3aff55c19%7C24b3d26b79ad6218bede6cd1942ce9e9%7C1532482922946%7C1%7C1532482928665; wp_fold=0; jebecookies=c9f4cb42-ddfb-4084-a1b8-9d965b7c84aa|||||; BAIDU_SSP_lcr=https://www.baidu.com/link?url=-OYKJOIkDLaLLW589YQXfVIob_i5LglCSpimboybaYe&wd=&eqid=87abad1a00003d64000000025b57d548

data = {
	'email': '17701256561',
	'icode': '',
	'origURL': 'http://www.renren.com/home',
	'domain': 'renren.com',
	'key_id': '1',
	'captcha_type': 'web_login',
	'password': '0bdc7ba2630974173cbcb1826900c0c825c7038f080dfb6e56ee99803bb42838',
	'rkey': '53124c1cc5654274b0e65ffe6496fca3',
	'f': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D7syJAUxc0l0zHsfVcgmHmIV98Ow_meJbTZt-kIQAPDu%26wd%3D%26eqid%3Deb9afdb800004268000000025b57d536',
}

data = urllib.parse.urlencode(data).encode(encoding='utf-8')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
}

request = urllib.request.Request(url=post_url, headers=headers)
# response = urllib.request.urlopen(request)
response = opener.open(request,data=data)

print(response.read().decode(encoding='utf-8'))
#{"code":true,"homeUrl":"http://www.renren.com/home"}

#____________________________________
#  登陆成功之后，向这个url发送请求
#___________________________________
get_url = 'http://www.renren.com/960481378/profile'
request_1 = urllib.request.Request(url=get_url,headers=headers)
response_1 = opener.open(request_1)

with open('renren_1.html','wb') as fp:
    fp.write(response_1.read())