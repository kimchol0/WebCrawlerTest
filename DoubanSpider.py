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
    datalist=getData(baseurl)
    savepath=".\\豆瓣电影Top250.xls"
    # 保存数据
    saveData(savepath)


# 爬取网页
def getData(baseurl):
    datalist = []
    # 逐一解析数据
    return datalist

# 保存数据
def saveData(savepath):
    print("132")




if __name__ == "__main__":  # 如果执行主函数，且运行函数名称为main时
    # 调用函数
    main()
