import time
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup

"""
    输入工作地点
    输入关键字
    输入页码
"""


class ZzhiLianSpider(object):
    def __init__(self, jl, kw, start_page, end_page):
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page
        self.url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
        self.headers = headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                          'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        self.items = []

    def parse_content(self, content):
        soup = BeautifulSoup(content, 'lxml')
        table_list = soup.find_all('table', class_='newlist')[1:]
        print(len(table_list))
        for table in table_list:
            zwmc = table.select('.zwmc > div > a')[0].text
            gsmc = table.select('.gsmc > a')[0].text
            zwyx = table.select('.zwyx')[0].text
            gzdd = table.select('.gzdd')[0].text

            print(zwmc)
            # exit()
            item = {
                '职位名称': zwmc,
                '公司名称': gsmc,
                '职位月薪': zwyx,
                '工作地点': gzdd,
            }
            self.items.append(item)

    def run(self):
        # 循环， 拼接每一页的url，发送请求，获取响应
        for page in range(self.start_page, self.end_page + 1):
            print('正在爬取第%s页' % page, '*' * 50)
            request = self.handler_request(page)
            content = urllib.request.urlopen(request)
            self.parse_content(content)
            print('完成爬取第%s页' % page, '*' * 50)
            time.sleep(4)
        # 将列表写入文件中
        string = str(self.items)
        with open('work.txt', 'w', encoding='utf-8') as fp:
            fp.write(string)

    def handler_request(self, page):
        # 拼接url
        data = {
            'jl': self.jl,
            'kw': self.kw,
            'p': page,
        }
        data = urllib.parse.urlencode(data)
        # self.url +=data  # 会多次拼接
        url = self.url + data

        return urllib.request.Request(url, headers=self.headers)


def main():
    jl = input('请输入工作地点:')
    kw = input('请输入搜索关键字:')
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束页:'))

    zhilian = ZzhiLianSpider(jl, kw, start_page, end_page)
    zhilian.run()


if __name__ == '__main__':
    main()
