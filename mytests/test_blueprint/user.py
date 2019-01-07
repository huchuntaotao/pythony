#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

# 蓝本的目的是模块化视图,把路由合理地拆分到不同的模块中。
# 在蓝本中定义的路由处于休眠状态，直到蓝本注册到程序上后，路由才真正成为程序的一部分。
# Flask 会为蓝本中的全部端点加上一个命名空间, 命名空间就是蓝本的名字(Blueprint 构造函数的第一个参数)。
user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/login/')
def login():
    return "<h1>欢迎登陆</h1>"

@user.route('/register/')
def register():
    return "<h1>欢迎注册</h1>"