#! /usr/bin/env python
# -*- coding:utf-8 -*-
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

serializer = Serializer('abc', 3600)  #私钥 ,有效期 ->序列号对象
s = serializer.dumps({'confirmed':'123'}) #加密字典成字符串
d = serializer.loads(s) #解密字符串成字典
print type(d),d 