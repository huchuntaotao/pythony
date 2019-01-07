#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from app import create_app,db
from config import env
app = create_app(env('dev','default'))

def create_db(app,db): #激活程序上下文， 创建DB
    with app.app_context():
        db.create_all()
        
if __name__ == '__main__':
    #create_db(app,db)
    print app.url_map
    app.run(debug=True)