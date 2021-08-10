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
print(soup.a.name)

#4, 输出a标签的类型
print(type(soup.a.name))

#5, 获取a标签的属性
print(soup.a.attrs)

#6, 获取a标签的值
print(soup.a.string)