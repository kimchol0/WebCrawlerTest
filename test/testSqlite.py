# -*- coding = utf-8 -*-
# @Time : 2020/11/25 21:07
# @Author : KimChol
# @File: testSqlite.py
# @Software : PyCharm

import sqlite3

conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
print("成功打开数据库")
c = conn.cursor()  # 获取游标
sql1 = '''
    drop table company;
'''
sql2 ='''
    create table company
    (id int primary key not null,
    name text not null,
    age int not null,
    address char(50),
    salary real);
'''
sql3 = '''
    insert into company (id,name,age,address,salary)
    VALUES (1,'张三','32','成都','8000')
'''
sql4 = '''
    insert into company (id,name,age,address,salary)
    VALUES (2,'李四','30','重庆','15000')
'''
sql5 = '''
    select id,name,address,salary from company
'''
c.execute(sql1)  # 执行sql语句
c.execute(sql2) # 执行sql语句
print("成功建表")
c.execute(sql3)  # 执行sql语句
c.execute(sql4) # 执行sql语句
conn.commit()  # 提交数据库操作
cursor = c.execute(sql5)
for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("address=",row[2])
    print("salary=",row[3],"\n")
conn.close()  # 关闭数据库连接


