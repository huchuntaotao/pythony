#! /usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

# cursor.execute(sql, params, multi=False)
# 第1个参数是要执行的SQL语句，其中，参数位置先使用占位符来占位.
# 在SQL中的占位符，统一写%s, 具体的类型，是在tuple中，传入的参数由元素类型决定.
# 第2个参数是一个序列，元素值就是SQL占位符对应的参数。
# 第3个参数是一个bool值，表示第一个参数是不是多个SQL语句，如果是的话，就传入True，否则传入False。


cfg = {'user': 'root', 'password': 'password',
       'database': 'testdb', 'host': '127.0.0.1', 'port': 3306}
connection = mysql.connector.connect(**cfg)
cursor = connection.cursor()

cursor.execute("select * from user")
description = cursor.description  # 字段信息,元组列表
print type(description), description
result = cursor.fetchall()  # 查询结果,元组列表
# result = cursor.fetchone()  # 查询结果,元组
# result = cursor.fetchmany(3)  # 返回结果,元组列表, 默认为1
print result


cursor.execute("select * from user where id=%s", (1,))
result = cursor.fetchone()
print result

cursor.execute("select * from user where name like %s", ['%li%', ])
result = cursor.fetchall()
print result

cursor.execute(
    "select * from user where id>%s and name like %s", [3, '%li%', ])
result = cursor.fetchall()
print result
