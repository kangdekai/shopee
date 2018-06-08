#coding:utf-8
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import threading
import urllib2
from bs4 import BeautifulSoup as BS
import thread
import requests
import http.cookiejar
import hashlib
qtCreatorFile = "main.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
# global fans_dir
# fans_dir={}
# class Get_fans_thread(QThread):
#     def __int__(self):
#         super(Get_fans_thread, self).__init__()
#     trigger=pyqtSignal()
#     def run(self):
#         # for i in range(203300030):
#         #     pass
#         # response = urllib2.urlopen("https://shopee.com.my/shop/37216574/followers/?offset=0&limit=5&offset_of_offset=0&_=1527731021727&__classic__=1")
#         response = urllib2.urlopen("https://shopee.com.my/shop/37216574/followers/?__classic__=1")
#         # bsObj = BS(open('fans.html'), "html.parser")
#         bsObj=BS(response.read(),"html.parser")
#
#         # print bsObj.prettify()
#         # print "title----\n",bsObj.title
#         # print bsObj.a.string
#         # print bsObj.find_all('class="up m14"')
#         fans = bsObj.select('div[class="up m14"] a')
#         # fans=bsObj.find_all(re.compile("username="))
#         print len(fans)
#         fans_dir = {}
#         for fan in fans:
#             # print str(fan)
#             fans_dir[(fan.attrs["userid"])] = (fan.attrs["username"])
#             # re.compile('username=.userid=.',unicode(fan.string))
#             # print fan.select("userid")
#             # print bsObj.h
#             # print response.read()
#             # print fans_dir
#         self.trigger.emit()  # 循环完毕后发出信号
#


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp,self).__init__()

        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.usr_login_pushButton.clicked.connect(self.user_login_f)#登录按钮
        self.query_fans_pushButton.clicked.connect(self.query_fans_f)#查询粉丝按钮
        self.flw_fans_pushButton.clicked.connect(self.flw_fans_f)#关注粉丝按钮
        self.connect(self, SIGNAL("show_fans_tableWidget()"),
                     self.show_fans_tableWidget)  # , Qt.QueuedConnection)
        self.connect(self,SIGNAL("edit_login_status_label()"),
                     self.edit_login_status_label)
        self.connect(self,SIGNAL("change_flw_status()"),
                     self.change_flw_status)
        self.session = requests.Session()
        # 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
        # 而MozillaCookieJar类是存为'/.txt'格式的文件
        self.session.cookies = http.cookiejar.LWPCookieJar("cookie")
        # 若本地有cookie则不用再post数据了
        try:
            self.session.cookies.load(ignore_discard=True)
        except IOError:
            print('Cookie未加载！')
        threading.Thread(target=self.is_log_f, args=()).start()
    def is_log_f(self):
        url = "https://shopee.com.my/user/account/profile/"

        headers = {'Host': 'seller.shopee.com.my',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Language': 'en-GB,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Referer': 'https://seller.shopee.com.my/account/signin?next=index.index&params=%5B%5D',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Content-Length': '175',
                   # 'Cookie': 'SPC_EC=-; SPC_F=3pSLvDrguo02XxrsVAoks5Iqz4QOd0c9; SPC_SI=x1g26ks9f6j6j8145kubi6hss2pynyaa; SPC_U=-; cto_lwid=b82b8f2f-cc24-40fd-9adc-f5a516c07d44; language=zhHans; SPC_T_IV="mz9FW/Qf+tJ+Son30b6h9Q=="; SPC_SC_TK=; SPC_T_ID="iyi6SRAQ6Ki9qWyhR9uSuMEa51myfhe0RfIk2S06DG6ntEqUU6b9yengSda3q7Wgdm/wsAPkLDKUzvppz7OLGVl12NZGC9qyqxa5IDA7avE="; SPC_T_F=0; SPC_SC_UD=; _ga=GA1.3.1939319452.1527731027; _gid=GA1.3.1679379021.1527731027; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22812562d7-1133-4c57-8a79-a2528aab53f4%22; SPC_CDS=92886269-4e0d-40b4-94a5-3b871d054239; root_csrftoken=bf23ada2-92ca-406f-b4a2-62775b2fa2ac; UYOMAPJWEMDGJ=; _ga=GA1.4.1939319452.1527731027; _gid=GA1.4.1679379021.1527731027',
                   'Cookie': 'SPC_EC=-; SPC_F=3pSLvDrguo02XxrsVAoks5Iqz4QOd0c9; SPC_U=-; cto_lwid=b82b8f2f-cc24-40fd-9adc-f5a516c07d44; language=zhHans; SPC_T_IV="XdYIPdwpVxa6/ZXLUrVYEA=="; SPC_SC_TK=; SPC_T_ID="HHuOZKlEafA1gukSS9rb+Qj73ZeHgB8XYkaFwCWG4cOF7WLqO5eINh1xnEZSl/L7261sxB3nZ6TKEq6gsIiFNczMy2GJh0A7jNbfVrmUHc0="; SPC_T_F=1; SPC_SC_UD=; _ga=GA1.3.1939319452.1527731027; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22812562d7-1133-4c57-8a79-a2528aab53f4%22; _ga=GA1.4.1939319452.1527731027; SPC_SI=tlpozgtpogi6j4xqdm8dp8bj16jwequ1; _gid=GA1.3.753135685.1528117564; _gid=GA1.4.753135685.1528117564; SPC_CDS=2021afb4-58b7-4b78-965c-9afdb662914e; root_csrftoken=2df00ec1-36be-45a5-9b17-f156169bcfdb; UYOMAPJWEMDGJ=',
                   'Connection': 'keep-alive'
                   }
        response = self.session.get(url, headers=headers, allow_redirects=False)
        # print response.text
        login_code=response.status_code
        if login_code == 200:
            self.login_status=True
            self.selfuserid=self.session.cookies._cookies['.shopee.com.my']['/']['SPC_SC_UD'].value
            print "login success"
        else:
            self.login_status=False
            print "login false"


        # bsObj = BS(response.text, "html.parser")
        # username = bsObj.select('div[class="user-page-brief__username"]')
        # print username[0].contents[0]
        self.emit(SIGNAL("edit_login_status_label()"))
        pass
    def user_login_f(self):
        usn_str=unicode(self.usn_textEdit.toPlainText())
        pwd_str=unicode(self.pwd_textEdit.toPlainText())
        threading.Thread(target=self.login_thread,args=(usn_str,pwd_str)).start()
        print usn_str,pwd_str
        print "log in button"
    def query_fans_f(self):
        threading.Thread(target=self.get_fans_table,args=(self,)).start()
    def flw_fans_f(self):
        userid_item_list=self.fans_tableWidget.selectedItems()
        # print userid_list
        userid_list=[]
        for idx in range(len(userid_item_list)/(self.fans_dir_attrs_num+1)):
            userid=unicode(userid_item_list[(self.fans_dir_attrs_num+1)*idx].text())
            userid_list.append(userid)
        threading.Thread(target=self.flw_fans_thread, args=(userid_list,)).start()
        # print result
        pass
    def flw_fans_thread(self,userid_list):
        cookies_var = (self.session.cookies._cookies)
        SPC_EC_STR= cookies_var['.shopee.com.my']['/']['SPC_EC'].value
        SPC_SC_TK_STR= cookies_var['.shopee.com.my']['/']['SPC_SC_TK'].value
        SPC_SC_UD_STR= cookies_var['.shopee.com.my']['/']['SPC_SC_UD'].value
        SPC_U_STR= cookies_var['.shopee.com.my']['/']['SPC_U'].value

        SPC_T_F_STR= cookies_var['seller.shopee.com.my']['/']['SPC_T_F'].value
        SPC_T_ID_STR= cookies_var['seller.shopee.com.my']['/']['SPC_T_ID'].value
        SPC_T_IV_STR= cookies_var['seller.shopee.com.my']['/']['SPC_T_IV'].value
        follow_header = {'Accept': '*/*',
                         'Accept-Encoding': 'gzip, deflate, br',
                         'Accept-Language': 'en-GB,en;q=0.5',
                         'Connection': 'keep-alive',
                         'Content-Length': '52',
                         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                         # 'Cookie': 'SPC_IA=-1; SPC_EC='+cookies_var['.shopee.com.my']['/']['SPC_EC'].value+'; _gat=1; _gat_gtm=1',
                         # 'Cookie': 'SPC_IA=-1; SPC_EC='+''+'; _gat=1; _gat_gtm=1',

                         'Host': 'shopee.com.my',
                         'If-None-Match-': '55b03-09900f96bf034b0960cc3c8908ac98da',
                         'Referer': 'https://shopee.com.my/shop/37216500/followers/?__classic__=1',
                         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
                         'X-Requested-With': 'XMLHttpRequest'}
        # follow_header={}
        follow_cookies = {
            '_ga': 'GA1.3.1939319452.1527731027',
            '_gid': 'GA1.3.753135685.1528117564',
            'ajs_anonymous_id': "812562d7-1133-4c57-8a79-a2528aab53f4",
            'ajs_group_id': 'null',
            'ajs_user_id': 'null',
            'csrftoken': 'nzIzvMrqvmObU4vCRlmsTnj9sJMhMY6N',
            'cto_lwid': 'b82b8f2f-cc24-40fd-9adc-f5a516c07d44',
            'language': 'zhHans',
            'REC_T_ID': '12ced1c4-6336-11e8-8aaa-5254009900d0',
            'root_csrftoken': '2df00ec1-36be-45a5-9b17-f156169bcfdb',
            'SPC_EC': SPC_EC_STR,
            'SPC_F': '3pSLvDrguo02XxrsVAoks5Iqz4QOd0c9',
            'SPC_IA': '-1',
            'SPC_SC_TK': SPC_SC_TK_STR,
            'SPC_SC_UD': SPC_SC_UD_STR,
            'SPC_SI': 'tlpozgtpogi6j4xqdm8dp8bj16jwequ1',
            'SPC_T_ID': SPC_T_ID_STR,
            'SPC_T_IV': SPC_T_IV_STR,
            'SPC_U': SPC_U_STR,
            'UYOMAPJWEMDGJ': ''
        }
        follow_data = {"csrfmiddlewaretoken": "nzIzvMrqvmObU4vCRlmsTnj9sJMhMY6N"}
        # flw_scs_num=0
        success_userid_list=[]
        for userid in userid_list:
            # url = "https://shopee.com.my/buyer/follow/shop/71339404/"
            follow_url = "https://shopee.com.my/buyer/follow/shop/"+(self.fans_dir[userid][1])+"/"
            print "follow url:",follow_url
            # result=session.post(url, data=follow_data, headers=follow_header,cookies=session.cookies)
            result = requests.post(follow_url, data=follow_data, headers=follow_header, cookies=follow_cookies)
            print result
            if result.status_code==200:
                success_userid_list.append(userid)
            print "success userid list",success_userid_list
        self.changed_userid_list=userid_list
        self.success_userid_list=success_userid_list

        self.emit(SIGNAL("change_flw_status()"))

        pass
    def change_flw_status(self):
        if len(self.changed_userid_list) > len(self.success_userid_list):
            QMessageBox.warning(self.centralWidget(), u"警告", str(len(self.changed_userid_list)-len(self.success_userid_list))+u"位用户关注失败！")
        for userid in self.success_userid_list:
            self.fans_dir[userid][2]=True
        self.emit(SIGNAL('show_fans_tableWidget()'))
        pass
    def login_thread(self,username,pwd):
        # url = "https://seller.shopee.com.my/"
        username="kangdekai@gmail.com"
        pwd="Amtf1041583081"
        url="https://seller.shopee.com.my/api/v1/login/"

        # 若不用验证码，直接登录
        data = {"captcha": "",
                "captcha_key": "0a3c42dcb15e470c83ebd2c0ed7271df",
                "email":username,
                "password_hash": (hashlib.sha256((hashlib.md5(pwd).hexdigest())).hexdigest()),
                "remember": "false"}

        headers = {'Host': 'seller.shopee.com.my',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Language': 'en-GB,en;q=0.5',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Referer': 'https://seller.shopee.com.my/account/signin?next=index.index&params=%5B%5D',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Content-Length': '175',
                   # 'Cookie': 'SPC_EC=-; SPC_F=3pSLvDrguo02XxrsVAoks5Iqz4QOd0c9; SPC_SI=x1g26ks9f6j6j8145kubi6hss2pynyaa; SPC_U=-; cto_lwid=b82b8f2f-cc24-40fd-9adc-f5a516c07d44; language=zhHans; SPC_T_IV="mz9FW/Qf+tJ+Son30b6h9Q=="; SPC_SC_TK=; SPC_T_ID="iyi6SRAQ6Ki9qWyhR9uSuMEa51myfhe0RfIk2S06DG6ntEqUU6b9yengSda3q7Wgdm/wsAPkLDKUzvppz7OLGVl12NZGC9qyqxa5IDA7avE="; SPC_T_F=0; SPC_SC_UD=; _ga=GA1.3.1939319452.1527731027; _gid=GA1.3.1679379021.1527731027; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22812562d7-1133-4c57-8a79-a2528aab53f4%22; SPC_CDS=92886269-4e0d-40b4-94a5-3b871d054239; root_csrftoken=bf23ada2-92ca-406f-b4a2-62775b2fa2ac; UYOMAPJWEMDGJ=; _ga=GA1.4.1939319452.1527731027; _gid=GA1.4.1679379021.1527731027',
                   'Cookie': 'SPC_EC=-; SPC_F=3pSLvDrguo02XxrsVAoks5Iqz4QOd0c9; SPC_U=-; cto_lwid=b82b8f2f-cc24-40fd-9adc-f5a516c07d44; language=zhHans; SPC_T_IV="XdYIPdwpVxa6/ZXLUrVYEA=="; SPC_SC_TK=; SPC_T_ID="HHuOZKlEafA1gukSS9rb+Qj73ZeHgB8XYkaFwCWG4cOF7WLqO5eINh1xnEZSl/L7261sxB3nZ6TKEq6gsIiFNczMy2GJh0A7jNbfVrmUHc0="; SPC_T_F=1; SPC_SC_UD=; _ga=GA1.3.1939319452.1527731027; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22812562d7-1133-4c57-8a79-a2528aab53f4%22; _ga=GA1.4.1939319452.1527731027; SPC_SI=tlpozgtpogi6j4xqdm8dp8bj16jwequ1; _gid=GA1.3.753135685.1528117564; _gid=GA1.4.753135685.1528117564; SPC_CDS=2021afb4-58b7-4b78-965c-9afdb662914e; root_csrftoken=2df00ec1-36be-45a5-9b17-f156169bcfdb; UYOMAPJWEMDGJ=',
                   'Connection': 'keep-alive'
                   }
        result = self.session.post(url, data=data, headers=headers)
        # print result
        if result.status_code==200:
            self.session.cookies.save(ignore_discard=True, ignore_expires=True)
            self.login_status=True
        else:
            self.login_status = False
            # QMessageBox.warning(self.centralWidget(),u"警告",u"用户名或密码错误！")
        self.emit(SIGNAL("edit_login_status_label()"))


        pass
    def edit_login_status_label(self):
        if self.login_status:
            self.login_status_label.setText(u"欢迎，"+self.selfuserid)
        else:
            QMessageBox.warning(self.centralWidget(), u"警告", u"用户名或密码错误！")
    def show_fans_tableWidget(self):
        table = self.fans_tableWidget
        table.setRowCount(100)
        table.setColumnCount(self.fans_dir_attrs_num+1)

        # Enter data onto Table
        horHeaders = [u"用户ID", u"用户名",u"商店ID",u"关注状态"]
        # horHeaders = ["userid", "username","follow status"]
        for n, key in enumerate(sorted(self.fans_dir.keys())):
            newitem0 = QtGui.QTableWidgetItem(key)
            newitem1 = QtGui.QTableWidgetItem(self.fans_dir[key][0])
            newitem2 = QtGui.QTableWidgetItem(self.fans_dir[key][1])
            newitem3=None
            table.setItem(n, 0, newitem0)
            table.setItem(n, 1, newitem1)
            table.setItem(n, 2, newitem2)
            if self.fans_dir[key][2]:
                newitem3 = QtGui.QTableWidgetItem(u'已关注')
            else:
                newitem3 = QtGui.QTableWidgetItem(u'未关注')
            table.setItem(n, 3, newitem3)
        # Add Header
        table.setHorizontalHeaderLabels(horHeaders)

        # Adjust size of Table
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

    # def get_fans_table2(self):
    #     get_fans_thread=Get_fans_thread()
    #     get_fans_thread.start()
    #     get_fans_thread.trigger.connect(self.timeStop)
    def get_fans_table(self,store_id):
        cookies_var = (self.session.cookies._cookies)
        SPC_EC_STR = cookies_var['.shopee.com.my']['/']['SPC_EC'].value
        SPC_SC_TK_STR = cookies_var['.shopee.com.my']['/']['SPC_SC_TK'].value
        SPC_SC_UD_STR = cookies_var['.shopee.com.my']['/']['SPC_SC_UD'].value
        SPC_U_STR = cookies_var['.shopee.com.my']['/']['SPC_U'].value

        SPC_T_F_STR = cookies_var['seller.shopee.com.my']['/']['SPC_T_F'].value
        SPC_T_ID_STR = cookies_var['seller.shopee.com.my']['/']['SPC_T_ID'].value
        SPC_T_IV_STR = cookies_var['seller.shopee.com.my']['/']['SPC_T_IV'].value
        fans_cookies = {
            '_ga': 'GA1.3.1939319452.1527731027',
            '_gat':'1',
            '_gat_gtm':'1',
            '_gid': 'GA1.3.753135685.1528117564',
            'ajs_anonymous_id': "812562d7-1133-4c57-8a79-a2528aab53f4",
            'ajs_group_id': 'null',
            'ajs_user_id': 'null',
            'csrftoken': 'nzIzvMrqvmObU4vCRlmsTnj9sJMhMY6N',
            'cto_lwid': 'b82b8f2f-cc24-40fd-9adc-f5a516c07d44',
            'language': 'zhHans',
            'REC_T_ID': '12ced1c4-6336-11e8-8aaa-5254009900d0',
            'root_csrftoken': '2df00ec1-36be-45a5-9b17-f156169bcfdb',
            'SPC_EC': SPC_EC_STR,
            'SPC_F': '3pSLvDrguo02XxrsVAoks5Iqz4QOd0c9',
            'SPC_IA': '-1',
            'SPC_SC_TK': SPC_SC_TK_STR,
            'SPC_SC_UD': SPC_SC_UD_STR,
            'SPC_SI': 'tlpozgtpogi6j4xqdm8dp8bj16jwequ1',
            'SPC_T_ID': SPC_T_ID_STR,
            'SPC_T_IV': SPC_T_IV_STR,
            'SPC_U': SPC_U_STR,
            'UYOMAPJWEMDGJ': ''
        }
        headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'en-GB,en;q=0.5',
                   'Connection': 'keep-alive',
                   'Host': 'shopee.com.my',
                   'Upgrade-Insecure-Requests':'1',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',

                   }
        fan_data={'__classic__':1}
        # response = urllib2.urlopen("https://shopee.com.my/shop/37216574/followers/?offset=0&limit=5&offset_of_offset=0&_=1527731021727&__classic__=1")
        # response = urllib2.urlopen("https://shopee.com.my/shop/36228301/followers/?__classic__=1")
        if 1:
            # response = urllib2.urlopen(
            #     "https://shopee.com.my/shop/37216574/followers/?offset=0&limit=50&offset_of_offset=0&_=1527731021727&__classic__=1")
            # response = urllib2.urlopen("https://shopee.com.my/shop/37216500/followers/?__classic__=1")
            # response = self.session.get("https://shopee.com.my/shop/37216501/followers/?__classic__=1",headers=headers,cookies=fans_cookies)
            response = self.session.get("https://shopee.com.my/shop/37216574/followers/?__classic__=1")
            # response = self.session.get("https://shopee.com.my/shop/37216574/followers/?__classic__=1",cookies=self.session.cookies)
            if response.status_code!=200:
                print 'query fans table status code:',response.status_code
                pass
                # QMessageBox.warning(self.centralWidget(), u"警告",u"获取粉丝列表失败，错误码："+str(response.status_code))

            # bsObj = BS(open('fans.html'), "html.parser")
            bsObj = BS(response.content, "html.parser")

            # bsObj=BS(response.read(),"html.parser")
        else:
            bsObj = BS(open('fans_3.html'), "html.parser")
        self.fans_dir={}
        fans = bsObj.select('li[data-follower-shop-id]')
        for fan in fans:
            shopid = fan.attrs[u'data-follower-shop-id']
            user = fan.contents[1]
            username = user.attrs['username']
            userid = user.attrs['userid']
            # follow=fan.contents[5].text
            # print userid,username,unicode(follow)
            is_follow = (fan.contents[5].text).find(u'关注中') >= 0
            print userid,username,is_follow
            self.fans_dir_attrs_num=3
            self.fans_dir[userid] = [username, shopid, is_follow]
        self.emit(SIGNAL("show_fans_tableWidget()"))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())