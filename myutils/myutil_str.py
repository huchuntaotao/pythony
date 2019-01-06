#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uuid import uuid1,uuid4
from myutils.myutil_time import now


def id32(uuid_no=1, is_hex=False):
    """Create 32 string for id."""
    id_str = uuid1() if uuid_no==1 else uuid4()
    return  id_str.hex if is_hex else str(id_str).replace('-', '')

def id50(ftime=now('f')):
    """Create 50 string for id."""
    return '%018d%s' % (int(ftime*1000), id32())


def fmap(s, d, lstr='{', rstr='}'):
    for k, v in d.iteritems():
        s = s.replace(lstr+k+rstr,str(v))
    return s

if __name__ == '__main__':
    hello = "My name is {name},I am {age} years old.I like {hobby}"
    print fmap(hello,{'name':'Lucy', 'age': 18, 'hobby':'music travel'})