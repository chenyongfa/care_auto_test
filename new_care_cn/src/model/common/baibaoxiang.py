#coding=utf-8

# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from contant.contant import Contant
from model.common.cm_element import Cmelement
from utils.utils import getElement
def clbbx(self):
    
    try:
        WebDriverWait(self.driver, 5,0.5).until(EC.presence_of_element_located((By.XPATH,Cmelement.bbx['value'])))
        getElement(self,Cmelement.bbx).click()
    except :
        print u'百宝箱点击错误'
    