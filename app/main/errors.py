#! /usr/bin/env python
# -*- coding: utf-8 -*-
from . import main
from flask import render_template

@main.app_errorhandler(404) #注册全局的错误处理程序
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500) 
def interval_server_error(e):
    return render_template('500.html'), 500


