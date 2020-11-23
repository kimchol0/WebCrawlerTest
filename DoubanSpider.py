# -*- coding = utf-8 -*-
# @Time : 2020/11/23 21:44
# @Author : KimChol
# @File: DoubanSpider.py
# @Software : PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250"
    # 爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    # 保存数据
    # saveData(savepath)
    askURL("https://movie.douban.com/top250")


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10): # 调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        html = askURL(url) # 保存获取到的网页源码
            # 逐一解析数据
    return datalist


# 得到指定一个url的网页内容
def askURL(url):
    head = { # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }  # 用户代理，表示告诉网站我是什么类型的机器，浏览器（本质上是告诉浏览器我们可以接收什么水平的文件内容）
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reaspn"):
            print(e.reason)
    return html
# 保存数据
def saveData(savepath):
    print("132")


if __name__ == "__main__":  # 如果执行主函数，且运行函数名称为main时
    # 调用函数
    main()
