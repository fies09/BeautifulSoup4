#coding = utf-8


import requests

res = requests.get('https://wenku.baidu.com/view/abde813d87c24028915fc366.html')
# print(res.text)


html_str = res.text
#1, 导入beautiful Soup 类
from bs4 import BeautifulSoup

#2, 传入参数,实例化这个类
soup = BeautifulSoup(html_str,'lxml')

#3,获取head的子节点title
print(soup.head.title)

#4, 获取head子节点title的类型
print(type(soup.head.title))

#5, 获取head子节点title的内容
# print(soup.head.title.string)