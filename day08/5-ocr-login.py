import time
import urllib
import lxml
import requests
from lxml import etree
from shibie import sb

count = 0
while 1:
    #  创建一个会话
    s = requests.Session()

    #  将验证码下载到本地
    from bs4 import BeautifulSoup

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/67.0.3396.99 Safari/537.36',
    }
    get_url = 'https://so.gushiwen.org/user/login.aspx?from'

    ret = s.get(url=get_url, headers=headers)

    #  通过bs得到图片的src
    soup = BeautifulSoup(ret.text, 'lxml')
    img_src = 'https://so.gushiwen.org' + soup.find('img', id='imgCode')['src']
    #  将图片下载到本地
    r_img = s.get(img_src)

    with open('code.png', 'wb') as fp:
        fp.write(r_img.content)
    #  获取隐藏框的值
    __VIEWSTATE = soup.select('#__VIEWSTATE')[0]['value']
    __VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0]['value']
    # code = input('请输入验证码:')
    #  修改为zidongshibie
    code = sb('code.png')
    print(code)
    data = {
        '__VIEWSTATE': __VIEWSTATE,
        '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
        'from': '',
        'email': ' 905690216@qq.com',
        'pwd': ' qwe123',
        'code': code,
        'denglu': ' 登录',
    }

    post_url = 'https://so.gushiwen.org/user/login.aspx?from'

    res_post = s.post(url=post_url, headers=headers, data=data)

    with open('gushi.html', 'wb') as fp:
        fp.write(res_post.content)
    # print(res_post.text)
    count += 1
    print('第{}次尝试登陆'.format(count))
    if '退出登录' in res_post.text:

        break
    time.sleep(2)

