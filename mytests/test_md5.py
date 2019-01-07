# -*- coding: utf-8 -*-
import hashlib

def get_md5(password):  #计算密码(字符串)的MD5值
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()
      
def cal_md5(username,password): #密码'加盐'
    return get_md5(username + password + 'the-Salt')
      
print cal_md5('lucy','12345678')
