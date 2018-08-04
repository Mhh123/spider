import time
import urllib.request

from bs4 import BeautifulSoup




def handler_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                      'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    return urllib.request.Request(url,headers=headers)


def get_text(href):
    request = handler_request(href)
    content = urllib.request.urlopen(request).read().decode(encoding='utf-8')
    soup = BeautifulSoup(content, 'lxml')
    odiv = soup.find('div', class_ = 'chapter_content')
    return odiv.text

def parse_hui(request, fp):
    content = urllib.request.urlopen(request).read().decode(encoding='utf-8')
    # 解析内容
    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    #获取所有的标题， 章节， 链接
    res = soup.select('.book-mulu > ul > li > a')
    # print(res)
    #[<a href="/book/sanguoyanyi/1.html">第一回·宴桃园豪杰三结义  斩黄巾英雄首立功</a>, ...]
    # print(len(res)) # 120

    for oa in res:
        title = oa.string
        print('*'*80)
        print('正在下载%s'% title)
        # 获取链接
        href = 'http://www.shicimingju.com' + oa['href']

        text = get_text(href)
        string = '%s\n%s' % (title, text)
        fp.write(string)
        print('结束下载%s' % title)
        print('-' * 80)
        time.sleep(2)

def main():
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    request = handler_request(url)

    # 打开文件
    fp = open('sanguo.html','w',encoding='utf-8')
    parse_hui(request, fp)
    fp.close()


if __name__ == '__main__':
    main()