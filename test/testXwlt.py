# -*- coding = utf-8 -*-
# @Time : 2020/11/25 20:40
# @Author : KimChol
# @File: testXwlt.py
# @Software : PyCharm
import xlwt

workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
worksheet = workbook.add_sheet('sheet1')  # 创建工作表
worksheet.write(0, 0, 'hello')  # 写入数据，第一个参数“行”，第二个参数“列”，第三个参数内容
workbook.save('student.xls')  # 保存数据表
