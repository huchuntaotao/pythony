# -*- coding: utf-8 -*-
import shelve

try:
    s = shelve.open('shelve_test.db')
    s['kk'] = {'int': 10, 'float': 9.5, 'String': 'Sample data'}
    s['MM'] = {1, 2, 3}
    s['QQ'] = ['8964566601', '896458888', '8888888888']
    s['AL'] = "Albaba"
except Exception, e:
    print e.message
finally:
    s.close()
    

try:
    db = shelve.open('shelve_test.db', flag='w', writeback=True)
    del db['MM'] #删除元素
    db['AL'] = "A LI BA BA" #修改元素
    db['TZ'] = "I'M TZ!" #增加元素

    #遍历1
    for k, v in db.items():
        print "%s = %r" %(k, v)
    #遍历2    
    for item in db.items():
        print item[0], db[item[0]]
except Exception, e:
    print e.message
finally:
    db.close()