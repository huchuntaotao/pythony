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


cursor.execute("update user set name=%s where id=%s", ('Alison', 1))

connection.commit()
