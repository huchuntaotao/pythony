#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import HTMLTestRunner
import os

class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    @classmethod
    def setUpClass(self):
    # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('11111')
        
    def setUp(self):
        # 每个测试用例执行之前做操作
        print('--------------->')  
         
    def test_a_run(self):
        print "test_a_run"
        self.assertEqual(1, 1)  # 测试用例
        
    def test_b_run(self):
        print "test_b_run"
        self.assertEqual(2, 2)  # 测试用例
        
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('<---------------')

    @classmethod
    def tearDownClass(self):
    # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('22222')
         
        
if __name__ == '__main__':
    unittest.main()#运行所有的测试用例
    
    suite = unittest.TestSuite() # 测试用例集
    #suite.addTest(MyTest('test_a_run')) #加入某个类中一个测试用例
    #suite.addTest(unittest.makeSuite(MyTest)) #加入某个类中所有测试用例
    
    all_cases = unittest.defaultTestLoader.discover('.', 'test_*.py') #所有的以test开头的Python文件里面的测试用例
    for case in all_cases: #把所有的测试用例添加进来
        suite.addTests(case)
    
    with open('result.html', 'wb+') as fp: #打开一个保存结果的html文件
        #生成执行用例的对象
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='api测试报告',description='测试结果')
        #执行测试套件
        runner.run(suite)