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

#3, 使用attrs获取id为link1的标签
print(soup.find_all(attrs={'id': 'link1'}))


#4, 使用kwargs获取class等于sister的标签
print(soup.find_all(class_='sister'))

#5, 使用text获取包含story的标签
import re
print(print(soup.find_all(name='b',text=re.compile('.*?story'))))

#6, 使用limit限制p标签的查询,只获取第一个
print(soup.find_all('p',limit=1))

#7, 使用recursive限制第一个p标签的查询
print(soup.find_all('p',limit=1,recursive=False))
