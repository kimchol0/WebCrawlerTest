# -*- coding = utf-8 -*-
# @Time : 2020/11/23 22:10
# @Author : KimChol
# @File: testUrllib.py
# @Software : PyCharm

import urllib.request

# 网页源代码
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
