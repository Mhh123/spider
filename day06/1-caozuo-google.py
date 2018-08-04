from selenium import webdriver
import time

# 创建一个浏览器对象
# chrome驱动地址
path = r'E:\locate_app\develop\Plug_in\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)

# 操作浏览器的过程
url = 'http://www.baidu.com'
browser.get(url)
time.sleep(3)

#  查找input输入框-
my_input = browser.find_element_by_id('kw')
#  网框里面写内容
my_input.send_keys('美女')
time.sleep(2)
Btn = browser.find_element_by_id('su')
Btn.click()
time.sleep(2)

#  打开美女图片
# Img = browser.find_element_by_xpath('//div[@class="op-img-address-divide-high"]/a[3]/img')
Img = browser.find_elements_by_css_selector('.op-img-address-divide-high a')[2]
Img.click()
time.sleep(2)
# 执行完毕，关闭浏览器
browser.quit()

