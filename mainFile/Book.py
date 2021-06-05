import requests
import json
from bs4 import BeautifulSoup
from bs4.element import Tag


class Book:

    def __init__(self, thor):
        self.thor = thor

    # 快速下单
    def book(self, goodsId, num=1):
        self.getRid(goodsId, num)

    def getRid(self, goodsId, num):
        response = requests.get(
            'https://easybuy.jd.com/skuDetail/newSubmitEasybuyOrder.action?callback=easybuysubmit&skuId=' + goodsId + '&num=' + str(
                num) + '&gids=&ybIds=&did=&useOtherAddr=false', headers={
                'Referer': 'https://item.jd.com/' + goodsId + '.html',
            }, cookies={
                'thor': self.thor
            })
        print(response.text[14:-2])
        rp = json.loads(response.text[14:-2])
        if rp['success']:
            self.quickBook(rp['jumpUrl'])

    def checkCoupon(self, url):
        response = requests.get('https://trade.jd.com/shopping/dynamic/coupon/getCoupons.action', headers={
            'Referer': url
        }, cookies={
            'thor': self.thor
        })
        soup = BeautifulSoup(response.text, 'html5lib')
        c = soup.select('.coupon-enable .coupon-item')
        return len(c) > 0

    def getBestCoupon(self, url):
        response = requests.get('https://trade.jd.com/shopping/dynamic/coupon/getBestVertualCoupons.action', headers={
            'Referer': url
        }, cookies={
            'thor': self.thor
        })

    def quickBook(self, jumpUrl):
        self.getBestCoupon(jumpUrl)
        response = requests.post('https://trade.jd.com/shopping/order/submitOrder.action', cookies={
            'thor': self.thor
        }, headers={
            'Referer': 'https:' + jumpUrl,
            'Host': 'trade.jd.com',
            'User-Agent': 'Mozilla/5.0(X11;Ubuntu;Linux x86_64;rv:63.0)Gecko/20100101Firefox/63.0'
        }, data={
            # 'overseaPurchaseCookies': '',
            # 'vendorRemarks': [{"venderId":"62710","remark":""}],
            # 'submitOrderParam.sopNotPutInvoice': True,
            # 'submitOrderParam.trackID': 'TestTrackId',
            # 'submitOrderParam.ignorePriceChange': 0,
            # 'submitOrderParam.btSupport': 0,
            # 'submitOrderParam.eid': '2NHYCD75HVHYYFLNK2VL3SZHGCJG4A2RORK6MF2UZCMT3G2LZSESKSZHYSK6ZYMGQ6JL7P3WUTO3ZVNYXTBG25MSDU',
            # 'submitOrderParam.fp': 'c2a009aec6339079c3a0c78eafe08816',
            # 'riskControl': 'D0E404CB705B9732FD97C4DFCA0B7A95B67DC1EAD150767F35CF7976744D2B1AB4DDE2EB88B501AC',
            # 'submitOrderParam.jxj': 1,
            # 'submitOrderParam.trackId': '8517a2ea6c588e2d7a3540034e7bfe37'
        })
        if json.loads(response.text)['success']:
            print('success!!!')
        else:
            print('failed!!!')

    def setData(self, soup, data):
        data['submitOrderParam.btSupport'] = self.__getBtSupport(soup)

    def __getBtSupport(self, soup):
        tags: Tag = soup.findAll(attrs={'class': 'payment-item', 'onlinepaytype': 1})
        if not tags:
            return 0
        for tag in tags:
            tag: Tag
            if 'payment-item-disabled' in tag.get('class'):
                return 0
        return 1
