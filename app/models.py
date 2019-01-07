#! /usr/bin/env python
# -*- coding:utf-8 -*-

from . import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(128), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic') #模型类名, 被关联模型类属性名
    
    def __repr__(self):
        return '<Role %r>' % self.rolename
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  #被外联表名
    
    def __repr__(self):
        return '<User %r>' % self.username