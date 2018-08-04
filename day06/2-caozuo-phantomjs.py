from selenium import webdriver
import time

path = r'E:\locate_app\develop\Plug_in\phantomjs-2.1.1-windows\bin\phantomjs.exe'


#  生成对象
browser = webdriver.PhantomJS(executable_path=path)

#  打开百度
browser.get('http://www.baidu.com')
time.sleep(3)


# 拍照片,查看现在走到哪
# browser.save_screenshot('./pic/baidu1.png')


#  找到输入框
browser.find_element_by_id('kw').send_keys('气质美女')
time.sleep(2)
# browser.save_screenshot('./pic/meinv.png')


browser.find_element_by_id('su').click()
time.sleep(3)

browser.save_screenshot('./pic/meinv1.png')

browser.quit()
