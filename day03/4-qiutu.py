import os
import re
import urllib.request
import urllib.parse


def handler_request(url, page):
    url = url.format(page)
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                      'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=headers)
    return request


def handler_content(request):
    print(0)
    response = urllib.request.urlopen(request)
    # 得到网页的字符串内容
    content = response.read().decode(encoding='utf-8')

    # 编译一个正则表达式对象
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt="(.*?)" />.*?</div>', re.S)
    res = pattern.findall(content)

    # res是一个列表，列表里面都是元组，元组的第一个元素是src，元组的第二个元素是al
    # with open('qiutu.html','wb') as fp:
    #     fp.write(str(res).strip('\n').encode(encoding='utf-8'))

    dirname = 'qiutu'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    # 下面做一个改进，不是写入html,img的scr；而是把图片下载下来
    for info in res:
        image_url = 'http:' + info[0]
        title = info[1]
        filename = title + '.' + image_url.split('.')[-1]
        print('正在下载%s' % filename, "*" * 40)
        # 得到图片路径
        filepath = os.path.join(dirname, filename)
        urllib.request.urlretrieve(image_url, filepath)
        print('结束下载%s' % filename, "*" * 40)


def main():
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束页:'))
    url = 'https://www.qiushibaike.com/pic/page/{}/'

    for page in range(start_page, end_page + 1):
        print('正在下载%s' % page, "*" * 40)
        # 拼接url,生成请求对象，并返回
        request = handler_request(url, page)
        # 发送请求，获得相应，解析内容
        handler_content(request)
        print('结束下载%s页' % page)


if __name__ == '__main__':
    main()
