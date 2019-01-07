#! /usr/bin/env python
# -*- coding: utf-8 -*-

try:
    d = {'a': 1, 'b': 2, 'c': 3}
    print 1 / 0
    print d['d']
except ZeroDivisionError, e:
    print "ZeroDivisionError...!"
except KeyError, e:
    print "KeyError...!"
except Exception, e:
    print "Exception...!"
else:
    print "没有发生异常...!"
finally:
    print "无论怎样都会执行...!"