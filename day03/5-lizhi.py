import time
import urllib.request
import urllib.parse
import re

"""

url 管理器 已爬(old_url)  待爬(新加url) 
url 下载器 urllib.request 
url 解析器 正则


小状况:download下来的html,需要加声明 <meta charset="UTF-8">

"""


def main():
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_{}.html'
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束页:'))
    # 打开文件
    fp = open('lizhi.html', 'w', encoding='utf-8')
    for page in range(start_page, end_page + 1):
        request = handler_request(url, page)
        handler_content(request, fp)
        time.sleep(2)
    fp.close()


def handler_request(url, page):
    url = url.format(page)
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                      'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    return urllib.request.Request(url, headers=headers)


def handler_content(request, fp):
    # 发送请求，获取响应
    content = urllib.request.urlopen(request).read().decode(encoding='utf-8')
    print('-' * 80)
    pattern = re.compile(r'<div class="art-t">.*?<a href="(.*?)">(.*?)</a>.*?</div>', re.S)
    res = pattern.findall(content)

    for info in res:
        # 获取内容链接
        href = 'http://www.yikexun.cn' + info[0]

        # 获取title
        title = info[1].strip('</b>')

        # 向href发送请求，获取内容
        text = get_text(href)

        string = '<h1>%s</h1>\n%s' % (title, text)

        # 将字符串写入文件中
        fp.write(string)
        exit()
        time.sleep(1)


def get_text(href):
    # 发送请求，获取响应
    request = handler_request(href, None)
    content = urllib.request.urlopen(request).read().decode(encoding='utf-8')
    pattern = re.compile(r'<div class="neirong">(.*?)</div>', re.S)
    res = pattern.search(content)

    text = res.group(1)
    # 将里面所有的图片标签干掉
    pattern = re.compile(r'<img .*?/>')
    text = pattern.sub('', text)

    return text


if __name__ == '__main__':
    main()
