from enum import Enum
class Cmelement(Enum):
    userName = {'key':'xpath','value':'//*[@id="username"]'}
    
    passWord = {'key':'xpath','value':'//*[@id="password"]'}
    login = {'key':'xpath','value':'//*[@id="loginform"]/button'}
    skip = {'key':'xpath','value':'/html/body/div[15]/div/div[5]/a[1]'}
    bbx={'key':'xpath','value':'//*[@id="app"]'}
    mbness={'key':'xpath','value':'//*[@id="moreAPPs"]/ul[1]/li[1]/a'}
    cname={'key':'xpath','value':'//*[@id="content"]/div[7]/div[1]/div[2]/input'}
    cadress={'key':'xpath','value':'//*[@id="content"]/div[7]/div[2]/div[2]/input'}
    cip={'key':'xpath','value':'//*[@id="content"]/div[7]/div[3]/div[2]/input'}
    phone={'key':'xpath','value':'//*[@id="content"]/div[7]/div[4]/div[3]/input'}
    OK={'key':'xpath','value':'//*[@id="content"]/div[7]/div[8]/div/input'}