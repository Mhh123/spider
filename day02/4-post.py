import urllib.request
import urllib.parse

post_url = 'http://fanyi.baidu.com/v2transapi'

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'baby',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '814534.560887',
    'token': '7518ccf005e3eeba364707e08b4e1140',
}

# 处理data
data = urllib.parse.urlencode(data).encode('utf-8')
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
#                   'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
# }
headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '121',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=F90666F891F9ABFE46063DF4FADA3DB8; BAIDUID=5E61BD0A9ED524DED47ECEC1B349A591:FG=1; PSTM=1532328315; pgv_pvi=5610460160; PSINO=2; BDRCVFR[auK81cz0o7_]=mk3SLVN4HKm; H_PS_PSSID=1450_26908_21097_20719; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1532397315; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1532397315; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
    'Host': 'fanyi.baidu.com',
    'Origin': 'http://fanyi.baidu.com',
    'Referer': 'http://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
request = urllib.request.Request(url=post_url, headers=headers)
response = urllib.request.urlopen(request, data)

print(response.read().decode('utf8'))
