import json
import threading
import time
from queue import Queue

import requests
from bs4 import BeautifulSoup
from lxml import etree


class CrawlThread(threading.Thread):
    def __init__(self, name, page_queue, data_queue):
        super(CrawlThread, self).__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/duanzi-{}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/67.0.3396.99 Safari/537.36',
                        }

    def run(self):
        print('生成线程--{}--启动'.format(self.name))
        #  采集线程的代码写到这里
        """
        1  出队一个页码
        2  拼接url
        3  发送请求，获取响应
        4  添加响应到数据队列
        """
        while 1:
            try:
                page = self.page_queue.get(False)
                # print('self.page_queue size is {}'.format(self.page_queue.qsize()))
                url = self.url.format(page)

                #  下载器下载html文档，（本质是字符串）
                r = requests.get(url=url, headers=self.headers)

                self.data_queue.put(r.text)

            except Exception as e:
                continue
            finally:
                if self.page_queue.empty():
                    break

        print('生成线程--{}--结束'.format(self.name))


class ParseThread(threading.Thread):
    def __init__(self, name, page_queue, data_queue, fp, lock):
        super(ParseThread, self).__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.fp = fp
        self.lock = lock

    def run(self):
        print('解析线程--{}--启动'.format(self.name))

        """
        1  从data队列出队一个数据
        2  解析数据
        3  保存文件中
        """
        while 1:
            try:

                content = self.data_queue.get(True, 3)
                self.parse_content(content)
            except Exception as e:
                continue
            finally:
                if self.page_queue.empty() and self.data_queue.empty():
                    break

        print("解析线程--{}--结束".format(self.name))

    def parse_content(self, content):
        """
        使用xml生成tree对象
        解析字典
        每一页一个列表，列表中都是字典
        将列表保存到文件中
        :return:
        """
        tree = etree.HTML(content)
        html_con = tree.xpath('//li[@class="cont-item"]/div[@class="cont-list-main"]/p[1]/text()')
        html_con = json.dumps(html_con, ensure_ascii=False)
        # print(html_con)
        print(type(html_con))
        self.lock.acquire()  # acquire,acquire,acquire
        self.fp.write('<p>{}</p>'.format(html_con))
        self.fp.write('\n'*2)
        self.lock.release()
        time.sleep(2)  # 防止被封，睡2秒


def create_queue():
    """
    创建两个队列，并且向页码队列提那家爬取的页码
    :return:  page_queue,data_queue
    """
    page_queue = Queue()
    data_queue = Queue()
    for page in range(1, 10):
        page_queue.put(page)
    return page_queue, data_queue


def main():
    # 打开文件
    fp = open('duoshuo.html', 'w', encoding='utf-8')
    fp.write('<meta charset="UTF-8">'+'\n')  # 是问了方便，直接声明类型
    lock = threading.Lock()

    #  创建队列函数
    page_queue, data_queue = create_queue()

    #  创建生成线程
    craw_name_list = ['craw_one', 'craw_two', 'craw_three']
    thread_list = []  # 这个线程列表里面存了6个子线程，3个生成线程，3个解析线程
    for crawl_name in craw_name_list:
        t_crawl = CrawlThread(crawl_name, page_queue, data_queue)
        t_crawl.start()
        thread_list.append(t_crawl)

    #  创建解析线程
    parse_name_list = ['parse_one', 'parse_two', 'parse_three']

    for parse_name in parse_name_list:
        t_parse = ParseThread(parse_name, page_queue, data_queue, fp, lock)
        t_parse.start()
        thread_list.append(t_parse)

    # 让主线程等待子线程结束
    for t in thread_list:
        t.join()

    fp.close()

    #  结束
    print('主线程，子线程全部结束')


if __name__ == '__main__':
    main()
