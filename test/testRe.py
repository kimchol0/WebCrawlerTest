# -*- coding = utf-8 -*-
# @Time : 2020/11/24 21:59
# @Author : KimChol
# @File: testRe.py
# @Software : PyCharm

# 正则表达式：字符串模式 （判断字符串是否符合一定的标准）

import re

# 创建模式对象
pat = re.compile("AA")  # 此处的AA是正则表达式，用来验证其它的字符串
m = pat.search("CBA")  # seacrh字符串被校验的内容，进行比对查找
m1 = pat.search("ABCAA")
m2 = pat.search("AACAADDCCAAA")
print(m)  # none
print(m1)  # <re.Match object; span=(3, 5), match='AA'>
print(m2)  # <re.Match object; span=(0, 2), match='AA'>
# 另一种写法，没有模式对象
m3 = re.search("asd", "Aasd")  # 前面的字符串是规则（模板），后面的字符串是被校验的对象
print(m3)  # <re.Match object; span=(1, 4), match='asd'>
print("------------------------------")
print(re.findall("a", "ASDaDFGAa"))  # 前面字符串是规则，后面字符串是被校验的。输出结果['a', 'a']
print("------------------------------")
print(re.findall("[A-Z]", "ASDaDFGAa"))  # ['A', 'S', 'D', 'D', 'F', 'G', 'A']
print("------------------------------")
print(re.findall("[A-Z]+", "ASDaDFGAa"))  # ['ASD', 'DFGA']
print("------------------------------")
# sub
print(re.sub("a", "A", "abcdcasd"))  # 找到a，用A替换，在第三个字符串做查找 输出结果AbcdcAsd
# 建议在正则表达式中，将被比较的字符串前面加上r，就不用担心转义字符的问题了
