import requests

class Coupon():

    def __init__(self,thor):
        self.thor = thor

    # 要领取券的key
    def getCoupon(self,couponKey):
        header = {
            'Referer': 'https://a.jd.com/',
        }
        cookies = {
            'thor': self.thor
        }
        html = requests.get(
            'https://a.jd.com/indexAjax/getCoupon.html?callback=jQuery3906318&key=' + couponKey + '&type=1',
            headers=header, cookies=cookies)
        print(html.text)

