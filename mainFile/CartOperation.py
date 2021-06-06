import requests
import random

class CartOperation():
    def __init__(self, thor):
        self.thor = thor

    #购物车全选
    def selectAll(self):
        response = requests.post('https://cart.jd.com/selectAllItem.action', headers={
            'Referer': 'https://cart.jd.com/cart.action'
        }, cookies={
            'thor': self.thor
        }, data={
            # 'locationId':'17-1381-50713-52576',
            # 'outSkus':None,
            # 't':0,
            # 'random':0.93
        })

    #购物车全取消
    def cancelAll(self):
        response = requests.post('https://cart.jd.com/cancelAllItem.action',headers={
            'Referer': 'https://cart.jd.com/cart.action'
        },cookies={
            'thor': self.thor
        })

    #选中单个商品
    def selectItem(self,pid,targetId,ptype):
        response = requests.post('https://cart.jd.com/selectItem.action?rd'+str(random.random()),headers={
            'Referer': 'https://cart.jd.com/cart.action'
        },cookies={
            'thor': self.thor
        },data={
            # 'packId' : 0,
            'pid' : '3488558',  #商品号
            'promoID' : '50000061698',  #不知道是啥,但必须带着
             'ptype' : 11,    #同上
            'targetId' : '50000061698' #同上
            # 't' : 0,
            # 'targetId' : 0,
            # 'venderId' : 8888
        })

