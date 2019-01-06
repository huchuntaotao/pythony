#! /usr/bin/env python
# -*- coding: utf-8 -*-


def is_empty(obj,
            check_inner=False, 
            emptys=['', 0,'0', None,False, 'None','False']):
    '''
    Check the obj(str/list/tuple/dict) is empty or not.
    if not check inner, check by length.
    if check inner, check by elements; ingore blank-character, ingore case-sensitive.
    '''
    if isinstance(obj,str):
        return obj=='' if not check_inner else obj.replace(' ', '')==''
    elif isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, dict):
        if not check_inner:
            return len(obj)==0
        else:
            all_is_empty = True #假设全是空
            for v in obj:
                v = v.replace(' ','').capitalize() if isinstance(v,str) else v
                all_is_empty = all_is_empty and (v in emptys)
            return all_is_empty
    else:
        return None


if __name__ == '__main__':
    pass