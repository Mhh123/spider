import time

from lxml import etree
from selenium import webdriver


path = r'E:\locate_app\develop\Plug_in\phantomjs-2.1.1-windows\bin\phantomjs.exe'

browser = webdriver.PhantomJS(executable_path=path)

url = 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action='

browser.get(url)
time.sleep(2)


browser.save_screenshot('pic/douban1.png')

#  让浏览器执行一句代码，模拟滚动条下拉
js = 'document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)

browser.save_screenshot('pic/douban2.png')

js1 = 'document.body.scrollTop=20000'
browser.execute_script(js1)
time.sleep(1)

browser.save_screenshot('./pic/douban3.png')



# 得到phantomjs执行js之后的代码，动态的内容已经写入到标签中
# with open('pic/douban.html', 'w', encoding='utf-8') as fp:
#     fp.write(browser.page_source)

#  如果我没有捕获到，我就可以通过这种方式；
#  让phantomjs执行js代码，结果返回给我
#  我再通过xpath、bs来解析网页的内容

tree = etree.HTML(browser.page_source)


name_list = tree.xpath('//div[@class="movie-name"]/span/a/text()')[:40]
print(name_list)
print(len(name_list))
browser.quit()

