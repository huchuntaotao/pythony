# -*- coding: utf-8 -*-
import json


print "json.dumps() >> Serialize obj to a JSON formatted str"

lst = ['foo', {'bar': ('baz', None, 1.0, 2)}]
jsonStr = json.dumps(lst)  #对象序列化
print type(jsonStr) #<type 'str'>
print jsonStr
lst_a = json.loads(jsonStr) #将序列化字符串反序列化
print type(lst_a)  #<type 'list'>
print lst_a

dic = {'d':1, 'c':3, 'b':2, 'a': 1}
jsonStr = json.dumps(dic,sort_keys=True)  #对象序列化,同时按键排(升)序
print jsonStr

jsonStr = json.dumps(dic,sort_keys=True, separators=('|',':'))  #对象序列化,同时按键排(升)序,并自定义分隔符(元素之间为| , KV之间:)
print jsonStr

jsonStr = json.dumps(dic,sort_keys=True, separators=('|',':'), indent=2)  #对象序列化,同时按键排(升)序,并自定义分隔符(元素之间为| , KV之间:) , 增加换行缩进
print jsonStr



print "json.dump() >> Serialize obj as a JSON formatted stream to fp (a.write()-supporting file-like object)."

obj = ['foo', {'bar':('baz', None, 1.0, 2)}]
with open(r'json.txt','w+') as f:
    json.dump(obj, f)

with open(r'json.txt', 'r') as f:
    a = json.load(f)  #将序列化字符串从文件读取并反序列化
    print type(a)     #<type 'list'>
    print a