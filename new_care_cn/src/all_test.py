#coding=utf-8

import time
import unittest
from HTMLTestRunner import HTMLTestRunner


def createHTML():
    #创建可以运行所有脚本的discover
    start_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(start_dir, 
                                                   pattern = 'test_*.py', 
                                                   top_level_dir = None)
    #创建html报告
    
    nowTime = time.strftime('%Y-%m-%d %H：%M：%S', time.localtime(time.time()))
    fileName = './report/'+nowTime+'_result.html'
    print fileName
    stream = open(fileName,'wb')
    
    run = HTMLTestRunner(stream = stream,
                         title = u"care业务系统自动化测试报告",
                         description = u"用例执行情况")
    
    run.run(discover)
    stream.close()
    
if __name__ == "__main__" :
    createHTML()