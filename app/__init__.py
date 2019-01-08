#! /usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong' #监控客户端IP和浏览器代理信息, 一旦异常则登出.
login_manager.login_view='auth.login' #登录断点

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    from .main import main as main_blueprnit
    from .auth import auth as auth_blueprnit
    app.register_blueprint(main_blueprnit)  #url_prefix='/'
    app.register_blueprint(auth_blueprnit, url_prefix='/auth')
    
    return app


if __name__ == '__main__':   
    app = create_app('dev')
    
    @app.route('/')
    def index():
        return '<h1>Test create_app()</h1>'
    
    
    app.run(debug=True)