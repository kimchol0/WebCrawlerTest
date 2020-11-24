# -*- coding = utf-8 -*-
# @Time : 2020/11/24 19:44
# @Author : KimChol
# @File: testbs4.py
# @Software : PyCharm

'''
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种：
-Tag
-NavigableString
-BeautifulSoup
-Comment
'''

from bs4 import BeautifulSoup

file = open('./baidu.html', 'rb')
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, 'html.parser')

# 1.Tag 标签及其内容：拿到它所找到的第一个内容
print("查找title标签及其内容:", bs.title)
print("--------------------")
print("查找a标签及其内容：", bs.a)
print("--------------------")
print("查找整个head标签及其内容", bs.head)
print("--------------------")
print("bs.head的类型：", type(bs.head))
print("--------------------")
# 2.NavigableString 标签里的内容（字符串）
print("仅拿到title标签的内容：", bs.title.string)
print("--------------------")
print("bs.title.string的类型：", type(bs.title.string))
print("--------------------")
print("拿到a标签及标签内属性的值，并且以字典的方式输出：", bs.a.attrs)
print("--------------------")
# 3.BeautifulSoup 表示整个文档
print("bs类型：", type(bs))
print("--------------------")
print("打印bs的名字：", bs.name)
print("--------------------")
print("打印整个bs文档的内容（实际上就是读取整个html）", bs)
print("--------------------")
# 4.Comment是一个特殊的NavigableString,但输出内容不包含注释符号
print("输出a标签下的内容：", bs.a.string)
print("bs.a.string类型", type(bs.a.string))
print("--------------------")
print("--------------------")
print("--------------------")
print("--------------------")
# 文档的遍历
print("输出head标签内contents的内容：", bs.head.contents)
print("上面内容中仅输出第一个：（使用下标访问）", bs.head.contents[1])
print("--------------------")
print("--------------------")
print("--------------------")
print("--------------------")
# 文档的搜索
# （1）findall
# 字符串过滤：会查找与字符串完全匹配的内容
t_list = bs.find_all("a")
print("找到所有a标签：", t_list)
# 正则表达式搜索：使用search（）方法来匹配内容
import re

t_list2 = bs.find_all(re.compile("a"))
print("包含a的都显示出来：（只要标签含有a，就把这个标签及其所有内容全都显示出来）\n", t_list2)
print("--------------------")


# 方法 传入一个函数（方法），根据函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr('name')


t_list3 = bs.find_all(name_is_exists)
print("标签里面有name的都显示出来：")
for item in t_list3:
    print(item)
print("--------------------")
print("--------------------")
# （2） kwargs参数
t_list4 = bs.find_all(id="head")
print("输出id=head内容里面所有的子内容：")
for item in t_list4:
    print(item)
print("--------------------")
t_list5 = bs.find_all(class_=True)
print("输出标签里面有class的内容：")
for item in t_list5:
    print(item)
print("--------------------")
t_list6 = bs.find_all(href="http://news.baidu.com")
print("输出含有href='http://news.baidu.com'的内容")
for item in t_list6:
    print(item)
# （3） text参数
t_list7 = bs.find_all(text="hao123")
print("查找含有hao123的：")
for item in t_list7:
    print(item)
print("--------------------")
t_list8 = bs.find_all(text=["hao123", "地图", "贴吧"])
print("查找含有hao123,地图，贴吧的：")
for item in t_list8:
    print(item)
print("--------------------")
# 应用正则表达式来查找包含特定文本的内容（标签里的字符串）
t_list9 = bs.find_all(text=re.compile("\d"))
print("正则表达式匹配数字的：")
for item in t_list9:
    print(item)
# (4)limit参数
t_list10=bs.find_all("a",limit=3)
print("含有a标签的前三个")
for item in t_list10:
    print(item)
print("--------------------")
# css选择器
print("包含title的：（通过标签查找）",bs.select("title"))
print("--------------------")
print("包含mnav类的：（通过类名来查找）",bs.select(".mnav"))
print("--------------------")
print("包含ID为u1的：（通过ID来查找）\n",bs.select("#u1"))
print("--------------------")
t_list11 = bs.select("a[class='bri']")
print("查找a标签里包含class=bri的：（通过属性来查找）",t_list11)
print("--------------------")
t_list12 = bs.select("head > title")
print("查找head标签下的title标签及其内容：（通过子标签来查找）")
for item in t_list12:
    print(item)
print("--------------------")
t_list13 = bs.select(".mnav ~ .bri")
print("通过兄弟节点.mnav ~ .bri来查找：",t_list13[0].get_text())