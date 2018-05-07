import time 
import unittest

# from contant.contant import Contant
from model.common.login import logIn
from model.common.logout import loginout
from model.common.baibaoxiang import clbbx

class A(unittest.TestCase):
    def test_a(self):
         
        logIn(self)
        print 'test role'
        time.sleep(2)
        clbbx(self)
        print 'test role'
        
        print 'test role'
        
        print 'test role'
        
        time.sleep(1)
        print 'test role'
        self.assertTrue(True)
        loginout(self)
    def runTest(self):
        pass


if __name__ == "__main__":
    B = A()
    B.test_a()