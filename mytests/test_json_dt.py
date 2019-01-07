#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import datetime

"""
json默认不支持的datetime.datetime数据类型时，自定义编解码函数 . 
"""
def time2str(obj):
    #python to json
    if isinstance(obj, datetime.datetime):
        json_str = {"datetime": obj.strftime("%Y-%m-%d %H:%M:%S")}
        return json_str
    return obj
    
    
def str2time(json_obj):
    #json to python
    if "datetime" in json_obj:
        date_str, time_str = json_obj["datetime"].split(' ')
        date = [int(x) for x in date_str.split('-')]
        time = [int(x) for x in time_str.split(':')]
        dt = datetime.datetime(date[0], date[1], date[2], time[0],time[1], time[2])
        return dt
    return json_obj

class MyEncoder(json.JSONEncoder):  #编码,序列化
    def default(self, obj): #重写default转化函数
        #python to json
        if isinstance(obj, datetime.datetime):
            json_str = {"datetime": obj.strftime("%Y-%m-%d %H:%M:%S")}
            return json_str
        return obj    

    
class MyDecoder(json.JSONDecoder): #解码, 反序列化
    def __init__(self):
        #调用父类的构造函数
        json.JSONDecoder.__init__(self, object_hook=self.str2time)
    
    def str2time(self, json_obj):
        #json to python
        if "datetime" in json_obj:
            date_str, time_str = json_obj["datetime"].split(' ')
            date = [int(x) for x in date_str.split('-')]
            time = [int(x) for x in time_str.split(':')]
            dt = datetime.datetime(date[0], date[1], date[2], time[0], time[1], time[2])
            return dt
        return json_obj
        
        
dt = datetime.datetime.now()
a = MyEncoder().encode(dt) #调用json.JSONDecoder的 encode()
print type(a), a
b = MyDecoder().decode(a)  #调用json.JSONDecoder的 decode()
print type(b), b
    
dt = datetime.datetime.now()  
print type(dt),dt  
a = json.dumps(dt, default=time2str)  #序列化时:指定转化函数 
print type(a), a
b = json.loads(a, object_hook=str2time) #反序列化时:指定转化函数
print type(b), b
