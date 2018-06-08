#coding:utf-8
import urllib2
from bs4 import BeautifulSoup as BS
import re
import re
import requests
import http.cookiejar
from PIL import Image
import time
import json

# print response.read()
#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
线程中发消息
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import threading
import time


# class Main(QDialog):
#     def __init__(self):
#         QDialog.__init__(self)
#         self.pbProcess = QPushButton("&amp;amp;amp;OK")
#         self.leResult = QLineEdit("")
#
#         layout = QHBoxLayout(self)
#         for w in self.pbProcess, self.leResult:
#             layout.addWidget(w)
#
#         self.connect(self.pbProcess, SIGNAL("clicked()"),
#                      self.process)
#         # self.connect(self, SIGNAL("waitProcess()"),
#         #              self.waitProcess,Qt.QueuedConnection)#, Qt.QueuedConnection)
#
#     def process(self):
#         threading.Thread(target=self.threadRun).start()
#
#     def threadRun(self):
#         time.sleep(3)
#         self.emit(SIGNAL("waitProcess()"))
#         print "sended.."
#
#     def waitProcess(self):
#         time.sleep(3)
#         self.leResult.setText("hello！")
#
# def main():
#     app = QApplication([])
#     Main().exec_()
#
# if __name__=="__main__":
#     main()

# response = urllib2.urlopen(
#                "https://shopee.com.my/mezowatch")
# print response.read()
# '''
data={"captcha":"",
      "captcha_key":"0a3c42dcb15e470c83ebd2c0ed7271df",
      "email":"kangdekai@gmail.com",
      "password_hash":"f79d4cca1417209abdf13ce7ed7275427f1d5c72cd7316f716e79683014b607f",
      "remember":"false"}

headers={'Host': 'seller.shopee.com.my',
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
# SPC_EC=-; SPC_F=3pSLvDrguo02XxrsVAoks5Iqz4QOd0c9; SPC_U=-; cto_lwid=b82b8f2f-cc24-40fd-9adc-f5a516c07d44; language=zhHans; SPC_T_IV="XdYIPdwpVxa6/ZXLUrVYEA=="; SPC_SC_TK=; SPC_T_ID="HHuOZKlEafA1gukSS9rb+Qj73ZeHgB8XYkaFwCWG4cOF7WLqO5eINh1xnEZSl/L7261sxB3nZ6TKEq6gsIiFNczMy2GJh0A7jNbfVrmUHc0="; SPC_T_F=1; SPC_SC_UD=; _ga=GA1.3.1939319452.1527731027; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22812562d7-1133-4c57-8a79-a2528aab53f4%22; _ga=GA1.4.1939319452.1527731027; SPC_SI=tlpozgtpogi6j4xqdm8dp8bj16jwequ1; _gid=GA1.3.753135685.1528117564; _gid=GA1.4.753135685.1528117564; SPC_CDS=2021afb4-58b7-4b78-965c-9afdb662914e; root_csrftoken=2df00ec1-36be-45a5-9b17-f156169bcfdb; UYOMAPJWEMDGJ=
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
#                          '(KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
#            "Host": "www.zhihu.com",
#            "Referer": "https://www.zhihu.com/",
#            }
# 建立一个会话，可以把同一用户的不同请求联系起来；直到会话结束都会自动处理cookies
session = requests.Session()
# 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
# 而MozillaCookieJar类是存为'/.txt'格式的文件
session.cookies = http.cookiejar.LWPCookieJar("cookie")
# 若本地有cookie则不用再post数据了
try:
    session.cookies.load(ignore_discard=True)
except IOError:
    print('Cookie未加载！')

cookies_var=(session.cookies._cookies)
# print cookies_var['.shopee.com.my']['/']['SPC_EC'].value
# print cookies_var['.shopee.com.my']['/']['SPC_SC_TK'].value
# print cookies_var['.shopee.com.my']['/']['SPC_SC_UD'].value
# print cookies_var['.shopee.com.my']['/']['SPC_U'].value
#
# print cookies_var['seller.shopee.com.my']['/']['SPC_T_F'].value
# print cookies_var['seller.shopee.com.my']['/']['SPC_T_ID'].value
# print cookies_var['seller.shopee.com.my']['/']['SPC_T_IV'].value

# {'.shopee.com.my': {'/': {'SPC_SC_TK': Cookie(version=0, name='SPC_SC_TK', value='78e0098120050b74604a2c3b489f82b8', port=None, port_specified=False, domain='.shopee.com.my', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=True, expires=1528724702, discard=False, comment=None, comment_url=None, rest={'httponly': 'None'}, rfc2109=False), 'SPC_EC': Cookie(version=0, name='SPC_EC', value='"3AoUL9B50ZT6KChuFx9wXbHNyPyuonTT1vReMVPn3pbxWgUolX2Px2C7ERMn0gHTj1H+tARKJ8ty3tCx69nD98WxBegKF9rYRWfyE9ZBbyuQbHpU7OgwqmwIoOR8LFhZKYZOu7oIv2xsjVU4cvCRcQ=="', port=None, port_specified=False, domain='.shopee.com.my', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=True, expires=1528724702, discard=False, comment=None, comment_url=None, rest={'httponly': 'None'}, rfc2109=False), 'SPC_SC_UD': Cookie(version=0, name='SPC_SC_UD', value='72014359', port=None, port_specified=False, domain='.shopee.com.my', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=True, expires=1528724702, discard=False, comment=None, comment_url=None, rest={'httponly': 'None'}, rfc2109=False), 'SPC_U': Cookie(version=0, name='SPC_U', value='72014359', port=None, port_specified=False, domain='.shopee.com.my', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=True, expires=1528724702, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)}}, 'seller.shopee.com.my': {'/': {'SPC_T_IV': Cookie(version=0, name='SPC_T_IV', value='"cOikHwuPCNCOC5vAy021iQ=="', port=None, port_specified=False, domain='seller.shopee.com.my', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=2158839902, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), 'SPC_T_ID': Cookie(version=0, name='SPC_T_ID', value='"Vnquxfq0UqLmYrp2s6oR7PC+vDLNKTFHYbcCCfLt3cE5LIzV744h6LEyAhY1exDtNL99kvksajcQoOVnsYty/LAwueRUBZMNHKHLOyKy34Q="', port=None, port_specified=False, domain='seller.shopee.com.my', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=2158839902, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), 'SPC_T_F': Cookie(version=0, name='SPC_T_F', value='0', port=None, port_specified=False, domain='seller.shopee.com.my', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=2158839902, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)}}}

# print type(session.cookies)
'''
def get_xsrf():
    """
    获取参数_xsrf
    """
    response = session.get('https://seller.shopee.com.my/api/v1/login/', headers=headers)
    html = response.text
    get_xsrf_pattern = re.compile(r'<input type="hidden" name="_xsrf" value="(.*?)"')
    _xsrf = re.findall(get_xsrf_pattern, html)[0]
    return _xsrf


def get_captcha():
    """
    获取验证码本地显示
    返回你输入的验证码
    """
    t = str(int(time.time() * 1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    response = session.get(captcha_url, headers=headers)
    with open('cptcha.gif', 'wb') as f:
        f.write(response.content)
    # Pillow显示验证码
    im = Image.open('cptcha.gif')
    im.show()
    captcha = input('本次登录需要输入验证码： ')
    return captcha


def login(username, password):
    url="https://seller.shopee.com.my/"
    # url="https://seller.shopee.com.my/api/v1/login/"

    # 若不用验证码，直接登录
    result = session.post(url, data=data, headers=headers)
    print result
    session.cookies.save(ignore_discard=True, ignore_expires=True)


def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://shopee.com.my/user/account/profile/"
    # 禁止重定向，否则登录失败重定向到首页也是响应200
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False
# response=urllib2.urlopen("https://seller.shopee.com.my/api/v1/login/?SPC_CDS=92886269-4e0d-40b4-94a5-3b871d054239&SPC_CDS_VER=2",
#                 data=data)
# print response.read()
# response = urllib2.urlopen("https://shopee.com.my/shop/37216574/followers/?__classic__=1")
# bsObj = BS(open('fans.html'), "html.parser")

# SPC_IA=-1;SPC_EC=riKzcmisPDuIa2cZIEycmELbt82C4GvNIU93pCvsOVlepmNqiOvkZSjXXgfyBWtgEnEBVF4iLJqtqBsP015gEn0jVgv93pP3erK8tyV7Umeaki44EwSJefNegVpxbJVNUfbuBWd/P8/iq/16JJ2k6Q=="; SPC_F=3pSLvDrguo02XxrsVAoks5Iqz4QOd0c9; REC_T_ID=12ced1c4-6336-11e8-8aaa-5254009900d0; SPC_T_ID="DrAXkvnWiwKhdiQ/UyNvIb7QlPfViVGHZ3690OKvZi68rI9B2I21Ah7fsSsasZ7H0lRIANV9Y6gCt0Ayr2sTUJTJ7EID9BAHwtg86JC6oQY="; SPC_U=72014359; SPC_T_IV="pv04KAKF1vLDO7Zq+pCD+g=="; cto_lwid=b82b8f2f-cc24-40fd-9adc-f5a516c07d44; csrftoken=nzIzvMrqvmObU4vCRlmsTnj9sJMhMY6N; language=zhHans; SPC_SC_TK=acb8a6655d89068cb54ed948cbf59932; SPC_SC_UD=72014359; _ga=GA1.3.1939319452.1527731027; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22812562d7-1133-4c57-8a79-a2528aab53f4%22; SPC_SI=vgy4v1vajxpi534ac5nmnhq258mcht9a; _gid=GA1.3.753135685.1528117564; bannerShown=true; root_csrftoken=36ac1a21-f5e0-4d57-b1e2-3d16b08da994; UYOMAPJWEMDGJ=
def follow(userid):
    url="https://shopee.com.my/buyer/follow/shop/71339404/"
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
                     'Referer': 'https://shopee.com.my/shop/37216574/followers/?__classic__=1',
                     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
                     'X-Requested-With': 'XMLHttpRequest'}
    # follow_header={}
    follow_cookies={
    '_ga':'GA1.3.1939319452.1527731027',
    '_gid':'GA1.3.753135685.1528117564',
    'ajs_anonymous_id':"812562d7-1133-4c57-8a79-a2528aab53f4",
    'ajs_group_id':'null',
    'ajs_user_id':'null',
    'csrftoken':'nzIzvMrqvmObU4vCRlmsTnj9sJMhMY6N',
    'cto_lwid':'b82b8f2f-cc24-40fd-9adc-f5a516c07d44',
    'language':'zhHans',
    'REC_T_ID':'12ced1c4-6336-11e8-8aaa-5254009900d0',
    'root_csrftoken':'2df00ec1-36be-45a5-9b17-f156169bcfdb',
    'SPC_EC':"C1B4pfQTPrV83PbewOBmcnvHo2LnyxcUGfjRIUBGJCNP90Ab7NnL/k03yMW8gLO+E+ulf8AravgVlvt5xRtmrnYbIaK4YTLn4fFgA4aQsME/vPTqaX4kWwLIfXKJoomd7kJedxCvDSgz1I6c6MIjKg==",
    'SPC_F':'3pSLvDrguo02XxrsVAoks5Iqz4QOd0c9',
    'SPC_IA': '-1',
    'SPC_SC_TK':'39518c9898f86347a90a3d3e3cc82f8d',
    'SPC_SC_UD':'72014359',
    'SPC_SI':'tlpozgtpogi6j4xqdm8dp8bj16jwequ1',
    'SPC_T_ID':"KVpf+khKX6CipghWdYZfNq4/YqqP3qcyuNO5/4FDZmmdMF1I5yRT+Kz04boQ5mbBDkumOnB1L0KI8IHVhMz6FZUGKYQ5prqYB5/O0WZl/HI=",
    'SPC_T_IV':"Q6H3O9GE1X20BdAXbqR6FQ==",
    'SPC_U':'72014359',
    'UYOMAPJWEMDGJ':''
    }
    follow_data={"csrfmiddlewaretoken":"nzIzvMrqvmObU4vCRlmsTnj9sJMhMY6N"}
    # result=session.post(url, data=follow_data, headers=follow_header,cookies=session.cookies)
    result = requests.post(url, data=follow_data, headers=follow_header,cookies=follow_cookies)
    print result

def login(username, password):
    """
    输入自己的账号密码，模拟登录知乎
    """
    # 检测到11位数字则是手机登录
    # if re.match(r'\d{11}$', username):
    #     url = 'http://www.zhihu.com/login/phone_num'
    #     data = {'_xsrf': get_xsrf(),
    #             'password': password,
    #             'remember_me': 'true',
    #             'phone_num': username
    #             }
    # else:
    #     url = 'https://www.zhihu.com/login/email'
    #     data = {'_xsrf': get_xsrf(),
    #             'password': password,
    #             'remember_me': 'true',
    #             'email': username
    #             }
    # url="https://seller.shopee.com.my/"
    url="https://seller.shopee.com.my/api/v1/login/"

    # 若不用验证码，直接登录
    result = session.post(url, data=data, headers=headers)
    print result
    # 打印返回的响应，r = 1代表响应失败，msg里是失败的原因
    # loads可以反序列化内置数据类型，而load可以从文件读取
    # if (json.loads(result.text))["r"] == 1:
    #     # 要用验证码，post后登录
    #     data['captcha'] = get_captcha()
    #     result = session.post(url, data=data, headers=headers)
    #     print((json.loads(result.text))['msg'])
    #     # 保存cookie到本地
    session.cookies.save(ignore_discard=True, ignore_expires=True)
if __name__ == '__main__':
    if isLogin():
        print('您已经登录')
    else:
        print "使用账号密码登录"
    # account = input('输入账号：')
    # secret = input('输入密码：')
        account="kangdekai@gmail.com"
        secret="amtf1041583081"
        login(account, secret)
    follow("")
# '''

# '''

if 0:
    response = urllib2.urlopen(
        "https://shopee.com.my/shop/37216574/followers/?offset=0&limit=50&offset_of_offset=0&_=1527731021727&__classic__=1")
    # response = urllib2.urlopen("https://shopee.com.my/shop/37216574/followers/?__classic__=1")
    # bsObj = BS(open('fans.html'), "html.parser")
    bsObj = BS(response.read(), "html.parser")

    # bsObj=BS(response.read(),"html.parser")
else:
    bsObj = BS(open('fans_3.html'), "html.parser")
# fans = bsObj.select('div[class="up m14"] a')
# follow_dir=bsObj.select('div[shopid]')
# # fans=bsObj.find_all(re.compile("username="))
# print len(fans)
fans_dir = {}
# for i,fan in enumerate(fans):
#     # print str(fan)
#     if follow_dir[i].next==u"关注中":
#         fans_dir[(fan.attrs["userid"])] = [(fan.attrs["username"]),True]
#     else:
#         fans_dir[(fan.attrs["userid"])] = [(fan.attrs["username"]),False]

fans = bsObj.select('li[data-follower-shop-id]')
for fan in fans:
    # shopid=fan.attrs[u'data-follower-shop-id']
    shopid=fan.attrs[u'data-follower-shop-id']
    user=fan.contents[1]
    username=user.attrs['username']
    userid=user.attrs['userid']
    follow=fan.contents[5].text
    print userid,username,unicode(follow)
    is_follow =(fan.contents[5].text).find(u'关注中')>=0
    fans_dir[userid]=[username,shopid,is_follow]

print fans_dir
# print follow_dir
'''
'''
bsObj = BS(open('profile.html'), "html.parser")

username = bsObj.select('div[class="user-page-brief__username"]')
print username[0].contents[0]
# '''
