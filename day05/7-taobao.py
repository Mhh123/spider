import time
import urllib.request
import json
import jsonpath

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                  'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}


def handler_request(url, page):
    url = url.format(page)
    return urllib.request.Request(url, headers=headers)


def parse_content(content):
    # 对内容进行处理，并转换为类dict的字符串后再loads转成python对象
    obj = json.loads(content.strip('()\n\t\r'))
    comments = obj['comments']

    items = []
    for comment in comments:
        # 获取头像
        # face = comment['user']['avatar']

        # 使用jsonpath语法
        face = jsonpath.jsonpath(comment, '$..avatar')[0]
        # 评论内容
        com = comment['content']
        # 获取手机信息
        info = jsonpath.jsonpath(comment, '$..sku')[0]
        item = {
            '头像': face,
            '评论': com,
            '手机信息': info
        }

        items.append(item)
    return items


def main():
    url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId=559141739630&userNumId=100340983&currentPageNum={}&pageSize=20'
    for page in range(1, 2):
        request = handler_request(url, page)
        content = urllib.request.urlopen(request).read().decode(encoding='utf-8')
        items = parse_content(content)

        with open('taobao.txt', 'w', encoding='utf-8') as fp:
            fp.write(str(items))


if __name__ == '__main__':
    main()
