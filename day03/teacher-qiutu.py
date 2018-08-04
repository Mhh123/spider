import urllib.request
import urllib.parse
import re
import os
import time


def main():
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    url = 'https://www.qiushibaike.com/pic/page/{}/'

    for page in range(start_page, end_page + 1):
        print('正在下载第%s页。。。。。。' % page)
        # 拼接url，生成请求对象，返回
        request = handle_request(url, page)
        # 发送请求，获得响应，解析内容
        handle_content(request)
        print('结束下载第%s页' % page)
        time.sleep(2)


def handle_content(request):
    print(0)
    response = urllib.request.urlopen(request)
    # 得到网页的字符串内容
    content = response.read().decode('utf8')
    # 先找到所有的这种div
    # pattern = re.compile(r'<div class="thumb">(.*?)</div>', re.S)
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt="(.*?)" />.*?</div>', re.S)

    ret = pattern.findall(content)
    # ret是一个列表，列表里面都是元组，元组的第一个元素是src，元组的第二个元素是alt
    # print(ret)
    print(1)

    dirname = 'qiutu'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    # 循环下载图片
    for info in ret:
        print(2)
        # 获取图片的src
        image_url = 'https:' + info[0]
        # 获取图片的标题
        title = info[1]

        # 拼接得到图片名字
        filename = title + '.' + image_url.split('.')[-1]
        print('正在下载%s...' % filename)
        # 得到图片路径
        filepath = os.path.join(dirname, filename)
        print(3)
        urllib.request.urlretrieve(image_url, filepath)
        print('结束下载%s' % filename)
        time.sleep(2)


def handle_request(url, page):
    url = url.format(page)
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


if __name__ == '__main__':
    main()
