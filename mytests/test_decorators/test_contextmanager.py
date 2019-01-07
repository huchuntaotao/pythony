#! /user/bin/env python
# -*- coding: utf-8 -*-
from contextlib import contextmanager

@contextmanager
def make_open_context(file, mode):
    print "here."
    fp = open(file, mode)
    try:
        yield fp
    finally:
        print "here2."
        fp.close()
        
with make_open_context('hello.py','r') as file_obj:
    print file_obj.read()
    
    
class MyResource(object):
    def query(self):
        print "query............"
        
@contextmanager        
def make_myresouce():
    print "Connect MyResource"
    yield MyResource()
    print "Close MyResource"
    
with make_myresouce() as r:
    r.query()
    

@contextmanager
def book_mark():
    print "<<",
    yield
    print ">>"
    
with book_mark():
    print "Learn Python The Hard Way",
