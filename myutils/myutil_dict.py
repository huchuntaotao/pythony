#! /usr/bin/env python
# -*- coding: utf-8 -*-

class SimpleDict(dict):
    '''x.key style'''
    def __init__(self, names=(), values=(), **kw):
        super(SimpleDict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def simple(d):  #内置字典dict, 转化为简单字典SimpleDict
    sd = SimpleDict()
    for k, v in d.iteritems():
        sd[k] = simple(v) if isinstance(v, dict) else v
    return sd

def merge(defaults, override): #字典合并, 后来居上
    r = {}
    for k, v in defaults.iteritems():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


if __name__ == '__main__':
    a = ('scolia', 123, True)
    b = ('good', 456)
    b = ['good', 456]
    b = ()