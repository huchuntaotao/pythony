#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://blog.csdn.net/mingzznet/article/details/53636395
# 密码的安全，关键在于密码的散列值。
# 计算散列值的函数是可复现的：只要输入一样，结果就一样。

from werkzeug.security import generate_password_hash, check_password_hash


#password: 明文密码
#method:加密方式
#salt_length:盐值长度,默认8
pwhash = generate_password_hash('abc')
print check_password_hash(pwhash, 'abc'), pwhash