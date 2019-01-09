#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from app import create_app
from config import env

app = create_app(env('dev','default'))
        
if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)