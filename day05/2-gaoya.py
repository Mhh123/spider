import os
import time
import urllib.request
import urllib.parse

from lxml import etree


def main():
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    url = 'http://sc.chinaz.com/tupian/rentiyishu_{}.html'
    for page in range(start_page, end_page + 1):
        request = handler_request(url, page)
        content = urllib.request.urlopen(request).read().decode(encoding='utf-8')
        parse_content(content)


def handler_request(url, page):
    if page == 1:
        url = 'http://sc.chinaz.com/tupian/rentiyishu.html'
    else:
        url = url.format(page)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                      'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    return urllib.request.Request(url, headers=headers)


def parse_content(content):
    print(type(content))    #<class 'str'>
    tree = etree.HTML(content)
    print(tree) #<Element html at 0x2c82708>
    tree1 = etree.parse(content)
    print(tree1)
    exit()
    # //*[@id="container"]/div[18]/div/a/img
    img_urls = tree.xpath('//*[@id="container"]/div/div/a/img/@src2')
    img_names = tree.xpath('//*[@id="container"]/div/div/a/img/@alt')

    """
    使用zip方法将img_urls和img_names压缩为一个iterabl对象，
    再list()格式化为列表，里面是元组
    """
    img_datas = list(zip(img_urls, img_names))

    dirname = 'gaoya'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    # for img_url in img_urls:
    #
    #     filename = img_names[img_urls.index(img_url)]+'.'+img_url.split('.')[-1]
    #     print('正在下载%s' % filename, '*' * 40)
    #     filepath = os.path.join(dirname,filename)
    #     urllib.request.urlretrieve(img_url, filepath)
    #     print('结束下载%s'%filename,'*'*40)

    # 使用img_datas版本
    for img_data in img_datas:
        filename = img_data[1] + '.' + img_data[0].split('.')[-1]
        filepath = os.path.join(dirname, filename)
        print('正在下载%s' % filename, '*' * 40)
        urllib.request.urlretrieve(img_data[0], filepath)
        print('结束下载%s' % filename, '*' * 40)


if __name__ == '__main__':
    main()
