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

#3, 获取span标签 字符串
print(soup.find_all(name='span'))

#4, 获取span标签 正则表达式 模型对象
import re
reg = re.compile('^sp')
print(soup.find_all(name=reg))

#5, 获取a标签和span标签 列表
print(soup.find_all(name=['a','span']))

#6, True的用法 递归的获取所有的标签
print(soup.find_all(name=True))