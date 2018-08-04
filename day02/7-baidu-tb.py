import os
import time
import urllib.request
import urllib.parse

"""
    url_root: https://tieba.baidu.com/index.html?traceid=
    utl : https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=100
    n pn=(n-1)*50
    
"""

url = 'https://tieba.baidu.com/f'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                  'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}


def handler_request(url, page, b_name):
    # 拼接url
    pn = (page - 1) * 50
    data = {
        'kw': b_name,
        'ie': 'utf-8',
        'pn': pn,
    }
    # 处理data
    query_string = urllib.parse.urlencode(data)
    url += query_string
    print(url)
    request = urllib.request.Request(url, headers)
    request = urllib.request.Request(url=url, headers=headers)
    print(request)
    print(type(request))
    #<urllib.request.Request object at 0x0000000002AB3278>
    #<class 'urllib.request.Request'>
    return request


def download(request, b_name, page):
    response = urllib.request.urlopen(request)
    if not os.path.exists(b_name):
        # 根据吧名创建文件夹
        os.mkdir(b_name)

    # 保存文件中
    filename = '第%s页.html' % page
    filepath = os.path.join(b_name, filename)
    # 保存内容
    with open(filepath, 'wb') as fp:
        fp.write(response.read())


def main():
    b_name = input('请输入贴吧名:')
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束:'))

    for page in range(start_page, end_page + 1):
        print(type(page))
        print('正在爬取第%d页'% page)
        # 拼接url,生成请求对象的函数
        request = handler_request(url, page, b_name)
        download(request, b_name, page)
        print('已结束爬取第%d页'% page)
        time.sleep(3)


if __name__ == '__main__':
    main()
