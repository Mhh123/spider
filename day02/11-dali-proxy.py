import random
import time
import urllib.request

# 将代理读取进来，读成一耳光列表

fp = open('pool.txt','r',encoding='utf-8')
lt = fp.readlines()
fp.close()
# print(lt)
url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'

while 1:
    proxy = random.choice(lt).rstrip('\n')
    # print(proxy)
    """
    >>> help(random.choice)
    Help on method choice in module random:
    
    choice(seq) method of random.Random instance
        Choose a random element from a non-empty sequence.
    """

    daili = {'http':proxy}
    print('现在使用的是%s的代理'% daili)
    handler = urllib.request.ProxyHandler(proxies=daili)
    opener = urllib.request.build_opener(handler)
    try:
        response = opener.open(url)

        with open('daili.html', 'wb') as fp:
            fp.write(response.read())
        break
    except Exception as e:
        print('代理服务器%s使用失败'% proxy)
    finally:
        print('现在结束的是%s的代理'% daili)
    time.sleep(2)

