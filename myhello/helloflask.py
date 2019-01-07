#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 激活虚拟环境 activate venv
# D:\Python27\venv\Scripts\activate

import os
from datetime import datetime
from threading import Thread #???

from flask import Flask
from flask import flash
from flask import request, session
from flask import make_response, redirect, abort, render_template, url_for

from flask_bootstrap import Bootstrap   #模板
from flask_moment import Moment #日期时间本地化
from flask_script import Manager,Shell #命令行
from flask_sqlalchemy import SQLAlchemy #DB
from flask_mail import Mail, Message #
from flask_migrate import Migrate, MigrateCommand #数据库迁移,被集成到Flask-Script

from flask_wtf import FlaskForm #表单
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#创建程序实例
app = Flask(__name__)

"""配置"""
app.config['SECRET_KEY'] = 'HARD TO GUESS STRING'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:password@localhost:3306/pythony'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['MAIL_SERVER'] = 'smtp.qq.com' 
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False #传输层安全（Transport Layer Security，TLS）协议
app.config['MAIL_USE_SSL'] = True #安全套接层（Secure Sockets Layer，SSL）协议
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME','896456601@qq.com') 
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD','cbkemwplnphqbcjd')
app.config['MAIL_DEFAULT_SENDER'] = '896456601@qq.com'
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False


"""扩展"""
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db =SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class NameForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField('Submit')
    

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')
    
    def __repr__(self):
        return '<Role %r>' % self.name
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return '<User %r>' % self.username

        
def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+' '+subject,
                  sender=('taozi',  '896456601@qq.com'),
                  recipients=[to])
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    mail.send(msg)


"""异步发送电子邮件"""
def send_async_email(app, msg):
    #很多 Flask 扩展都假设已经存在激活的程序上下文和请求上下文。
    with app.app_context():
        mail.send(msg)
        
def send_email(to, subject, template, **kwargs):
    msg = Message(subject='Pythony' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], 
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    # 把发送电子邮件的函数移到后台线程中, 避免处理请求过程中不必要的延迟. (>: Celery任务队列)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


@app.route('/mail/', methods=['GET', 'POST'])
def mail_index():
    form = NameForm()   #表单
    if form.validate_on_submit(): #表单验证
        user = User.query.filter_by(username=form.name.data).first() #DB查找
        if user is None:#没查到
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known']=False
            if app.config['FLASKY_ADMIN']:
                send_mail('896456601@qq.com', 'New User', '/mail/new_user',user=user) 
        else:#查到了
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('mail_index'))
    return render_template('/mail/index.html', form=form,name=session.get('name'), known=session.get('known', False))


@app.shell_context_processor  #上下文处理器,开放变量到模板
def make_shell_context():  
    return dict(db=db, User=User, Role=Role)

#(venv) $ python helloflask.py shell
#导入变量到shell环境
manager.add_command("shell", Shell(make_context=make_shell_context))  

# 自动创建迁移脚本 ???
# python hello.py db migrate -m "initial migration" 

# 更新数据库 ???
# python hello.py db upgrade

#注册路由(访问DB)
@app.route('/db', methods=['GET', 'POST'])
def db_index():
    form = NameForm()
    if form.validate_on_submit():
        username = form.name.data
        user = User.query.filter_by(username=username).first()
        if user is None:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
            session['known']=False
        else:
            session['known']=True
        session['name']=form.name.data
        return redirect(url_for('db_index'))
    return render_template('/db/index.html', form=form,name=session.get('name'), known=session.get('known', False))


#注册静态路由
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    urlmap = app.url_map
    return '<h1>浏览器: %r</h1><br/><p>请求头 : %r </p><br/><p>URL映射: %r</p><br/> ' % (user_agent, request.headers, urlmap)


#注册路由(返回response对象)
@app.route('/rsp')
def rsp():
    response = make_response('<h1>This document carries a cookie.</h1>')
    response.set_cookie('answer', 'NO WAY!')
    return response

#注册路由(重定向)
@app.route('/baidu')
def baidu():
    return redirect('http://www.baidu.com')

# 定义User类
class User_(object):
    def __init__(self, id, name):
        self.id=id
        self.name=name

#定义user加载函数        
def load_user(id):
    return User_(1, 'Lucy') if id==1 else None  

#注册动态路由(返回错误响应)
@app.route('/user/<int:id>')
def user(id):
    #id = int(id)
    user = load_user(id)
    prompt = '<h1>hello, the user-id is [%s].</h1>' % id #提示信息
    if user is not None:
        return prompt + '<br/><h1>and the user-name is [%s].</h1>' % user.name
    else:
        return abort(404)

 
#注册路由(404)
@app.errorhandler(404) 
def not_found(e):
    return render_template('/bts/404.html'),404

#注册路由(500)
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('/bts/500.html')
  
    
#注册路由(WFT表单)
@app.route('/wtf', methods=['GET', 'POST'])
def wtf_index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('/wtf/index.html', form=form, name=name)

#注册路由(刷新问题)
@app.route('/refresh', methods=['GET', 'POST'])
def wtf_refresh():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name!=form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        print url_for('wtf_refresh')
        return redirect(url_for('wtf_refresh'))
    return render_template('/wtf/index.html', form=form,name=session.get('name'))

    
#注册静态模板路由
@app.route('/tpl')
def tpl_index():
    return render_template('/hello/index.html')

#注册动态模板路由
@app.route('/tpl/user/<name>')
def tpl_user(name):
    return render_template('/hello/user.html', name=name)


#注册路由(静态BTS模板)
@app.route('/bts')
def bts_index():
    return render_template('/bts/index.html', current_time=datetime.utcnow())

#注册路由(动态BTS模板)
@app.route('/bts/user/<name>')
def bts_user(name):
    return render_template('/bts/user.html', name=name)
    

if __name__ == '__main__':
    #创建DB
    #db.create_all()
    #以debug模式启动WEB开发服务器
    app.run(debug=True)
    
    #启动后支持命令行解析, 相当于cmd下执行python hello.py
    #manager.run()
    #Cmd: 
    #python hello.py >>显示帮助信息
    #python hello.py runserver >>以debug模式启动WEB开发服务器
    #python hello.py runserver --help >>查看runserver命令帮助信息
    #python hello.py runserver --host:0.0.0.0 >> 开放同网访问权限(默认localhost)