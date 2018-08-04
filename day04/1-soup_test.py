import lxml
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('t4_html.html',encoding='utf-8'),'lxml')


# 重写 __str__方法
# print(type(soup))   #<class 'bs4.BeautifulSoup'>
# res = soup.a
# print(res)  #<a href="http://www.qing.com">李清照</a>

# 获取属性
# print(res.attrs)    #{'href': 'http://www.qing.com'}
# print(res.attrs['href'])    #http://www.qing.com
# print(res['title']) #?  KeyError: 'title'

# 获取内容
# print(res.string)
# print(res.text)
# print(res.get_text)
#<bound method Tag.get_text of <a href="http://www.qing.com">李清照</a>>

# obj = soup.div
# print(obj.string)   #None
# print(obj.text.replace('\t','').replace('\n',''))
# 阿珂        孙悟空        李白        兰陵王
# print(obj.get_text)
# <bound method Tag.get_text of <div class="hero_list">
#         阿珂
#         <p>孙悟空</p>
#         李白
#         <p>兰陵王</p>
# </div>>



#---------------------------------------

# obj = soup.find('a')
#print(obj)  #<a href="http://www.qing.com">李清照</a>
# 查找到的是第一个a

# find 加限定条件
obj_1 = soup.find('a',title='宠辱不惊')
# print(obj_1)
# <a class="花" href="http://dumu.com" title="宠辱不惊">看庭前花开花落</a>
