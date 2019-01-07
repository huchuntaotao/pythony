#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Manager, Shell, Command, Server


# Flask-Script的 Shell 一个加载了 Flask应用上下文的交互式环境
# make_context 在启动的 shell中添加默认的变量.
x = 100
y = [1,'a']
def make_shell_context():
    return dict(app=app, x=x, y=y)

app = Flask(__name__)
manager = Manager(app)

class Hello(Command):
    def run(self):
        print "Hello."
        
@manager.command
def hi():
    print "Hi."   

@manager.option('-n', '--name', dest='name', help='Your name', default='')
@manager.option('-a', '--age', dest='age', help='Your age', default=0)
def who(name, age):
    print "Hello,%s.You are %d years old." % (name, int(age))
     
manager.add_command('hello', Hello())
manager.add_command('start', Server(host='0.0.0.0', port=5555))  
manager.add_command("myshell", Shell(make_context=make_shell_context))


@app.route('/')
def index():
    return "<h1>Welcome to flask_script!</h1>"

if __name__ == '__main__':
    # Manager类追踪所有在命令行中调用的命令和处理过程的调用运行情况
    manager.run() #启动Manager实例, 接收命令行中的命令
    
    #python manager.py 
    #python manager.py hello
    #python manager.py hi
    #python manager.py who -n Lucy -a 18
    #python manager.py start
    #python manager.py myshell
    
    ##python manager.py shell
    #python manager.py runserver