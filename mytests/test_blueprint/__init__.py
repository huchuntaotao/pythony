#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, Blueprint!</h1><br/>app.url_map=%s" % app.url_map

# 注册(唤醒)蓝本
from user import user as user_blueprint
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)