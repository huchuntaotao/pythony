#! /usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

class UTC(datetime.tzinfo): #国际标准时间 ???
    def __init__(self, offset=0):
        self._offset = offset
        
    def utcoffset(self, dt):
        return datetime.timedelta(hours=self._offset)
    
    def tzname(self, dt):
        return "UTC + %s" % self._offset
    
    def dst(self, dt):
        return datetime.timedelta(hours=self._offset) 
    
    
if __name__ == '__main__':
    #北京时间
    bj = datetime.datetime(2011, 11, 11, 0, 0, 0, tzinfo=UTC(8))
    #曼谷时间
    mg = datetime.datetime(2011, 11, 11, 0, 0, 0, tzinfo=UTC(7))
    #北京时间转成曼谷时间
    bj2mg = bj.astimezone(UTC(7))
    
    # <type 'datetime.datetime'> 2011-11-11 00:00:00+08:00
    # <type 'datetime.datetime'> 2011-11-11 00:00:00+07:00
    # <type 'datetime.datetime'> 2011-11-10 23:00:00+07:00
    print type(bj),bj
    print type(mg),mg
    print type(bj2mg),bj2mg
