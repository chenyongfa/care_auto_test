#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from contant.contant import Contant
from model.common.cm_element import Cmelement
from utils.utils import getElement, inputText


def logIn(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(3)
    self.driver.get(Contant.baseUrl1)
    self.driver.maximize_window()
    print Cmelement.userName
    print Contant.userName
    inputText(self,Cmelement.userName,Contant.userName)
    inputText(self,Cmelement.passWord,Contant.passWord1)
    getElement(self,Cmelement.login).click()
    try:
        WebDriverWait(self.driver, 5,0.5).until(EC.presence_of_element_located((By.XPATH,Cmelement.skip['value'])))
        getElement(self,Cmelement.skip).click()
    except :
        print '没有出现跳过弹窗'
    
    
