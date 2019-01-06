#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time

'''
字符串,结构化时间,时间戳转换
'''
 
def ftime(t, f='%Y-%m-%d %H:%M:%S'):
    """Change structime or stime to ftime"""
    if isinstance(t, float) or isinstance(t, int):
        return float(t)
    elif isinstance(t, str):
        return time.mktime(time.strptime(t,f))
    elif isinstance(t, time.struct_time):
        return time.mktime(t)
    else:
        raise ValueError('Not structime or stime!')      
  
        
def stime(t, f='%Y-%m-%d %H:%M:%S'):
    """Change structime or ftime to stime"""
    if isinstance(t, str):
        return t
    elif isinstance(t, float) or isinstance(t, int):
        return time.strftime(f, time.localtime(t)) 
    elif isinstance(t, time.struct_time):
        return time.strftime(f, t)
    else:
        raise ValueError('Not structime or ftime!')      
 
        
def structime(t, f='%Y-%m-%d %H:%M:%S'):
    """Change stime or ftime to structime"""
    if isinstance(t, time.struct_time):
        return t
    elif isinstance(t, float) or isinstance(t, int):  
        return time.localtime(t)
    elif isinstance(t, str):
        return time.strptime(t, f)
    else:
        raise ValueError('Not stime or ftime!')   


def now(ttype='struct', f='%Y-%m-%d %H:%M:%S'):
    """System current time."""
    t = time.time()
    ttype = ttype.lower()
    if ttype=='f':
        return t
    elif ttype=='s':
        return stime(t,f)
    else:
        return structime(t)

def fix_number(m,n=10,prefix='0',suffix=''):
    if isinstance(m, int) or isinstance(m, long):
        return prefix+str(m)+suffix if m<n else str(m)
    else:
        raise ValueError('Not int or long number value!')   

def year(t=now()):
    return structime(t).tm_year 

def month(t=now()):
    return structime(t).tm_mon 

def day(t=now()):
    return structime(t).tm_mday

def ymd(t=now(),f=''): # return str
    return f.join([fix_number(year(t),n=100,prefix='20'),fix_number(month(t)),fix_number(day(t))])

def hour(t=now()):
    return structime(t).tm_hour

def minute(t=now()):
    return structime(t).tm_min

def second(t=now()):
    return structime(t).tm_sec

def hms(t=now(),f=''): # return str
    return f.join([fix_number((hour(t))),fix_number(minute(t)),fix_number(second(t))])
  
  
if __name__ == '__main__':
    print ymd(f='-'), hms(now('s'),':')