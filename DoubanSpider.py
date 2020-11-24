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
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    # 保存数据
    # saveData(savepath)
    # askURL("https://movie.douban.com/top250")


findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式（影片详情链接的规则）
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S让换行符包含在字符中（影片图片链接的规则）
findTitle = re.compile(r'<span class="title">(.*)</span>')  # 影片片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 影片评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')  # 评价人数
findInq = re.compile(r'<span class="inq">(.*)</span>')  # 找到概况
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 影片相关内容


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):  # 查找符合要求的字符串，形成列表
            data = []  # 保存一部电影的所有信息
            item = str(item)

            link = re.findall(findLink, item)[0]  # 通过正则表达式查找指定的字符串（影片详情链接）
            data.append(link)  # 添加链接
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)  # 添加图片
            titles = re.findall(findTitle, item)  # 片名可能只有一个中文名，没有外国名
            if (len(titles) == 2):
                ctitle = titles[0]  # 添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去掉无关符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ')  # 留空外国名字

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加评分
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 添加评价人数
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)
            else:
                data.append(" ")  # 留空
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉br
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  # 把处理好的一步电影信息放入datalist
        for item in datalist:
                print(item)
    return datalist


# 得到指定一个url的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }  # 用户代理，表示告诉网站我是什么类型的机器，浏览器（本质上是告诉浏览器我们可以接收什么水平的文件内容）
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveData(savepath):
    print("132")


if __name__ == "__main__":  # 如果执行主函数，且运行函数名称为main时
    # 调用函数
    main()
