#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from flask import Flask
from flask_mail import Mail,Message
from threading import Thread

app = Flask(__name__)

# Flask-Mail 连接到简单邮件传输协议（Simple Mail Transfer Protocol，SMTP）服务器，并把邮件交给这个服务器发送。
# Flask-Mail SMTP服务器的配置(QQ邮箱):
app.config['MAIL_SERVER'] = 'smtp.qq.com' 
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False #传输层安全（Transport Layer Security，TLS）协议
app.config['MAIL_USE_SSL'] = True #安全套接层（Secure Sockets Layer，SSL）协议
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME','896456601@qq.com') 
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD','cbkemwplnphqbcjd')
app.config['MAIL_DEFAULT_SENDER'] = '896456601@qq.com'
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)


msg = Message(subject="Hello, I'm Flask-Mail", 
              sender=('taozi',  '896456601@qq.com'),
              recipients=['896456601@qq.com'])
# 邮件内容, 呈现格式取决于邮件客户端,文本或html格式.
msg.body='Flask-Mail.testing'
msg.html="<b>Flask-Mail.testing</b>"


def send_async_email(app, msg): #激活程序上下文 
    with app.app_context(): #发送邮件
        mail.send(msg)
    with app.open_resource('upload.png') as fp: #添加附件???
        msg.attach('upload.png','image/png', fp.read())
           
def send_email(app,msg): #异步发送  
    thr = Thread(target=send_async_email, args=(app, msg))
    thr.start()
    return thr


if __name__ == '__main__':
    send_email(app, msg)
