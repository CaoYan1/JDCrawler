import random
import requests
import cv2
import threading
import time
import numpy as np
import json

class Login():

    LOGIN_URL = 'https://passport.jd.com/new/login.aspx'
    QRCODE_URL = 'http://qr.m.jd.com/show?appid=133&size=147&t='
    CHECK_URL = 'https://qr.m.jd.com/check?callback=jQuery8392893&appid=133&token='

    def __init__(self):
        self.thor = ''
        self.cap = cv2.VideoCapture()
        self.t = ''
        self.wlfstk_smdl = ''
        self.QRCodeKey = ''
        self.loginSuccess = False

    def get(self):
        return self.thor

    def login(self):
        self.__getQRcode()

    def __getThor(self,ticket):
        headers = {
            'Referer': 'https://passport.jd.com/new/login.aspx?ReturnUrl=https//www.jd.com'
        }
        response = requests.get('https://passport.jd.com/uc/qrCodeTicketValidation?t='+ticket,headers=headers)
        self.thor = response.cookies.get('thor')



    def __queryThread(self):
        success = False
        print(self.CHECK_URL + self.wlfstk_smdl + '&_=' + self.t)
        cookies = {
            'wlfstk_smdl':self.wlfstk_smdl,
            'QRCodeKey':self.QRCodeKey
        }
        headers = {
            'Referer': 'https://passport.jd.com/uc/login?ltype=logout'
        }
        while not success:
            result = requests.get(self.CHECK_URL + self.wlfstk_smdl + '&_=' + self.t,cookies = cookies,headers=headers).text
            result = result[14:-1]
            result = json.loads(result)
            print(result)
            code = result['code']
            if code == 200:
                self.__getThor(result['ticket'])
                success = True
                cv2.destroyAllWindows()
            else:
                print(result['msg'])
            time.sleep(2)


    def __getQRcode(self):
        code = []
        for i in range(13):
            code.append(str(random.randint(0,9)))
        self.t = ''.join(code)
        print((self.QRCODE_URL + self.t))
        response = requests.get(self.QRCODE_URL + self.t)
        self.wlfstk_smdl = response.cookies.get('wlfstk_smdl')
        self.QRCodeKey = response.cookies.get('QRCodeKey')
        img_arr = np.asarray(bytearray(response.content), dtype='uint8')
        img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        cv2.imshow('a',img)
        threading.Thread(target = self.__queryThread,daemon=True).start()

        while cv2.waitKey()&0xff == ord('q'):
            return







