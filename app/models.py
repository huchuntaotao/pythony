#! /usr/bin/env python
# -*- coding:utf-8 -*-

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db,login_manager
from flask_login import UserMixin,login_required
from werkzeug.security import generate_password_hash, check_password_hash

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(128), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic') #模型类名, 被关联模型类属性名
    
    def __repr__(self):
        return '<Role %r>' % self.rolename
    
    
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    
    confirmed = db.Column(db.Boolean, default=False)
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  #被外联表名.id
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def generate_confirmation_token(self, expiration=3600): #生成令牌, 有效期1小时
        s = Serializer(current_app.config['SECRCT_KEY'], expiration)
        return s.dumps({'confirm': self.id})
    
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.load(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    
@login_manager.user_loader
def load_user(user_id): #回调函数, 加载用户 #???
    return User.query.get(int(user_id))