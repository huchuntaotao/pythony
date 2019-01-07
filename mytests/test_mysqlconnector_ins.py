#! /usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector


cfg = {
    'user': 'root',
    'password': 'password',
    'database': 'testdb',
    'host': '127.0.0.1',
    'port': 3306
}

connection = mysql.connector.connect(**cfg)
cursor = connection.cursor()

cursor.execute("delete from user")
cursor.execute("insert into user (id,name) values (1, 'Tom')")

cursor.execute(  # 元组
    "insert into user (id,name) values (%s, %s)",
    (2, 'Lucy')
)

cursor.execute(  # 列表
    "insert into user (id,name) values (%s, %s)",
    [3, 'LiLei']
)

cursor.execute(  # 字典
    "insert into user (id,name) values (%(id)s, %(name)s)",
    {'id': 4, 'name': 'HanMeiMei'}
)

cursor.executemany(  # 元组元组
    "insert into user (id,name) values (%s, %s)",
    ((5, 'Scott'), (6, 'John'))
)

cursor.executemany(  # 列表元组
    "insert into user (id,name) values (%s, %s)",
    ([7, 'Smith'], [8, 'Dawei'])
)

cursor.executemany(  # 元组列表
    "insert into user (id,name) values (%s, %s)",
    [(9, 'XiaoMing'), (10, 'XiaoHong')]
)

cursor.executemany(  # 列表列表
    "insert into user (id,name) values (%s, %s)",
    [[11, 'Zhangsan'], [12, 'Lisi']]
)

cursor.executemany(  # 字典元组
    "insert into user (id,name) values (%(id)s, %(name)s)",
    ({'id': 13, 'name': 'Wangwu'}, {'id': 14, 'name': 'Zhaoliu'})
)

cursor.executemany(  # 字典列表
    "insert into user (id,name) values (%(id)s, %(name)s)",
    [{'id': 15, 'name': 'XiaoWang'}, {'id': 16, 'name': 'XiaoWangBa'}]
)

connection.commit()
