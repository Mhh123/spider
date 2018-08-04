import sys
import urllib.request
import urllib.parse
import traceback

url = 'http://www.maodan.com/'
try:
    response = urllib.request.urlopen(url)
except Exception as e:
    # traceback.print_exc()
    # traceback.print_exc(file=sys.stdout)
    print('error------------------->', e)
    # e <urlopen error [Errno 11004] getaddrinfo failed>
print('error 被捕获program继续running')
