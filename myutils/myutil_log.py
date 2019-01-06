#! /usr/bin/env python
# -*- coding:utf-8 -*-
import logging
from myutil_time import now,stime

def _profiling(start, sql, interval=1000):
    '''
    start 开始执行时间
    sql ...
    interval 超出多少毫秒给出警告,默认1秒
    '''
    if now('f')-start > interval:
        logging.warning('[PROFILING] [DB] %s-%s: %s' % (stime(start), now('s'), sql))
    else:
        logging.info('[PROFILING] [DB] %s-%s: %s' % (stime(start), now('s'), sql))
