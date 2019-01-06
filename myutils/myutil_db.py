#! /usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector


#------------------------------------------------------------------------------ 
#必填参数：user,password,database,host
#可选参数：kw(优先于默认参数)
#默认参数：host,port
#固定参数：buffered
#------------------------------------------------------------------------------ 
def connect_mysql(user,password,database, **kw):
    params= dict(user=user,password=password,database=database)
    defaults = dict(host='127.0.0.1', port=3306,
                    use_unicode=True, charset='utf8', 
                    collation='utf8_general_ci', autocommit=False)
    for k,v in defaults.iteritems():
        params[k] = kw.pop(k,v)
    params.update(kw)
    params['buffered'] = True
    return mysql.connector.connect(**params)
    
    