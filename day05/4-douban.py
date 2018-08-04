import json
import time
import urllib.request
import urllib.parse

"""
url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                  'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
with open('douban.html', 'wb') as fp:
    fp.write(response.read())
"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebkit/537.36 ('
                  'KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}


def handler_request(url, page):
    start = (page -1)*20
    limit = 20
    data = {
        'page_limit': limit,
        'page_start':start,
    }
    query_string = urllib.parse.urlencode(data)
    url = url + query_string
    return urllib.request.Request(url, headers=headers)


def parse_content(content):
    items = []
    movie_list = json.loads(content)['subjects']

    for movie in movie_list:

        haibao = movie['cover']
        name = movie['title']
        # actor = movie['actors']
        score = movie['rate']
        count = movie['cover_y']
        item = {
            '海报':haibao,
            '名称':name,
            # '演员':actor,
            '评分':score,
            '人数':count,
        }
        items.append(item)
    return items
def main():
    start_page = int(input('请输入起始页码:'))
    send_page = int(input('请输入结束页码:'))
    url = 'https://movie.douban.com/j/search_subjects?&tag=%E5%8A%A8%E4%BD%9C&'
    for page in range(start_page, send_page+1):
        request = handler_request(url, page)
        content = urllib.request.urlopen(request).read().decode(encoding='utf-8')
        items_ = parse_content(content)

        #  将items保存即可
        string = json.dumps(items_, ensure_ascii=False)
        with open('电影.json', 'w', encoding='utf-8') as fp:
            fp.write(string)
        time.sleep(2)

if __name__ == '__main__':
    main()