# -*- coding = utf-8 -*-
# @Time : 2020/11/23 22:10
# @Author : KimChol
# @File: testUrllib.py
# @Software : PyCharm

import urllib.request

# 网页源代码
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))  # 对获取到的网页源码进行UTF-8编码

# 获取一个POST请求
import urllib.parse

# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))


response = urllib.request.urlopen("http://httpbin.org/get")
print(response.read().decode("utf-8"))