#coding = utf-8
#css选择器

import requests

res = requests.get('https://wenku.baidu.com/view/abde813d87c24028915fc366.html')
# print(res.text)


html_str = res.text
# print(html_str)
#1, 导入beautiful Soup 类
from bs4 import BeautifulSoup

#2, 传入参数,实例化这个类
soup = BeautifulSoup(html_str,'lxml')

#3, 获取class = 'ie-fix' 的div
print(soup.select('.reader-txt-layer .ie-fix'))

#4,获取所有li节点 标签选择器
print(soup.select('ul li'))

#5, 获取所有的li节点 类选择器
print(soup.select('.list .element'))

#6, 获取第二个ul的li节点 id选择器
print(soup.select('#list-2 li'))

#7,获取第二个ul的li节点  类选择器
print(soup.select('.small-list li'))

#8, 获取第二个ul节点 列表获取
# print(soup.select('ul')[1])