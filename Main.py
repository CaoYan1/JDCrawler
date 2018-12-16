from Coupon import Coupon
from Login import Login
from Book import Book

if __name__ == '__main__':
    config = open('config','r+')
    thor = config.readline()
    if not thor or thor == '':
        #登录获取thor(扫码登录)
        loginObj = Login()
        loginObj.login()
        thor = loginObj.get()
        config.write(thor)
    config.close()
    #根据商品的id快速下单
    b = Book(thor)
    b.book('27752137726',1)

    #根据券的id领取优惠券
    c = Coupon(thor)
    c.getCoupon('a89a85ebee8296dc65bd776f4a1d414e4e224464bb14bd65f5e822c44ff2854868dffebfbaa256891583cb0c75b53605')

