#coding = utf-8


import requests

res = requests.get('https://wenku.baidu.com/view/abde813d87c24028915fc366.html')
# print(res.text)


html_str = res.text
#1, 导入beautiful Soup 类
from bs4 import BeautifulSoup

#2, 传入参数,实例化这个类
soup = BeautifulSoup(html_str,'lxml')

#3,定位元素title
print(soup.title)

#4, 查看获取到的结果的类型 获取到的元素的类型是Tag类的对象
print(type(soup.title))

#5, 当html中存在多个相同的节点时,只会提取第一个节点
print(soup.a)