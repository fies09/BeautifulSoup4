#coding = utf-8
#关联选择器

import requests

res = requests.get('https://wenku.baidu.com/view/abde813d87c24028915fc366.html')
# print(res.text)


html_str = res.text
#1, 导入beautiful Soup 类
from bs4 import BeautifulSoup

#2, 传入参数,实例化这个类
soup = BeautifulSoup(html_str,'lxml')

# #3, 获取p标签的子节点
# print(soup.p.contents)
#
# #4, 获取p标签的子节点 children
# print(soup.p.children)
#
# for i,child in enumerate(soup.p.children):
#     print(i,child)

# #6, 获取a节点的父节点 parent
# print(soup.a.parent)
#
# #7, 获取a节点的祖孙节点 parents
# print(soup.a.parents)
#
# print(list(enumerate(soup.a.parents)))
#

# 8, 获取a节点的兄弟节点
print(soup.a.next_sibling)

#9, 获取a节点的所有兄弟节点 next_siblings
print(soup.a.next_siblings)

print(list(enumerate(soup.a.next_siblings)))


#10, 获取a节点的前面一个节点 previous_sibling
print(soup.a.previous_sibling)

#11, 获取a节点前的所有节点 previous_siblings
print(soup.a.previous_siblings)

print(list(enumerate(soup.a.previous_siblings)))