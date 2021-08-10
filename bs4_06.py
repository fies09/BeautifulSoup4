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

#3,获取ul节点
print(soup.select('ul'))

#4, 查看ul节点的类型
print(type(soup.select('ul')))

for ul in soup.select('ul'):
    print(ul)
    print(type(ul))
    print(ul.select('li'))