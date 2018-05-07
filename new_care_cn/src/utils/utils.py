#coding=utf-8
from email import email
from email.mime.image import MIMEImage
import os

# from contant.contant import Contant


def getElement(self, selector):
    """
    to locate element by selector
    :arg
    selector should be passed by an example with "i,xxx"
    "x,//*[@id='langs']/button"
    :returns
    DOM element
    """
    key = selector['key']
    value = selector['value']

    if key in ['i','I','id','ID','Id']:
        element = self.driver.find_element_by_id(value)
    elif key in ['x','X','xpath','Xpath','XPATH']:
        element = self.driver.find_element_by_xpath(value)
    elif key in ['c','C','class_name','Class_name','CLASS_NAME']:
        element = self.driver.find_element_by_class_name(value)
    elif key in ['l','L','link_text','Link_text','LINK_TEXT']:
        element = self.driver.find_element_by_link_text(value)
    elif key in ['p','P','partial_link_text','Partial_link_text','PARTIAL_LINK_TEXT']:
        element = self.driver.find_element_by_partial_link_text(value)
    elif key in ['t','T','tag_name','Tag_name','TAG_NAME']:
        element = self.driver.find_element_by_tag_name(value)
    elif key in ['n','N','name','Name','NAME']:
        element = self.driver.find_element_by_name(value)
    elif key in ['c','C','css_selector','Css_selector','CSS_SELECTOR']:
        element = self.driver.find_element_by_css_selector(value)
    else:
        raise NameError("Please enter a valid type of targeting elements.")

    return element

def getElements(self, selector):
    """
    to locate elements by selector
    :arg
    selector should be passed by an example with "i,xxx"
    "x,//*[@id='langs']/button"
    :returns
    DOM elements
    """
    key = selector['key']
    value = selector['value']

    if key in ['i','I','id','ID','Id']:
        elements = self.driver.find_elements_by_id(value)
    elif key in ['x','X','xpath','Xpath','XPATH']:
        elements = self.driver.find_elements_by_xpath(value)
    elif key in ['c','C','class_name','Class_name','CLASS_NAME']:
        elements = self.driver.find_elements_by_class_name(value)
    elif key in ['l','L','link_text','Link_text','LINK_TEXT']:
        elements = self.driver.find_elements_by_link_text(value)
    elif key in ['p','P','partial_link_text','Partial_link_text','PARTIAL_LINK_TEXT']:
        elements = self.driver.find_elements_by_partial_link_text(value)
    elif key in ['t','T','tag_name','Tag_name','TAG_NAME']:
        elements = self.driver.find_elements_by_tag_name(value)
    elif key in ['n','N','name','Name','NAME']:
        elements = self.driver.find_elements_by_name(value)
    elif key in ['c','C','css_selector','Css_selector','CSS_SELECTOR']:
        elements = self.driver.find_elements_by_css_selector(value)
    else:
        raise NameError("Please enter a valid type of targeting elements.")

    return elements

def inputText(self,selector,text):
    """
           作用：向输入框中输入文字
           用法：xxx.imputText({'key'='i','valu'e='el'},"selenium")
           
    """
#     print text
    el = getElement(self,selector)
    el.clear()
    el.send_keys(text)
    
def sendMail():
    import smtplib
    from email.mime.text import MIMEText
     
    my_sender='nova_hemy@126.com'    # 发件人邮箱账号
    my_pass = '123456abcd'              # 发件人邮箱密码
    my_user='nova_chenyf@126.com,nova_hemy@126.com,nova_yaomin@126.com,nova_heyuancs@126.com'     # 收件人邮箱账号，我这边发送给自己
    
    msg = email.MIMEMultipart.MIMEMultipart()
    
    msg1=MIMEText(open(new_report()).read(),'html','utf-8')
    
    
    #添加二进制附件  
      
    ctype = 'application/octet-stream'  
    maintype, subtype = ctype.split('/', 1)  
    att1 = MIMEImage(open(new_report()).read(), _subtype = subtype)
    fileName = new_report().split("\\")[1]  
    att1.add_header('Content-Disposition', 'attachment', filename = fileName)  
    msg.attach(att1)  
    
    
    
    msg.attach(msg1)
    msg['From']=my_sender  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=my_user            # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="care系统自动化测试报告"                # 邮件的主题，也可以说是标题

    server=smtplib.SMTP("smtp.126.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
    server.set_debuglevel(1)
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender,my_user.split(','),msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit() # 关闭连接
     
   
        
def new_report():
    result_dir = 'F:/work_space/new_care_cn/src/report'
    list = os.listdir(result_dir)
    file = os.path.join(result_dir,list[-1])
    print file
    return file
    
    
    
if __name__ =="__main__":
    sendMail()    

