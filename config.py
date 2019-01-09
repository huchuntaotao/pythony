#! /usr/bin/env python
# -*- coding:utf-8 -*-
import os
import logging

def env(k, default=''):
    return os.environ.get(k.upper(),default)


class Config(object):
    SECRET_KEY = env('SECRET_KEY','HARD TO GUESS STRING')
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    
    MAIL_SERVER = 'smtp.qq.com' 
    MAIL_PORT = 465
    
    MAIL_USE_TLS = False #传输层安全（Transport Layer Security，TLS）协议
    MAIL_USE_SSL = True #安全套接层（Secure Sockets Layer，SSL）协议
    
    MAIL_USERNAME = env('MAIL_USERNAME','896456601@qq.com') 
    MAIL_PASSWORD = env('MAIL_PASSWORD','cbkemwplnphqbcjd')
    MAIL_DEFAULT_SENDER = '896456601@qq.com'
    
    MAIL_MAX_EMAILS = None
    MAIL_ASCII_ATTACHMENTS = False
    
    PYTHONY_ADMIN = env('PYTHONY_ADMIN','Pythony Admin<896456601@qq.com>')
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN', 'Flasky Admin<896456601@qq.com>')

    @staticmethod
    def init_app(app): #预留方法???
        print 'Enter init_app()...'
        #logging.debug('Enter init_app()...')
    

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:password@127.0.0.1:3306/pythony'  
    

class ProdConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True
  
  
config = {
    'dev':DevConfig,
    'test':TestConfig,
    'prod':ProdConfig,
    'default':DevConfig
}

  
if __name__ == '__main__':
    print env('NLS_LAx','XXX')
    print config.get(env('dev','default')).SQLALCHEMY_DATABASE_URI