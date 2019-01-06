#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os


print os.environ #return dict
print os.environ.get('NLS_LANG', 'UTF-8')