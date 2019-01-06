#! /usr/bin/env python
# -*- coding: utf-8 -*-

s  = '123'
try:
    int(s)
    #print 9/0
except Exception, e:
    print(e)
else:
    print 'All is Ok.'
finally:
    print 'forever.'