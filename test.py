from bs4 import BeautifulSoup
from bs4.element import Tag
html = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="expires" content="0" /> 
    <meta name="format-detection" content="telephone=no" />  
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" /> 
    <meta name="format-detection" content="telephone=no" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>订单结算页 -京东商城</title>
	<!--结算页面样式-->	
	<link rel="stylesheet" href="//sp.jd.com/payment/1.2.0/css/bankList.css" charset="utf-8">
						<link type="text/css" rel="stylesheet"  href="//misc.360buyimg.com/user/purchase/2.0.0/widget/??common/common.css,header-2017/header-2017.css,consignee-scroll/consignee-scroll.css,consignee-selfpick/consignee-selfpick.css,payment-step/payment-step.css,presale-step/presale-step.css,shopping-list/shopping-list.css,invoice-dialog/invoice-dialog.css,order-virtual/order-virtual.css,order-summary/order-summary.css,checkout-floatbar/checkout-floatbar.css,paypwd/paypwd.css,/delivery-calendar-freight/delivery-calendar-freight.css,backpanel/backpanel.css" source="widget"/>
				<link type="text/css" rel="stylesheet"  href="//misc.360buyimg.com/jdf/1.0.0/unit/??ui-base/5.0.0/ui-base.css,shortcut/5.0.0/shortcut.css,global-header/5.0.0/global-header.css,myjd/5.0.0/myjd.css,nav/5.0.0/nav.css,shoppingcart/5.0.0/shoppingcart.css,global-footer/5.0.0/global-footer.css,service/5.0.0/service.css"/>
		<script type="text/javascript" src="//misc.360buyimg.com/jdf/lib/jquery-1.6.4.js"></script>
		<script type="text/javascript" src="//misc.360buyimg.com/jdf/1.0.0/unit/??base/5.0.0/base.js,basePatch/1.0.0/basePatch.js"></script>
		<script type="text/javascript" src="//misc.360buyimg.com/user/purchase/2.0.0/js/cookieTrack_v4.js"></script>
	
	<script type="text/javascript" src="//trade.jd.com/shopping/misc/js/order.common.js?r=20180208"></script>
	<script type="text/javascript" src="//trade.jd.com/shopping/misc/js/jquery.checkout.js?v=03091"></script>
    <script type="text/javascript"  src="//trade.jd.com/static/js/lib/other/class.mini.js" /></script>
</head>	<body id="mainframe">
		<!--shortcut start-->
<div id="shortcut-2014">
	<div class="w">
    	<ul class="fl">
    		<li id="ttbar-home"><i class="iconfont">&#xe608;</i><a href="//www.jd.com/" target="_blank">京东首页</a></li>
    		<li class="dorpdown" id="ttbar-mycity"></li>
    	</ul>
    	<ul class="fr">
			<li class="fore1" id="ttbar-login">
				<a href="javascript:login();" class="link-login">你好，请登录</a>&nbsp;&nbsp;<a href="javascript:regist();" class="link-regist style-red">免费注册</a>
			</li>
			<li class="spacer"></li>
			<li class="fore2">
				<div class="dt">
					<a target="_blank" href="//order.jd.com/center/list.action">我的订单</a>
				</div>
			</li>
			<li class="spacer"></li>
			<li class="fore3 dorpdown" id="ttbar-myjd">
				<div class="dt cw-icon">
					<!-- <i class="ci-right"><s>◇</s></i> -->
					<a target="_blank" href="//home.jd.com/">我的京东</a><i class="iconfont">&#xe605;</i>
				</div>
				<div class="dd dorpdown-layer"></div>
			</li>
			<li class="spacer"></li>
			<li class="fore4" id="ttbar-member">
				<div class="dt">
					<a target="_blank" href="//vip.jd.com/">京东会员</a>
				</div>
			</li>
			<li class="spacer"></li>
			<li class="fore5"   id="ttbar-ent">
				<div class="dt">
					<a target="_blank" href="//b.jd.com/">企业采购</a>
				</div>
			</li>
			<li class="spacer"></li>
			<li class="fore6 dorpdown" id="ttbar-serv">
				<div class="dt cw-icon">
					<!-- <i class="ci-right"><s>◇</s></i> -->
					客户服务<i class="iconfont">&#xe605;</i>
				</div>
				<div class="dd dorpdown-layer"></div>
			</li>
			<li class="spacer"></li>
			<li class="fore7 dorpdown" id="ttbar-navs">
				<div class="dt cw-icon">
					<!-- <i class="ci-right"><s>◇</s></i> -->
					网站导航<i class="iconfont">&#xe605;</i>
				</div>
				<div class="dd dorpdown-layer"></div>
			</li>
			<li class="spacer"></li>
			<li class="fore8 dorpdown" id="ttbar-apps">
				<div class="dt cw-icon">
					<!-- <i class="ci-left"></i> -->
					<!-- <i class="ci-right"><s>◇</s></i> -->
					<a target="_blank" href="//app.jd.com/">手机京东</a>
				</div>
			</li>
    	</ul>
		<span class="clr"></span>
    </div>
</div>
<div id="o-header-2013"><div id="header-2013" style="display:none;"></div></div>
<!--shortcut end-->
<!--shortcut end-->


<div class="w w1 header clearfix">
    <!--<div id="logo">
                    <a href="http://www.jd.com/" class="link1" target="_blank"><img src="//misc.360buyimg.com/lib/img/e/logo-201305.png" alt="京东商城"></a>
                <a href="#none" class="link2"><b></b>"结算页"</a>
    </div>-->
            <div id="logo-2014">
            <a href="http://www.jd.com/" class="logo" target="_blank"></a>
            <a href="#none" class="link2"><b></b>"结算页"</a>
        </div>
    
    <div class="stepflex" id="#sflex03">
        <dl class="first done">
            <dt class="s-num">1</dt>
            <dd class="s-text">1.我的购物车<s></s><b></b></dd>
        </dl>
        <dl class="normal doing">
            <dt class="s-num">2</dt>
            <dd class="s-text">2.填写核对订单信息<s></s><b></b></dd>
        </dl>
        <dl class="normal last">
            <dt class="s-num">3</dt>
            <dd class="s-text">3.成功提交订单<s></s><b></b></dd>
        </dl>
    </div>
</div>

<!-- /header -->
<!--/ /widget/header/header.tpl -->

<div id="consignee_back" name="consignee_back" style="display:none"></div>
<div id="consignee_back_action" name="consignee_back_action" style="display:none"></div>
<div id="part-invoice_back" name="part-invoice_back" style="display:none"></div>
<div id="part-invoice_back_action" name="part-invoice_back_action" style="display:none"></div>
<div id="payment-ship_back_action" name="payment-ship_back_action" style="display:none"></div>
<div id="payment-ship_back" name="payment-ship_back" style="display:none"></div>
<input type="hidden" name="beforePickSiteId" id="beforePickSiteId"><!--自提点-->
<input type="hidden" name="beforePickDate" id="beforePickDate"><!--自提时间-->
<input type="hidden" name="beforePickSiteNum" id="beforePickSiteNum"><!--默认5个-->
<input type="hidden" name="beforePickRegionId" id="beforePickRegionId" value="-1"><!--搜索区域-->
<input type="hidden" name="beforePickSelRegionid" id="beforePickSelRegionid"><!--搜索区域-->
<input type="hidden" id="beforePickName" name="beforePickName"/>
<input type="hidden" id="sopCartJson"/>
<input type="hidden" id="showInvoiceSeparate" value="true"><!-- 是否支持货票分离 -->
<input type="hidden" id="invoiceSeparateSwitch" value="1"><!-- 货票分离开关值 -->
<input type="hidden" id="hasBigItem" value="false">
<input type="hidden" id="hasGiftCardSku" value="false"/>
<input type="hidden" id="sopNotPutInvoice" value="false">
<input type="hidden" id="isChangeItemByArea" value="false"/>
<input type="hidden" id="hasTang9" value="false">
<input type="hidden" id="isHasSam" value="false"/>
<input type="hidden" id="needPay" value="5499.00"/>
<input type="hidden" id="consignee_id" name="consignee_id" value="138479095">
<input type="hidden" id="hideAreaIds"
       value="17-1381-50713-52576"/>

<input type="hidden" id="presaleStepPay" value=""/>
<input type="hidden" id="flowType" value=""/>
<input type="hidden" id="flowId" value=""/>
<input type='hidden' id="cur_payid" value="4">
<input type="hidden" id="showCheckCode" value="false"/>
<input type="hidden" id="reset_promise_311" value="0"/>
<input type="hidden" id="resetFlag" value="0000000000"/>
<input type="hidden" id="easyBuyFlag" value=""/>
<input type="hidden" id="ui-dialog-close" value=""/>
<input type="hidden" id="overseaPurchaseCookies" value=""/>
<input type="hidden" id="isHasSimCard" value="false">
<input type="hidden" id="ignorePriceChange" value="0">
<input type="hidden" id="canBaitiaoDetail" value="true"/>
<input type="hidden" id="getEquipInfo" value="true"/>
<input type="hidden" id="selfPickShutDownFlag" value="0">
<input type="hidden" id="selfPickOptimize" value="0">

<input type="hidden" id="secondHandFlag" value=""/>
<input type="hidden" id="TrackID" name="TrackID" value="TestTrackId"/>
<input type="hidden" id="invokeNewCouponInterface" name="invokeNewCouponInterface" value="true"/>
<input type="hidden" id="submitButtonABTest" value="0">
<input type="hidden" id="eid" value="" />
<input type="hidden" id="fp" value="" />
<input type="hidden" id="baitiaoPayRequest" value="plan=1" />
<input type="hidden" id="baitiaoPayRepayDateRequest" value="repayDate=" />
<input type="hidden" id="jdpy_cardInfo" value="nocard" />
<form id="direct_pay" action="https://cashier.jd.com/direct/directPay.action" method="post">
    <input type="hidden"  name="orderId"/>
    <input type="hidden"  name="toType"/>
    <input type="hidden"  name="orderType"/>
    <input type="hidden"  name="directPayInfoJson"/>
    <input type="hidden"  name="payMethod"/>
    <input type="hidden"  name="key"/>
    <input type="hidden"  name="countdownTime"/>
    <input type="hidden"  name="orderSubmitTime"/>
    <input type="hidden"  name="sendPayDict"/>
</form>
<input type="hidden" id="lastneedPay" value="5499.00"/>
<input type="hidden" id="btNeedPay" value="5499.00"/>
<input type="hidden" id="isNewVertual" name="isNewVertual" value="true"/>
<input type="hidden" id="isBestCoupon" name="isBestCoupon"/>
<input type="hidden" id="agreeNoRefundInMain" value="false"/>

<input type="hidden" id="allFreightWeight" value="2.680kg"/>
<input type="hidden" id="overFreightWeight" value=""/>
<input type="hidden" id="copywritingContent" value="0"/>
<input type="hidden" id="bigItemCopywritingContent" value="0"/>
<input type="hidden" id="normalCopywritingContent" value="0"/>
<input type="hidden" id="calendarCopywritingContent" value="0"/>
<input type="hidden" id="needForJZD" value="0"/>
<input type="hidden" id="needForJZDcalendar" value="0"/>
<input type="hidden" id="supportSelfPick" value="0"/>
<input type="hidden" id="workdayContent" value="0"/>
<input type="hidden" id="weekendContent" value="0"/>
<input type="hidden" id="supportByDay" value="0"/>
<input type="hidden" id="supportSop" value="0"/>
<input type="hidden" id="allSxFreightWeight" value=""/>
<input type="hidden" id="allWmFreightWeight" value=""/>
<input type="hidden" id="overSxFreightWeight" value=""/>
<input type="hidden" id="overWmFreightWeight" value=""/>
<input type="hidden" id="totalFreightWeightShow" value="2.680"/>
<input type="hidden" id="topTitleInfoUsed" value="1"/>
<input type="hidden" id="topTitleInfoFor315" value="1"/>
<input type="hidden" id="riskControl" value="D0E404CB705B97321DC526ECFF85E2673BC4425CAB2467EDB12D918EC44D8A1146E727F79E966021"/>
<input type="hidden" id="newReplacedFlow" value="true"/>
<input type="hidden" id="hongKongId" value="52993"/>
<input type="hidden" id="taiWanId" value="32"/>
<input type="hidden" id="hkId" value="52994"/>
<input type="hidden" id="mkId" value="52995"/>
<input type="hidden" id="overSeasId" value="53283"/>
<div class="replacedSkus hide">[]</div>
<input type="hidden" id="plusStatus" value="1"/>
<input type="hidden" id="totalPrice" value="0"/>
<div class="plusInfoConfig hide">{"plusInfos":[{"typeContent":"立即开通","clstag":"pageclick|keycount|201601152|50","url":"http://plus.jd.com/order/page","content":"开通PLUS会员，享受商品会员价","classInfo":null,"configId":0},{"typeContent":"立即开通","clstag":"pageclick|keycount|201601152|49","url":"http://plus.jd.com/order/page","content":"开通PLUS会员，享受商品会员价","classInfo":null,"configId":0},{"typeContent":"立即开通","clstag":"pageclick|keycount|201601152|48","url":"http://plus.jd.com/order/page","content":"开通PLUS会员，享受商品会员价","classInfo":null,"configId":0},{"typeContent":"立省运费","clstag":"pageclick|keycount|201601152|47","url":"http://plus.jd.com/index","content":"开通PLUS会员，每月送5张自营运费券","classInfo":null,"configId":0},{"typeContent":"立即开通","clstag":"pageclick|keycount|201601152|50","url":"http://plus.jd.com/order/page","content":"还在花运费？每月领5张自营运费券","classInfo":null,"configId":0},{"typeContent":"立省运费","clstag":"pageclick|keycount|201601152|50","url":"http://plus.jd.com/index","content":"开通会员PLUS，享受商品会员价","classInfo":null,"configId":0}],"classInfo":"com.jd.trade.app.common.config.PlusConfig","configId":26283}</div>
<input type="hidden" id="totalFreight" value=""/>
<div class="plusProductList hide">[]</div>
<input type="hidden" id="closeRefreshSelfpick" value="0"/>
<input type="hidden" id="enterPriseUser" value="false"/>
<input type="hidden" id="closeEnterPrisePayment" value="false"/>
<input type="hidden" id="useBestCoupons" value="1"/>
<input type="hidden" id="crossRegionalFee" value="0"/>
<div class="crossSku hide">null</div>
<input type="hidden" id="411content" value="0"/>
<input type="hidden" id="411content4save" value="0"/>
<input type="hidden" id="editConsignee" value="0"/>
<input type="hidden" id="delConsignee" value="0"/>
<input type="hidden" id="downUpdateSelfPick" value="0"/>
<input type="hidden" id="downRisktak" value="0"/>
<input type="hidden" id="newForcedChoice" value="0"/>
<input type="hidden" id="gsd_newForcedChoice" value="0"/>
<input type="hidden" id="311flag" value="0"/>
<input type="hidden" id="secondHandTag" value="订单中含有二手商品，购买前请">
<input type="hidden" id="secondHandMsg" value="查看购买提醒">
<input type="hidden" id="link2" value="https://help.jd.com/user/issue/195-559.html"/>
<input type="hidden" id="link3" value="https://help.jd.com/user/issue/235-631.html"/>
<input type="hidden" id="link4" value="https://help.jd.com/user/issue/232-627.html"/>
<input type="hidden" id="link5" value="https://help.jd.com/user/issue/79-88.html"/>
<input type="hidden" id="link10" value="http://help.jd.com/user/issue/239-3760.html"/>

<input type="hidden" id="xhmf" value="绿色环保，签收后配送员会现场将循环包装收回"/>
<input type="hidden" id="xhmftip" value="采用可多次使用的循环包装，签收时需将循环包装返还；签收当场将包装返还配送员的，赠送5个京豆。"/>
<input type="hidden" id="xhff" value="服务费用¥@，使用循环包装，签收当场返还得京豆"/>
<input type="hidden" id="xhfftip" value="采用可多次使用的循环包装，签收时需将循环包装返还；签收当场将包装返还配送员的，赠送5个京豆。"/>
<input type="hidden" id="sjxyh" value="7天内退货，15天内换货，预计获得@元运费赔付(到小金库)。"/>
<input type="hidden" id="sjxyhdt" value="7天内退货，15天内换货，预计获得1次运费赔付(到小金库)。"/>
<input type="hidden" id="second" value="false"/>
<!-- main -->
<div id="container">
    <div id="content" class="w">
        <!-- <div class="m"> -->
        <div class="orderInfo-tip hide">
            <span class="wicon"></span>
            <span class="ftx-03"> 温馨提示：订单中存在不支持7天无理由退换商品，请确认相关商品信息后提交订单。</span>
            <span class="cls-btn" onclick="closeorderInfotip()">x</span>
        </div>
        <div class="checkout-tit">
            <span class="tit-txt">填写并核对订单信息</span>
                                            </div>
        <!--<div class="mc">-->
        <div class="checkout-steps">
            <!--  /widget/consignee-step/consignee-step.tpl -->
            <div class="step-tit">
                <h3>收货人信息</h3>
                <div class="tips-new-white hide" id="tariffTip"><b></b><span>目的国/地区如产生关税及其它相关费用，需用户自行承担</span></div>
                <div class="tips-new-white hide" id="hkTip"><b></b><span>收货地址为住宅时，需向配送员支付住宅附加费：20港币/单</span></div>
                <div class="extra-r">
                                            <a href="#none" class="ftx-05 J_consignee_global" onclick="use_NewConsigneeOversea()">新增收货地址</a>
                                        <!--<a href="#none" class="ftx-05" onclick="use_NewConsignee()" clstag="pageclick|keycount|trade_201602181|3">新增收货地址</a>-->
                    <input type="hidden" id="del_consignee_type" value="0"/>
                </div>
            </div>
            <div class="step-cont">
                <div id="consignee-addr" class="consignee-content">
                    <div class="consignee-scrollbar">
                        <div class="ui-scrollbar-main">
                            <div class="consignee-scroll">
                                <div class="consignee-cont" id="consignee1">
                                                                        <ul id="consignee-list">
                                    <!---->
                                        <!--
<li class="ui-switchable-panel" id="consignee_index_138479095" selected="selected" style="cursor: pointer;">
	<div class="consignee-item item-selected" consigneeId="138479095" id="consignee_index_div_138479095">
		<b></b>
		<div class="user-name">
			<div class="fl"><strong limit="4">曹炎</strong>&nbsp;&nbsp;收</div>
			<div class="fr">176****3600</div>
			<div class="clr"></div>
		</div>
		<div class="mt10" limit="15">湖北 武汉市 江夏区 城区</div>
		<div class="adr-m" limit="30">武汉工程大学流芳校区泰塑公寓</div>
		<div class="op-btns ar">
							<span class='mr10'>默认地址</span>
									<a href="#none" class="ftx-05 mr10 edit-consignee" fid="138479095">编辑</a>
			<a href="#none" class="ftx-05 del-consignee hide" fid="138479095">删除</a>
		</div>
	</div>
</li>
-->

<li  class="ui-switchable-panel ui-switchable-panel-selected"    style="display: list-item;"  id="consignee_index_138479095" selected="selected" style="cursor: pointer;" c_li_custom_label="consignee_li">
	<div  class="consignee-item item-selected"  longitude="1000.0" gcLng="114.429961" latitude="1000.0" gcLat="30.459888" consigneeId="138479095" provinceId="17" cityId="1381" countyId="50713" id="consignee_index_div_138479095" consigneeType="0" clstag="pageclick|keycount|trade_201602181|1" c_div_custom_label="consignee_div">		
		<span limit="8" title="曹炎">曹炎</span><b></b>
	</div>
	<div class="addr-detail">
		<!--yanwenqi 全球购添加idcard 不是国际购的要不要显示？ -->
				 <span class="addr-name" limit="6">曹炎</span>
		 <span class="addr-info" limit="45">湖北 武汉市 江夏区 城区 武汉工程大学流芳校区泰塑公寓</span>
		 <span class="addr-tel">176****3600</span>
						<span class="addr-default">默认地址</span>
			</div>
	<div class="op-btns" consigneeId="138479095" isOldAddress="false">
		<span></span>				<a href="#none" class="ftx-05 edit-consignee" fid="138479095" clstag="pageclick|keycount|trade_201602181|6">编辑</a>
		<a href="#none" class="ftx-05 del-consignee hide" fid="138479095" clstag="pageclick|keycount|trade_201602181|5">删除</a>
	</div>
</li>

	             
       <!-- 地址升级提示:两种情况 -->      
              
       

          <!-- 地址升级隐藏域信息 -->
  	      <input type="hidden"
  	             id="hid_upArea_138479095"
  	             consigneeId="138479095"
	             isOldAddress="false"
	             isMapping="false"
	             newProvinceId="0"
	             newCityId="0"
	             newCountyId="0"
	             newTownId="0" 
	             newProvinceName=""
	             newCityName=""
	             newCountyName=""
	             newTownName=""
	             address_type="1"
	             addressName="曹炎"
	             name="曹炎"
	             email=""
	             mobile="176****3600"
	             phone="176****3600"
	             idCard="4202**********243X"
	             address="武汉工程大学流芳校区泰塑公寓"
	             ceshi1=""/>
	             
                                            <!-- -->
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="addr-switch switch-on" id="consigneeItemAllClick" onclick="show_ConsigneeAll()" clstag="pageclick|keycount|trade_201602181|2">
                    <span>更多地址</span><b></b>
                </div>
                <div class="addr-switch switch-off hide" id="consigneeItemHideClick"
                     onclick="hide_ConsigneeAll()">
                    <span>收起地址</span><b></b>
                </div>

                <div id = "selfPickArea" class="consignee-scroll mt10 hide">
                    <div class="consignee-cont">
                        <div class="hr" id="selfPickLine"></div>
                        <div class="picksite-lead hide" id="firstAccessTip">
                            <i class="pl-joy"></i>
                            <span class="pl-info">自提地址挪位置啦~根据您的配送习惯，<br>我们为您新增了京东自提点</span>
                            <span class="pl-btn" onclick='doHandleFirstAccess()'>我知道了</span>
                            <i class="pl-cls" onclick='doHandleFirstAccess()'></i>
                            <i class="pl-arrow"></i>
                        </div>
                    <ul id="selfPickInfo">
                                                                                    <li id="defaultSelfPick" defaultSelfPick="1">
                                    <div id="selfPickSiteName" class="consignee-item" clstag="pageclick|keycount|trade_201602181|40" onclick='doSelectSelfPickSite("125711","工程大学流芳校区京东派")'>
                                        <span id="pickName" pickId="125711" limit="8">京东自提点</span>
                                        <b></b>
                                    </div>
                                    <div class="addr-detail">
											<span class="addr-name" limit="6">
                                                曹炎
                                            </span>
                                        <span class="addr-info" limit="45">
												 工程大学流芳校区京东派 湖北省武汉市江夏区武汉工程大学流芳校区泰塑公寓进大门左转下坡100米（泰塑6栋对面）											</span>
                                        <span class="addr-tel">
                                            176****3600
                                        </span>
                                    </div>
                                    <div class="addr-ops">
                                        <a id = "selfPickEdit" href="#none" onclick="openEditSelfPickConsigneeDialog()" clstag="pageclick|keycount|trade_201602181|41" class="ftx-05 mr10 edit-selfconsignee hide" fid="125711">更换自提地址</a>
                                        <i class="pick-err-icon noPickChoose hide"></i><span class="ftx-01 mr10 noPickChoose hide">部分商品不支持</span>
                                        <a class="ftx-05 selfpick-edit selfPickChoose hide" href="#none" onclick="openEditSelfPickConsigneeDialog()">重新选择</a>
                                    </div>
                                </li>
                                                    </ul>
                                            </div>
                </div>
                <!--end-->
                                    <div class="picksite-scroll mt10">
                        <div class="picksite-cont">
                            <div class="hr hide" id="zitihr"></div>
                            <div id="zititype1" class="consignee-picksite-info mb10 mt10 hide">
                                <span class="c-picksite-logo">京东自提</span>
                                <span class="ftx-03 ml5" id="gaztqd1">随时取</span>
                                <a target='_blank' href="http://help.jd.com/user/issue/100-965.html" class="ftx-05 ml10 J_picksite_desc_btn">详情</a>
                            </div>
                            <div id="zititype2" class="consignee-picksite-info mb10 mt10 hide">
                                <span class="c-picksite-logo">京东自提</span>
                                <span class="ftx-01 ml5" id="absMoney">随时取</span>
                                <a target='_blank' href="http://help.jd.com/user/issue/100-965.html" class="ftx-05 ml10 J_picksite_desc_btn">详情</a>
                            </div>
                            <div id="zititype3" class="consignee-picksite-info mb10 mt10 hide">
                                <span class="c-picksite-logo">京东自提</span>
                                <span class="ftx-01 ml5" id="gaztqd2">周末没人？使用京东自提 随时取</span>
                                <a target='_blank' href="http://help.jd.com/user/issue/100-965.html" class="ftx-05 ml10 J_picksite_desc_btn">详情</a>
                            </div>
                            <div id="zititype5" class="consignee-picksite-info mb10 mt10 hide">
                                <span class="c-picksite-logo">京东自提</span>
                                <span class="ftx-01 ml5" id="gaztqd3">抱歉，存在不支持自提的商品或该地址下没有可用的自提点</span>
                                <a target='_blank' href="http://help.jd.com/user/issue/100-965.html" class="ftx-05 ml10 J_picksite_desc_btn">详情</a>
                            </div>
                            <ul id="selfPickOptimizeUl">
                            </ul>
                        </div>
                    </div>

                    <div id="zititype4" class="picksite-nosuport-cont hide">
                        <span class="tips-cont ml10"><b></b>订单中部分商品不支持自提，暂无法使用京东自提</span>
                        <a href="#none" class="ftx05 J_picksite_disable_info ml30">详情&nbsp;></a>
                        <div class="picksite-nosuport-box">
                            <i class="arrow-up"></i>
                            <strong>以下商品不支持自提</strong>
                            <ul id="unSupportSelfPickSkuList">
                            </ul>
                        </div>
                    </div>
                
                                    <input type="hidden" id="consigneeList_giftSenderConsigneeMobile"
                           value="">
                    <input type="hidden" id="consigneeList_giftSenderConsigneeName"
                           value="">
                            </div>
            <!--/ /widget/consignee-step/consignee-step.tpl -->
            <div class="hr"></div>
                        <!--/ /widget/shopping-list/shopping-list.tpl -->
            <div id="shipAndSkuInfo">
                <div id="payShipAndSkuInfo">
                    <div class="step-tit">
  <h3>支付方式</h3>
</div>
<div type="hide"></div>
<input type="hidden" id="totalPriceVender" value="0"/>
<input type="hidden" id="totalNumVender" value="0"/>
<div class="plusProductListVender hide">[]</div>
<input type="hidden" id="crossRegionalFeeVender" value=""/>
<div class="crossSkuVender hide"></div>
<div class="step-cont">
  <div class="payment-list" id="">
    <div class="list-cont">
          <ul id="payment-list">
        <input type="hidden" id="instalmentPlan" value="false">
		
													
		      
        			<!-- 是否限制该支付方式 -->
						<li style="cursor: pointer;" onclick="
									 save_Pay(1,0,1); 				" 
								clstag="pageclick|keycount|trade_201602181|8"											    												>

				<div class=" payment-item  online-payment " for="pay-method-1"
					payname="货到付款" payid="1" onlinePayType="0"><b></b>
					    					货到付款<span class="qmark-icon qmark-tip" data-tips="送货上门后再收款，支持现金、POS机刷卡、支票支付 <a href='//help.jd.com/user/issue/103-983.html' target='_blank' class='ftx-05'>查看服务及配送范围</a>"></span>					                    													                                																</div>
			</li>
			
            
					<!-- 是否限制该支付方式 -->
						<li style="cursor: pointer;" onclick="
				save_Pay(4,0,1);" 
				clstag="pageclick|keycount|trade_201602181|7"															    												>

				<div class=" payment-item item-selected online-payment " for="pay-method-4"
					payname="在线支付" payid="4" onlinePayType="0"><b></b>
																	<em class="payment-promo">惠</em> 
												在线支付                    													                <span id="cod" class="qmark-icon qmark-tip" data-tips="即时到账，支持绝大数银行借记卡及部分银行信用卡 <a href='//help.jd.com/user/issue/223-562.html' target='_blank' class='ftx-05'> 查看银行及限额</a>"></span>                 																</div>
			</li>
			
            
					<!-- 是否限制该支付方式 -->
						<li style="cursor: pointer;" onclick="
				save_Pay(5,0,1);" 
												clstag="pageclick|keycount|trade_201602181|9"							    												>

				<div class="hide payment-item  online-payment " for="pay-method-5"
					payname="公司转账" payid="5" onlinePayType="0"><b></b>
																	公司转账                    													                                												<span class="qmark-icon qmark-tip" data-tips="通过快钱平台转账 转账后1-3个工作日内到账 <a href='//help.jd.com/user/issue/list-175.html' target='_blank' class='ftx-05'>查看账户信息</a>"></span> 				</div>
			</li>
			
            
				<li id="payment-less" class="hide">
          <div class="payment-item-on" clstag="pageclick|keycount|PaymentLead__2016030411|10">
            <span>收起</span><b></b>
          </div>
        </li>
        <li id="payment-more">
          <div class="payment-item-off" clstag="pageclick|keycount|PaymentLead__2016030411|9">
            <span>更多</span><b></b>
          </div>
        </li>


<script>
$('.online-payment')
.hover(function(){
	$(this).addClass('payment-item-hover');
},function(){
	$(this).removeClass('payment-item-hover');
}); 
if($("#payment-list li").length<=4){
	$('#payment-less').hide();
	$('#payment-more').hide();
	var payid=[5,2,8];
	for(var i in payid){
		$("#payment-list div[payid="+payid[i]+"]").show();
	}
}
$('.payment-item-on').click(function(){
	$('#payment-less').hide();
	$('#payment-more').show();
	var payid=[5,2,8];
	for(var i in payid){
		var payment = $("#payment-list div[payid="+payid[i]+"]");
		if(!payment.hasClass("item-selected")){
			payment.hide(100);
		}
	}
});
$('.payment-item-off').click(function(){
	$('#payment-less').show();
	$('#payment-more').hide();
	var payid=[5,2,8];
	for(var i in payid){
		var payment = $("#payment-list div[payid="+payid[i]+"]");
		if(!payment.hasClass("item-selected")){
			payment.show(100);
		}
	}
});
</script>
              </ul>
          </div>
  </div>
</div>
<div class="hr"></div>
<!--/ /widget/payment-step/payment-step.tpl -->
<div class="step-tit">
  <h3>送货清单</h3>
	<div id="secondHint" class="tips-new-white hide"></div>
  <div class="extra-r">
  	<a class="price-desc" id="price-desc" href="#none" data-tips="因可能存在系统缓存、页面更新导致价格变动异常等不确定性情况出现，商品售价以本结算页商品价格为准。">
  		<i></i>&nbsp;价格说明
  	</a>
          <a href="//cart.jd.com" id="cartRetureUrl" class="return-edit ftx-05" clstag="pageclick|keycount|trade_201602181|15">返回修改购物车</a>
      </div>
</div>
<div class="step-cont" id="skuPayAndShipment-cont">
  <!--添加商品清单  zhuqingjie -->
  <div class="shopping-lists" id="shopping-lists"> 
           <!--定义大商品清单LIST-->
	<div class="hide" id="skuDetailInfo" notOneMainsku="false"></div>
	    <div class="shopping-list ABTest">
        <div class="goods-list">

			          <!--购物车单品商品-->
                      <!--一般套装商品-->
           <!--满返套装商品-->
         <!--满赠套装商品-->
           <!--配送方式-->
    <div class="goods-tit">
        <h4 class="vendor_name_h vendor_name_0" id="0">商家：京东自营</h4>
    </div>

    <!--单品开始-->
    <div class="goods-items">     								                                 <div data-service=""></div>
        <div class="goods-item goods-item-extra" goods-id="6072622" sx-type="0">
    
				<div class="p-img">
					<a target="_blank" href="http://item.jd.com/6072622.html?dist="><img src="//img14.360buyimg.com/N4/jfs/t28210/176/166163755/271400/2e654ec0/5bea36b6N79ca2695.jpg" alt=""></a>
    				        							</div>
				<div class="goods-msg">
		          <div class="goods-msg-gel">			
		  					<div class="p-name">
															                            <!-- 京东精选 begin -->
		  					                                <!-- 生鲜 begin -->
                                                                 <!-- 生鲜 end -->
                                
                    <a href="http://item.jd.com/6072622.html?dist=" target="_blank">
                          联想ThinkPad 翼480（0VCD）英特尔8代酷睿14英寸轻薄窄边框笔记本电脑（i5-8250U 8G 128GSSD+500G 2G独显）
                    </a>
                </div>
                                <div class="p-price ">
				                <!--增加预售金额显示 begin   预售分阶段支付类型（1：一阶梯全款支付；2：一阶梯定金支付(全款或定金可选)；3：三阶梯(仅定金)；4：三阶梯(全款或定金可选)；5：一阶梯仅定金支付） -->


                                                            <strong class="jd-price">
                                                            ￥ 5499.00

                            																	                        </strong>
                                                    <!--增加预售金额显示 end-->
                <span class="p-num">
                                                                        x1
                                                            </span>
                <span id="pre-state" class="p-state" skuId="6072622">有货</span>
                                    <span class="p-weight">2.680kg</span>
                                                    
                                                                    </div>
            </div>
                            </div>
            <!-- 颜色尺码以及车型begin -->
                        	<div class="p-extra-continer">
                   <div class="p-extra-line">
	                   	                    <div class="fl"><strong>颜色：</strong><span>冰原银</span></div>
	                   	                    	                    <div class="fl"><strong>尺码：</strong><span>i5-CPU</span></div>
	                                      </div>
                                </div>
                         <!-- 颜色尺码以及车型end -->
                <div class="p-icon-continer">
                                        <i class="p-icon p-icon-w sevenicon"></i><span class="ftx-07 withouthk seven">支持7天无理由退货（激活后不支持）
                                        <!-- 京尊达 begin -->
                    <!-- 京尊达 end -->
                </div>
                
                <div class="clr"></div>
                                    						<div class="gift-item ftx-03"  gift-id="3230620" gift-img="//img14.360buyimg.com/N4/jfs/t2737/349/2990798208/183631/5f57c7b7/577cc2e7Ne0245882.jpg" gift-name="ThinkPad（4X40L08937）皮质单肩背包T300" gift-num="1" gift-price="0.00" gift-uri="http://item.jd.com/3230620.html" gift-type="1">
                            							<p>【赠品】 &nbsp;ThinkPad（4X40L08937）皮质单肩背包T300 ×1&nbsp;&nbsp;<a href="http://item.jd.com/3230620.html" target="_blank" class="gift-price">查看价格</a></p>
                                                    </div>
                                                    <!-- 家具服务相关-->
                                                                    <!-- 山姆会员专享价 begin -->
                                <!-- 山姆会员专享价 end -->
                <!-- 京券和东券显示 -->
                

				  <!-- 延保显示 -->
				  					 				                   <!--服务 -->
                                                       				  				  <!-- 京东礼品购礼品盒展示 -->
				  				  
				  <!-- 京东loc门店展示 -->
				  
            </div>
            </div>
    <!--单品结束-->
    <!--一般套装开始-->
                <!--一般套装结束-->
        <!--满返套装开始-->
                <!--满返套装结束-->
        <!--满赠套装开始-->
                <!--满赠套装结束-->
    						            <!-- 买家版运费险 -->
            <div class="hide service-items ml20 mr20">
                <div class="hide service-item" id="vender_freight_insurance_0">
                    <div class="hr"></div>
                    <span class="service-desc">退换无忧</span>
                    <strong class="service-price"></strong>
                </div>
            </div>
			<!-- 循环包装 -->
		<div class="hide service-items ml20 mr20">
            <div class="service-item xhbz hide" id="packagingServices_0">
                <div class="hr"></div>
                <span class="service-desc">循环包装服务费</span>
                <strong class="service-price" id="packagingServicesCharge_0">￥0.00</strong>
            </div>
        </div>
            <!-- 增加商家备注 -->
            <div class="remarks-items ml20 mr20 mt10 hide " vendor="0">
                <div class="remarks-item">
                    <span class="remarks-tit ">留言:</span>
                    <textarea style="height: 22px" maxlength="45" class="remarks-cont " rows="1" placeholder="建议留言前先与商家沟通确认" onfocus="setRemarkWrite(this)" onblur="fitRemark(this)" oninput="setNum(this)" blur=""></textarea>
                    <em class="remarks-limits remarks-limits-new error hide">45</em>
                </div>
            </div>



        </div><!--goods-list 结束-->
        <div class="dis-modes" id="11">
			      <!--购物车单品商品-->
			              <!--一般套装商品-->
			   <!--满返套装商品-->
			 <!--满赠套装商品-->
            <!--以下为京东配送方式-->
			   <!--配送方式-->
			   <!--配送方式-->
			 <!--配送方式-->
			 <!--配送方式-->
			 <!--配送方式-->
			            <!-- 实物商品搭售虚拟商品 -->
									                <div class="mode-item mode-tab">
                    <div class="mode-item-tit">
                        <h4>配送方式</h4>
                        <div class="extral-r"><a id="jd-goods-item" class="cor-goods" href="#none"><i></i>对应商品</a></div>
                    </div>
                    <div class="mode-tab-nav">
                        <ul>
							                                <input type="hidden" id="containFactoryShip" value="0"/>
                      <li class="mode-tab-item jd curr" id="jd_shipment_item" onclick="doSwithTab('pay')" clstag="pageclick|keycount|trade_201602181|11">
									                                        <span id="jdShip-span-tip" class="m-txt">京东快递<i class='qmark-icon qmark-tip' data-tips='由京东公司负责配送，速度很快，还接受上门刷卡付款服务'></i></span><b></b>
									                                </li>
																			    <li class="mode-tab-item hide " id="Honor_shipment_item_0" onclick="doSwithTab('honor',0)" clstag="pageclick|keycount|trade_201602181|11">
    						<span class="m-txt"><i class="jdship-jz-ico"></i>京尊达<i class='qmark-icon qmark-tip' data-tips='由京东专人、专车、专线配送，享受尊贵配送服务'></i></span><b></b>
                        </li>
                            <li class="mode-tab-item hide " id="pick_shipment_item" onclick="doSwithTab('picksite')" clstag="pageclick|keycount|trade_201602181|12">
                                <span class="m-txt">上门自提<i class="qmark-icon qmark-tip" data-tips="自提时付款，支持现金、POS刷卡、支票支付<a href='http://help.jd.com/user/issue/100-181.html' target='_blank' class='ftx-05'>查看自提流程</a>"></i></span><b></b>
                            </li>

                            <li class="mode-tab-item hide  " id="car_shipment_item" onclick="doSwithTab('car')" clstag="pageclick|keycount|trade_201602181|12">
                                <span class="m-txt">快递到车<i class="qmark-icon qmark-tip" data-tips="快递将配送至您账号绑定的蔚来汽车后备箱中"></i></span><b></b>
                            </li>
                        </ul>
                    </div>
					                    <div class="mode-tab-con " id="jd_shipment">
					                    <ul class="mode-list">
						                        <li id="shipment_times" >
																								   <div class="fore1 hide" id="Honor_tip_0"></div>
                            <div class="fore1" id="jd_shipment_calendar_date" data-text="    "><span class="ftx-03">配送时间：</span>&nbsp;&nbsp;<span id='promise311tip'></span>预计&nbsp;12月15日<span class=ftx-04>[周六]</span>&nbsp;09:00-15:00&nbsp;送达</div>
                            <div class="fore2 hide" id="jdshipdate_eidt_id" onclick="doEdit311Time(null,1)" clstag="pageclick|keycount|trade_201602181|14"><a href="#none" class="ftx-05">修改</a></div>
                            <div id="forcedChoice-sales" class="fresh-tip-cont hide">
                                <span class="fl fresh-tip-left"><i></i>京准达</span>
                                <span class="fl fresh-tip-right">限时免费，准时送达</span>
                            </div>
                        </li>
                        <li id="forcedChoice-times" style="display:none">
                            <a href="#none" onclick="doEdit311Time(3,1)" class="fl ftx08 mr15 edit-delivery-time-fresh"><i class="date-icon mr5"></i>选择配送时间</a>
                            <span class="fl fresh-tip-left"><i></i>京准达</span>
                            <span class="fl fresh-tip-right" id="car_tips_on">限时免费，准时送达</span>
                        </li>
                        <li id="car-ship-times" style="display:none">
                            <a href="#none" onclick="doEdit311Time(3,1)" class="fl ftx08 mr15 edit-delivery-time-car"><i class="date-icon mr5"></i>选择配送时间</a>
                            <span class="fl car-tip-left"><i></i>京准达</span>
                            <span class="fl car-tip-right">限时免费，准时送达</span>
                        </li>
                        <li class="delivery-info-li" id="delivery-info-li-zxj">
							                  <span class="delivery-tips fr">
												  <i class="d-ico fl mr5"></i><i class="d-arr"></i>							                      <a id="zxj_show_id" href="#none" class="mr5 hide" onclick="doEdit311Time(3)">京准达</a>
							                      <a id="311_show_id" href="#none" class="mr5 hide" onclick="doEdit311Time(1)">标准达</a>
							                      <a id="411_show_id" href="#none" class="mr5 hide" onclick="doEdit311Time(2)">极速达</a>配送服务全面升级							                  </span>
                        </li>
                        <div class="mode-tab-item-info mt10 hide" id="car_tips">
                            <i class="warn-icon"></i>
                            <span class="mode-tab-item-info-cont">请确保送货时间段内蔚来汽车停驻在收货地址附近</span>
                        </div>
                        <li style="display:none" id="item_installDate">
                            <div class="fore1" id="jd_install_date_div">
                                <span class="mode-label ftx-03">安装时间：</span>
                                <div class="mode-infor">
                                </div>
                            </div>
                            <div class="fore2" onclick="doEditJdInstallDate('0')"><a href="#none" class="ftx-05 edit-install-time">修改</a></div>
                        </li>
						
						<li class="pb10 hide" id="combine_service" style="display:none;">
                                <p class="mb5"><label class="l-for-check"><input id="combine_servicebox" type="checkbox" class="mr5" onclick="selectCombineService(this)">合并送货</label></p>
                                <p class="ftx-03">您购买的商品分属不同仓库，可能会分多次上门配送。选择合并送货后配送员将等待所有商品配齐后一次上门配送。</p>
                        </li>
                        
						<li class="pb10 buyer_insurance hide" id="0" style="display:none;">
                                <p class="mb5" >
									<label class="l-for-check">
										<input id="vender_0" type="checkbox" class="mr5 buyer_freight_insurance" onclick="selectBuyerFreightInsurance(this, 0)" >
										退换无忧
									</label>
									<span class="ftx-01 ml10">¥0.50</span></p>
                                <p class="ftx-03"></p>
								<span class="mode-infor-tips mode-infor-tips-sec" id="mode-infor-tips-secid_0" style="display: none;"></span>
                        </li>
						<li class="pb10 packaging_services hide" id="packaging_services_li" style="display:none;">
                                <p class="mb5" >
									<label class="l-for-check">
										<input id="packaging_services_check" type="checkbox" class="mr5" checked="" onclick="selectPackagingServices(this, 0)">
											循环包装
									</label>
									<span class="ftx-01 ml10"></span>
								</p>
                                <p class="ftx-03" id="packaging_services_copy"></p>
                                <p class="ftx-03 mt5 hide" id="packaging_services_uns">以下商品支持循环包装<a id="xhbz-goods-item" class="ftx-05 cor-goods" href="#none">&nbsp;&nbsp;查看详情</a></p>
								<div class="hide" id="xhbz_unsurpportSku"> 
									<div class="tooltip-goods">
                            			<div class="tooltip-tit">
                            				以下商品支持循环包装
										</div>
                            			<div class="goods-items unsupport">
                            				<div class="goods-item">
                            					<div class="p-img">
                            						<a href="#none"><img src="" alt=""></a>
                            					</div>
                            					<div class="p-name">
                            						<a href="#none"></a>
                            					</div>
                            				</div>
                            			</div>
                            	</div>	
                            </li>
                    </ul>
                    <div class="tips-618 hide tips-618-for-normal" style="z-index:9">
                        <div class="tips-con">
                            <i>&nbsp;</i>
                            <p class="tips-m">
                                双11大促恰逢周末，请确认好收货地址和时间以保证货物及时送达。
                            </p>
                        </div>
                    </div>
                </div>
                    <div class="mode-tab-con hide" id="gsd_shipment">
						<input type="hidden" id="zygsdforcedChoice" value="0"/>
                        <ul class="mode-list">
                            <li id="gsd-old-ships" style="display:none">
                                <div class="fore1" id="gsd_date"><span class="ftx-03"></span></div>
                            </li>
							 <li id="gsd-new-times-wmr" style="display:none">
                                <a href="#none" onclick="doEdit311Time(3,1)" class="fl ftx08 mr15 edit-delivery-time-fresh"><i class="date-icon mr5"></i>选择配送时间</a>
							 </li>
							  <li id="gsd-new-times-ymr" style="display:none">
								<div class="fore1" id="gsd_shipment_calendar_date"><span class="ftx-03">配送时间：</span></div>
								<div class="fore2" id="gsdshipdate_eidt_id" onclick="doEdit311Time(null,2)" clstag="pageclick|keycount|trade_201602181|14"><a href="#none" class="ftx-05">修改</a></div>
							 </li>
                        </ul>
                    </div>
                    <div class="mode-tab-con hide" id="selfpick_shipment">
                        <ul class="mode-list">
                            <li>
                                <div class="fore1" id="selfpick_name"><span class="ftx-03">自提地点：</span></div>
                                <div class="fore2" onclick="doEditPicksite()"><a href="#none" class="ftx-05 picksite-edit">修改</a></div>
                            </li>
                            <li>
                                <div class="fore1" id="selfpick_date"><span class="ftx-03">自提时间：</span></div>
                                <div class="fore2" onclick="doEditPickSiteDate('0')"><a href="#none" class="ftx-05">修改</a></div>
                            </li>
                            
							<li class="pb10 buyer_insurance hide" id="0" style="display:none;">
                                <p class="mb5" >
									<label class="l-for-check">
										<input id="vender_0" type="checkbox" class="mr5 buyer_freight_insurance" onclick="selectBuyerFreightInsurance(this, 0)" >
										退换无忧
									</label>
									<span class="ftx-01 ml10">¥0.50</span></p>
                                <p class="ftx-03"></p>
								<span class="mode-infor-tips mode-infor-tips-sec" id="mode-infor-tips-secid_0" style="display: none;"></span>
                        </li>
							<li class="pb10 packaging_services hide" id="packaging_services_li_ZT" style="display:none;">
                                <p class="mb5" >
									<label class="l-for-check">
										<input id="packaging_services_check_ZT" type="checkbox" class="mr5" checked="" onclick="selectPackagingServices(this, 0)">
											循环包装
									</label>
									<span class="ftx-01 ml10"></span>
								</p>
                                <p class="ftx-03" id="packaging_services_copy_ZT"></p>
                                <p class="ftx-03 mt5 hide" id="packaging_services_uns_ZT">以下商品支持循环包装<a id="xhbz-goods-item-zt" class="ftx-05 cor-goods" href="#none">&nbsp;&nbsp;查看详情</a></p>
								<div class="hide" id="xhbz_unsurpportSku_ZT"> 
									<div class="tooltip-goods">
                            			<div class="tooltip-tit">
                            				以下商品支持循环包装
										</div>
                            			<div class="goods-items unsupport_ZT">
                            				<div class="goods-item">
                            					<div class="p-img">
                            						<a href="#none"><img src="" alt=""></a>
                            					</div>
                            					<div class="p-name">
                            						<a href="#none"></a>
                            					</div>
                            				</div>
                            			</div>
                            	</div>	
                            </li>
                        </ul>
                        <div class="tips-618 hide tips-618-for-selfpick" style="z-index:9">
                            <div class="tips-con">
                                <i>&nbsp;</i>
                                <p class="tips-m">
                                    双11大促恰逢周末，请确认好收货地址和时间以保证货物及时送达。
                                </p>
                            </div>
                        </div>
                    </div>
                    <!--隐藏自提点开始-->
                    <div id="picksite_hidediv"  class="hide">
						<!-- 选择自提点 -->

<div class="form picksite-box">
	<div class="item">
		<span class="label">选择区域：</span>
		<div class="fl">
			<select name="pickRegion" id="pickRegion_select" class="selt pickRegion_select" onchange="doEditPickReigon(this)">
						   <option value="-1">全部区域</option>
						</select>
		</div>
	</div>
	<div class="item">
		<span class="label">选择自提点：</span>
		<div class="fl">
			<div class="pick-sites pick-sites-more"  id="pick-sites">
				<!--循环取出自提点信息开始-->
												<!--循环取出自提点信息结束-->
			</div>
			<div class="pick-more" >
				<span  class="selfpick_more_link open ftx05 hide"  style="cursor:pointer;" onclick="open_MorePicksite(this)">展开更多<b></b></span>
			</div>
		</div>
	</div>
	<div class="item">
		<span class="label">&nbsp;</span>
		<div class="fl">
			<div class="op-btns">
				<a class="btn-9" onclick="doSaveDialogPickSite()">保存自提点</a>
				<a class="btn-9 ml10" href="javascript:jQuery.closeDialog();">取消</a>
			</div> 
			<div class="ftx-03 mt10">温馨提示：</div>
			<div class="ftx-03">1、自提时付款，支持现金、POS刷卡、支票支付 <a class="ftx-05" href="http://help.jd.com/user/issue/100-181.html" target="_blank">查看自提流程</a></div>
            <div class="ftx-03"><span class="ftx-04">2、京东将根据您的收货地址显示其范围内的自提点，请确保您的收货地址正确填写。 </span></div>
		</div>
	</div>
</div>
<script type="text/javascript">
   //选择自提点
   function doSelectPicksite(thisElement){
      if($(thisElement).parent().hasClass("site-item-disabled")){
         //alert("您所选取的自提点不可用");
         return;
      }
      $("#selfpick_siteDiv .site-item").each(function(index,item){
	       if($(this).hasClass("site-item-selected")){
	           $(this).removeClass().addClass("site-item");
	       }
	  });
	  if($(thisElement).parent().hasClass("site-item-selected")==false){
	      $(thisElement).parent().removeClass().addClass("site-item site-item-selected");
	  }
   }
   function doClosePickSite(){
   	   $(".site-item").each(function(index,item){
	       if($(this).hasClass("site-item-selected")){
	           $(this).removeClass().addClass("site-item");
	       }
	  });
	  javascript:jQuery.closeDialog();
   }
</script>                    </div>
                    <!--隐藏自提点结束-->
                    <!--自提点配送时间开始-->
                    <div id="pickSiteShipDate" class="hide">
							<div class="date-box">
		<div class="date-list">
			<ul>
			  			</ul>
		</div>
		<div class="ftx-03 mt10">
			温馨提示：<br>
			1、您选择的时间可能会因库存不足等因素导致订单延迟，请您谅解！<br>
			2、我们会在您选定提货日期的前一天处理您的订单，在此之前您的订单处于暂停状态。
	
		</div>
		<div class="op-btns mt20 ac">
			<a href="#none" onclick="doSavePickShipDate('0')" class="btn-9">保存</a>
			<a href="javascript:jQuery.closeDialog();"  class="btn-9 ml10">取消</a>
		</div>
	</div>

<script type="text/javascript">
        //点击切换自提点配送时间
        function doSwithPickShipDate(venderId,thisElement){
			 $('.li_pick_shipment').removeClass().addClass("li_pick_shipment");
            $(thisElement).removeClass().addClass("li_pick_shipment selected");
        }
        
        //保存自提点配送时间
        function doSavePickShipDate(venderId){
           $("#selfpick_date").html('<span class="ftx-03">配送时间：</span>' + $('.li_pick_shipment.selected').attr("picksite_date") + " " + $('.li_pick_shipment.selected').attr("picksite_weekDay"));
           $("#saveParam_pickDate").val($('.li_pick_shipment.selected').attr("date"));
           $("#beforePickDate").val($('.li_pick_shipment.selected').attr("date"));
		   doSavePayAndShipmentInfo("jd_picksite_time");
           jQuery.closeDialog();
        }
</script>                    </div>
                    <!--自提点配送时间结束-->
                    <!--非大件对应商品清单开始-->
                    <div class="hide" id="jdItem_surpportSku">
						                        <div class="tooltip-goods">
                            <div class="tooltip-tit">
                                以下商品为<strong>非大件商品</strong>
                            </div>
                            <div class="goods-items">
																											                                            <div class="goods-item">
                                                <div class="p-img">
                                                    <a href="#none"><img src="//img14.360buyimg.com/N4/jfs/t28210/176/166163755/271400/2e654ec0/5bea36b6N79ca2695.jpg" alt=""></a>
                                                </div>
                                                <div class="p-name">
                                                    <a href="#none">联想ThinkPad 翼480（0VCD）英特尔8代酷睿14英寸轻薄窄边框笔记本电脑（i5-8250U 8G 128GSSD+500G 2G独显）</a>
                                                </div>
                                            </div>
																											                            </div>
                        </div>
                    </div>
                    <!--非大件对应商品清单结束-->
                </div>
			            <!--以下为京东大家电配送-->
			
            <!--以下为京东第三方配送-->
			            <!--以下为第三方配送-->
            <!--如果是SOP快递或者是京东中小件商品，但是不支持配送，则采用快递运输-->
						
						
				            <!--sop大件入仓配送-->
			
        </div><!--dis-modes 结束-->
        <div class="clr"></div>
        <!--
			<div class="freight-cont">
				   					       <strong class="ftx-01" style="color:#666" freightByVenderId="0"  popJdShipment="false">免运费</strong>
				   			  </div>
	      -->
		            <div class="weight-cont total-freight-weight hide">总重量：<em class="ftx-03 total-freight-weight-val"></em></div>
		    </div><!--shopping-list 结束-->
	<form id="skuAndShipment_submit_form"  method = 'post'  action = '' >
    <input type="hidden" id="saveParam_paymentId" name="saveParam.paymentId" /><!--支付方式id-->
    <input type="hidden" id="saveParam_otype" name="saveParam.onlinePayType" />
    <!-- 京东配送 -->
    <input type="hidden" id="saveParam_jdShipmentType" name="saveParam.jdShipmentType" value="65" /><!--京东配送-->
    <input type="hidden" id="saveParam_jdShipTime" name="saveParam.jdShipTime" value="4"/><!-- 区分工作日，311，411-->
    <input type="hidden" id="saveParam_jdPayWayId" name="saveParam.jdPayWayId" value="0"/><!--货到付款方式-->
    <input type="hidden" id="saveParam_jdCheckType" name="saveParam.jdCheckType" value="2"/><!--如果是支票这个只是写死的[仅支持京东上门自取]-->
    <input type="hidden" id="saveParam_jdBigItemShipTimeOffset" name="saveParam.jdBigItemShipTimeOffset" value="0"/><!--京东大家电配送时间偏移量-->
    <input type="hidden" id="saveParam_jdBigItemInstallTimeOffest" name="saveParam.jdBigItemInstallTimeOffest" value="0"/><!--京东大家电安装时间偏移量-->
    <input type="hidden" id="saveParam_installTimeOffest" name="saveParam.installTimeOffest"/><!--京东自营落地配小件安装时间偏移量-->
    <!--311-->
    <input type="hidden" id="saveParam_promiseType" name="saveParam.promiseType"/><!--1表示311类型，2表示411-->
    <input type="hidden" id="saveParam_promiseDate" name="saveParam.promiseDate"/><!--日历-->
    <input type="hidden" id="saveParam_promiseTimeRange" name="saveParam.promiseTimeRange"/><!--波次-->
    <input type="hidden" id="saveParam_promiseSendPay" name="saveParam.promiseSendPay"/><!--选择的sendpay-->
    <input type="hidden" id="saveParam_batchId" name="saveParam.batchId"/><!--选择的sendpay-->
    <input type="hidden" id="saveParam_promiseMessage" name="saveParam.promiseMessage"/><!--预约配送提示-->
    <!--411-->
    <input type="hidden" id="saveParam_jdBigItemNightShip" name="saveParam.jdBigItemNightShip" value="false"/><!--大家电是否支持晚间配送-->
    <!--京东第三方配送-->
    <input type="hidden" id="saveParam_otherShipmentType" name="saveParam.otherShipmentType" value=""/><!--京东第三方配送-->
    <input type="hidden" id="saveParam_otherShipTime" name="saveParam.otherShipTime" value=""/><!--区分工作日，311，411-->
    <input type="hidden" id="saveParam_otherBigItemShipOffset" name="saveParam.otherBigItemShipOffset" value=""/><!--京东大家电安装时间偏移量-->
    <input type="hidden" id="saveParam_otherBigItemInstallTimeOffset" name="saveParam.otherBigItemInstallTimeOffset" value=""/><!--京东大家电配送时间偏移量-->
    <!--sop京东和第三方配送-->
    <input type="hidden" id="saveParam_sopShipment" name="saveParam.sopShipment" value=""/><!--sop三方配送-->
    <input type="hidden" id="saveParam_sopOtherShipmentType" name="saveParam.sopOtherShipmentType" value=""/><!--sop第三方配送-->
    <!-- 自提方式 -->
    <input type="hidden" id="saveParam_pickShipmentType" name="saveParam.pickShipmentType" value=""/>
    <!--自提方式-->
    <input type="hidden" id="saveParam_pickSiteId"  name="saveParam.pickSiteId" value="0"/><!--自提点-->
    <input type="hidden" id="saveParam_pickDate" name="saveParam.pickDate" value=""/><!--自提时间-->
    <input type="hidden" id="saveParam_pickSiteNum" name="saveParam.pickSiteNum" value="5" /><!--默认5个-->
    <input type="hidden" id="saveParam_pickRegionId" name="saveParam.pickRegionId"  /><!--搜索区域-->

    <input type="hidden" id="saveParam_jdBigItemPromiseType"  name="saveParam.jdBigItemPromiseType"/>
    <input type="hidden" id="saveParam_jdBigItemPromiseDate" name="saveParam.jdBigItemPromiseDate" />
    <input type="hidden" id="saveParam_jdBigItemPromiseTimeRange" name="saveParam.jdBigItemPromiseTimeRange"  />
    <input type="hidden" id="saveParam_jdBigItemPromiseSendPay" name="saveParam.jdBigItemPromiseSendPay"  />
    <input type="hidden" id="saveParam_jdBigItemBatchId" name="saveParam.jdBigItemBatchId"  />

    <input type="hidden" id="saveParam_otherBigItemPromiseType"  name="saveParam.otherBigItemPromiseType"/>
    <input type="hidden" id="saveParam_otherBigItemPromiseDate" name="saveParam.otherBigItemPromiseDate" />
    <input type="hidden" id="saveParam_otherBigItemPromiseTimeRange" name="saveParam.otherBigItemPromiseTimeRange"  />
    <input type="hidden" id="saveParam_otherBigItemPromiseSendPay" name="saveParam.otherBigItemPromiseSendPay"  />
    <input type="hidden" id="saveParam_otherBigItemBatchId" name="saveParam.otherBigItemBatchId"  /><!--搜索区域-->

    <input type="hidden" id="zxj_promiseTagType" name="saveParam.promiseTagType" /><!--中小件京准达时效类型 -->
    <input type="hidden" id="tdc_cutOrder" name="saveParam.cutOrder" /><!--TDC京准达波次 -->


    <!-- 大件仓极速达商品  -->
    <input type="hidden" id="djd_speedHour" name="saveParam.speedHour" />
    <input type="hidden" id="djd_sendPay" name="saveParam.sendPay" />
    <input type="hidden" id="djd_codDate" name="saveParam.codDate" />
    <input type="hidden" id="djd_speedMark" name="saveParam.speedMark" />

    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_venderId" name="saveParam.venderId" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_storeId" name="saveParam.storeId" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_warehouseId" name="saveParam.warehouseId" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_name" name="saveParam.name" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_businessHours" name="saveParam.businessHours" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_longitude" name="saveParam.longitude" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_latitude" name="saveParam.latitude" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_storeMark" name="saveParam.storeMark" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_stockStatus" name="saveParam.stockStatus" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_distance" name="saveParam.distance" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_storeAddress" name="saveParam.storeAddress" />
    <input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_recentlyMark" name="saveParam.recentlyMark" />
	
	<input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_venderStoreStockTab" name="saveParam.venderStoreStockTab" />
	<input type="hidden" id="saveParam_venderSelfDeliveryStoreVO_vendSource" name="saveParam.vendSource" />
    <input type="hidden" id="saveParam_sopShipmentType" name="saveParam.sopShipmentType" />
    <input type="hidden" id="saveParam_gsdShipmentType" name="saveParam.gsdShipmentType" />
    <input type="hidden" id="saveParam_carDeliver" name="saveParam.carDeliver" />
	   <input type="hidden" id="saveParam_honorVenderId" name="saveParam.honorVenderId" />
	   <input type="hidden" id="honorVenderId" name='saveParam.honorVenderIdBack' />
	   <input type="hidden" id="saveParam_honorVenderIds" name='saveParam.honorVenderIds' />
	   <input type="hidden" id="saveParam_honorVenderIdStatus" name='saveParam.honorVenderIdStatus' />
	   
	   <input type="hidden" id="consolidator_id" name="saveParam.consolidator.id">
	   <input type="hidden" id="consolidator_name" name="saveParam.consolidator.name">
	   <input type="hidden" id="consolidator_selected" name="saveParam.consolidator.selected">
	   <input type="hidden" id="consolidator_logo" name="saveParam.consolidator.logo">
	   <input type="hidden" id="consolidator_proviceId" name="saveParam.consolidator.proviceId">
	   <input type="hidden" id="consolidator_cityId" name="saveParam.consolidator.cityId">
	   <input type="hidden" id="consolidator_countyId" name="saveParam.consolidator.countyId">
	   <input type="hidden" id="consolidator_townId" name="saveParam.consolidator.townId">
	   <input type="hidden" id="consolidator_detailAddr" name="saveParam.consolidator.detailAddr">
	   <input type="hidden" id="consolidator_chargeStandard" name="saveParam.consolidator.chargeStandard">
	   <input type="hidden" id="consolidator_pcLogoUrl" name="saveParam.consolidator.pcLogoUrl">
	   <input type="hidden" id="consolidator_appLogoUrl" name="saveParam.consolidator.appLogoUrl">
	   <input type="hidden" id="saveParam_packagingServices" name='saveParam.packagingServices' />
	   <input type="hidden" id="saveParam_combineServices" name='saveParam.combine'/>
	   <input type="hidden" id="saveParam_immediateDelivery" name='saveParam.immediateDelivery' />
</form>
<input type="hidden" id="mainSkuIdAndNums" value="6072622_1,"/><!--icon隐藏域,用于更新库存-->
<input type="hidden" id="calendar_hdata" value=""/><!--icon隐藏域，用户存日历控件时间段-->
<input type="hidden" id="calendar_ddata" value=""/><!--icon隐藏域，用户存日历控件日期-->
<input type="hidden" id="calendar_x" value=""/><!--icon隐藏域，存日历控件X坐标-->
<input type="hidden" id="calendar_y" value=""/><!--icon隐藏域，用日历控件Y坐标-->
<input type="hidden" id="calendar_big_hdata" value=""/><!--icon隐藏域，用户存日历控件时间段-->
<input type="hidden" id="calendar_big_ddata" value=""/><!--icon隐藏域，用户存日历控件日期-->
<input type="hidden" id="calendar_big_bzd_hdata" value=""/><!--icon隐藏域，用户存日历控件时间段-->
<input type="hidden" id="calendar_big_bzd_ddata" value=""/><!--icon隐藏域，用户存日历控件日期-->
<input type="hidden" id="calendar_big_x" value=""/><!--icon隐藏域，存日历控件X坐标-->
<input type="hidden" id="calendar_big_y" value=""/><!--icon隐藏域，用日历控件Y坐标-->
<input type="hidden" id="calendar_big_bzd_x" value=""/><!--icon隐藏域，存日历控件X坐标-->
<input type="hidden" id="calendar_big_bzd_y" value=""/><!--icon隐藏域，用日历控件Y坐标-->
<input type="hidden" id="last_sel_promiseDate" value=""/><!--icon隐藏域，记录上次选中的日期-->
<input type="hidden" id="last_sel_promiseTimeRange" value=""/><!--icon隐藏域，记录上次选中的时间段-->
<input type="hidden" id="last_sel_promiseSendPay" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="last_sel_batchId" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="big_last_sel_promiseDate" value=""/><!--icon隐藏域，记录上次选中的日期-->
<input type="hidden" id="big_last_sel_promiseTimeRange" value=""/><!--icon隐藏域，记录上次选中的时间段-->
<input type="hidden" id="big_last_sel_promiseSendPay" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="big_last_sel_batchId" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="big_last_sel_offset" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="big_bzdrl_last_sel_promiseDate" value=""/><!--icon隐藏域，记录上次选中的日期-->
<input type="hidden" id="big_bzdrl_last_sel_promiseTimeRange" value=""/><!--icon隐藏域，记录上次选中的时间段-->
<input type="hidden" id="big_bzdrl_last_sel_promiseSendPay" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="big_bzdrl_last_sel_offset" value=""/>
<input type="hidden" id="big_bzdrl_last_sel_batchId" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="big_bzd_last_sel_promiseDate" value=""/><!--icon隐藏域，记录上次选中的日期-->
<input type="hidden" id="big_bzd_last_sel_promiseTimeRange" value=""/><!--icon隐藏域，记录上次选中的时间段-->
<input type="hidden" id="big_bzd_last_sel_promiseSendPay" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="big_bzd_last_sel_batchId" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="bigshipment_bzd_type" value="0"/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="shipment411_sendpay" value=""/><!--411sendpay-->
<input type="hidden" id="shipment_support_type" value=""/><!--icon隐藏域，当前311和411支持的类型，0表示311,411都不支持,1表示只支持311,2表示只支持411,3表示311,411都支持-->
<input type="hidden" id="shipment_select_support" value="0"/><!--icon隐藏域，当前311和411选中的是哪一个，1表示选中311,2表示选中411,3表示京准达-->
<input type="hidden" id="bigshipment_bzd_support" value="0"/><!--icon隐藏域，当前京准达和标准达支持的类型，标准达 0表示不支持,1表示支持-->
<input type="hidden" id="bigshipment_bzd_shipAndInstall" value="0"/><!--icon隐藏域，大家电标准达是否支持送装一体，1：支持  0不支持不处理,-1不支持-->
<input type="hidden" id="bigshipment_jzd_support" value="0"/><!--icon隐藏域，当前京准达和标准达支持的类型，京准达 0表示不支持,1表示支持-->
<input type="hidden" id="bigshipment_jsd_support" value="0"/><!--icon隐藏域，当前极速达支持的类型，极速达 0表示不支持,1表示支持-->
<input type="hidden" id="bigshipment_select_support" value="1"/><!--icon隐藏域，当前京准达和标准达选中的是哪一个，1表示选中京准达,2表示选中标准达,3标示极速达-->
<input type="hidden" id="shipment_cur411_support" value=""/><!--icon隐藏域，当前411是否还支持配送，1支持，2不支持-->
<input type="hidden" id="shipment411_msg" value=""/><!--icon隐藏域，411提示信息-->
<input type="hidden" id="pick_sel_regionid" value=""/><!--icon隐藏域，临时存放选中的自提点区域ID-->
<input type="hidden" id="temp_pick_sel_regionid" value=""/><!--icon隐藏域，临时存放选中的自提点区域ID-->
<input type="hidden" id="pick_sel_id" value=""/><!--icon隐藏域，临时存放选中的自提点ID-->
<input type="hidden" id="is_invoke_pickdate" value="0"/><!--自提时间隐藏域，是否要刷新自提点时间-->
<input type="hidden" id="is_refresh_installdate" value=""/><!--icon隐藏域，是否要刷新商品安装时间-->
<input type="hidden" id="bigItemCodDates" value=""/><!--icon隐藏域，是否要刷新商品安装时间-->

<input type="hidden" id="popVenderIdStr" value="0"/><!--icon隐藏域，所有店铺ID串-->
<input type="hidden" id="locShopIdStr"  value=""/><!--icon隐藏域，所有loc门店ID串 -->

<input type="hidden" id="calendar_hdata_zxj_jzd" value=""/><!--icon隐藏域，用户存日历控件时间段-->
<input type="hidden" id="calendar_ddata_zxj_jzd" value=""/><!--icon隐藏域，用户存日历控件日期-->
<input type="hidden" id="calendar_x_zxj_jzd" value=""/><!--icon隐藏域，存日历控件X坐标-->
<input type="hidden" id="calendar_y_zxj_jzd" value=""/><!--icon隐藏域，用日历控件Y坐标-->
<input type="hidden" id="last_sel_promiseDate_zxj_jzd" value=""/><!--icon隐藏域，记录上次选中的日期-->
<input type="hidden" id="last_sel_promiseTimeRange_zxj_jzd" value=""/><!--icon隐藏域，记录上次选中的时间段-->
<input type="hidden" id="last_sel_promiseSendPay_zxj_jzd" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="last_sel_batchId_zxj_jzd" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="promiseSopViewList" /><!--sop日历弹窗隐藏域-->
<input type="hidden" id="jzdAmount_hidden" value=""/><!--京准达运费收费标准-->
<input type="hidden" id="jsdAmount_hidden" value=""/><!--极速达运费收费标准-->
<input type="hidden" id="djzdAmount_hidden" value=""/><!--大家电京准达运费收费标准-->
<input type="hidden" id="bigItemJzdInstallTimeOffest" value=""/><!--大家电京准达安装偏移量-->
<!--<input type="hidden" id="bigItemJsdInstallTimeOffest" value=""/>--><!--大家电极速达安装偏移量-->
<input type="hidden" id="bigItemInstallTimeOffest" value=""/><!--大家电标准达安装偏移量-->
<input type="hidden" id="forcedChoice" autocomplete="off" value=""/><!--生鲜是否显示默认时效-->

<input type="hidden" id="hid_calendar_tag" value=''/><!--存取京准达多波次时效tag-->

<input type="hidden" id="calendar_hdata_car_jzd" value=""/><!--icon隐藏域，用户存日历控件时间段-->
<input type="hidden" id="calendar_ddata_car_jzd" value=""/><!--icon隐藏域，用户存日历控件时间段-->

<input type="hidden" id="calendar_x_car_jzd" value=""/><!--icon隐藏域，存日历控件X坐标-->
<input type="hidden" id="calendar_y_car_jzd" value=""/><!--icon隐藏域，用日历控件Y坐标-->
<input type="hidden" id="packageChargehide" value=""/>

<input type="hidden" id="gsd_calendar_hdata_zxj_jzd" value=""/><!--icon隐藏域，用户存日历控件时间段-->
<input type="hidden" id="gsd_calendar_ddata_zxj_jzd" value=""/><!--icon隐藏域，用户存日历控件日期-->
<input type="hidden" id="gsd_calendar_x_zxj_jzd" value=""/><!--icon隐藏域，存日历控件X坐标-->
<input type="hidden" id="gsd_calendar_y_zxj_jzd" value=""/><!--icon隐藏域，用日历控件Y坐标-->
<input type="hidden" id="gsd_last_sel_promiseDate_zxj_jzd" value=""/><!--icon隐藏域，记录上次选中的日期-->
<input type="hidden" id="gsd_last_sel_promiseTimeRange_zxj_jzd" value=""/><!--icon隐藏域，记录上次选中的时间段-->
<input type="hidden" id="gsd_last_sel_promiseSendPay_zxj_jzd" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="gsd_last_sel_batchId_zxj_jzd" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="gsd_immediately_x" value=""/><!--icon隐藏域，记录上次选中的时间段-->
<input type="hidden" id="gsd_immediately_y" value=""/><!--icon隐藏域，记录上次选中的sendpay-->
<input type="hidden" id="gsd_immediately" value=""/><!--icon隐藏域，记录上次选中的sendpay-->

<!--隐藏的自营落地配小件安装日历开始-->
<script id="installEdit" type="text/temp">

</script>
<!--隐藏的自营落地配小件安装日历结束-->
<!--隐藏的sop配送日历开始-->
<script id="sop_shipment_hidediv" type="text/temp">
		  <div class="date-thickbox" >
				<div class="tab-nav">
					<ul>
						<li class="tab-nav-item tab-item-selected" id="sopbzd">标准达 <b> </b> </li>
						<li class="tab-nav-item tab-item-selected" id="sopjsd">京瞬达 <b> </b> </li>
					</ul>
				</div>
				<div class="tab-con" id="tab_sop_div">
					<div class="date-delivery" id="date-delivery-sop"></div>
					<div class="ftx-03 mt20">
						温馨提示：我们会努力按照您指定的时间配送，但因天气、交通等各类因素影响，您的订单有可能会有延误现象！
					</div>
					<div class="op-btns mt10 ac"> <a id="timeSaveSop" clstag="pageclick|keycount|trade_201602181|52" href="javascript:void(0);"  class="btn-1">确定 </a> <a href="javascript:jQuery.closeDialog();"  class="btn-9 ml10"> 取消 </a> </div>
				</div>
		</div>
	</script>
<!--隐藏的sop配送日历结束-->
<!--隐藏的311配送日历开始-->
<script id="shipment_hidediv" type="text/temp">
		  <div class="date-thickbox" >
				<div class="tab-nav">
					<ul>
						<li class="tab-nav-item" id="li_zxj_id" onclick="doSwith311Tab('zxj')"><span id="jzdAmount"></span> <b> </b> </li>
						<li class="tab-nav-item" id="li_311_id" onclick="doSwith311Tab('311')">标准达 <b> </b> </li>
						<li class="tab-nav-item" id="li_411_id" onclick="doSwith311Tab('411')"><span id="jsdAmount"></span><b> </b> </li>
					</ul>
				</div>
				<div class="tab-con" id="tab_zxj_div">
				     <div id="jzd_calendar_tag">
                     </div>
					<div class="date-delivery date-delivery-freight" id="date-delivery0"></div>
					<div class="ftx-03 mt20">
						温馨提示：我们会努力按照您指定的时间配送，但因天气、交通等各类因素影响，您的订单有可能会有延误现象！
					</div>
		           	 <div class="tips-618 mt20 hide tips-618-for-calendar">
		              <div class="tips-con">
		                <p class="tips-m">双11大促恰逢周末，请确认好收货地址和时间以保证货物及时送达。</p>
		          	  </div>
		         	 </div>
					<div class="op-btns mt10 ac"> <a id="timeSaveZxj" clstag="pageclick|keycount|trade_201602181|52" href="javascript:void(0);"  class="btn-1">确定 </a> <a href="javascript:jQuery.closeDialog();"  class="btn-9 ml10"> 取消 </a> </div>
				</div>
				<div class="tab-con hide" id="tab_311_div">
					<div class="date-delivery date-delivery-new" id="date-delivery1"></div>
					<div class="ftx-03 mt20">
						温馨提示：我们会努力按照您指定的时间配送，但因天气、交通等各类因素影响，您的订单有可能会有延误现象！
					</div>
		           	 <div class="tips-618 mt20 hide tips-618-for-calendar">
		              <div class="tips-con">
		                <p class="tips-m">双11大促恰逢周末，请确认好收货地址和时间以保证货物及时送达。</p>
		          	  </div>
		         	 </div>
					<div class="op-btns mt10 ac"> <a id="timeSave311" clstag="pageclick|keycount|trade_201602181|51" href="javascript:void(0);"  class="btn-1"> 确定 </a> <a href="javascript:jQuery.closeDialog();"  class="btn-9 ml10"> 取消 </a> </div>
				</div>
				<div class="tab-con hide" id="tab_411_div">
					<div id="411_content_div"> 下单后或支付成功后2小时送达</div>
					<div class="ftx-03 mt20" id="message_show_411">
						温馨提示：我们会努力按照您指定的时间配送，但因天气、交通等各类因素影响，您的订单有可能会有延误现象！
					</div>
					<div class="op-btns mt10 ac"> <a id="timeSave411" clstag="pageclick|keycount|trade_201602181|53" class="btn-1"> 确定 </a> <a href="javascript:jQuery.closeDialog();" class="btn-9 ml10"> 取消 </a> </div>
				</div>
		</div>
	</script>
<!--隐藏的311配送日历结束-->
<!--隐藏的大家电配送日历开始-->
<script id="bigShipment_hidediv" type="text/temp">
		  <div class="date-thickbox">
				<div class="tab-nav">
					<ul>
						<li class="tab-nav-item tab-item-selected" id="li_djd_id" onclick="doSwithBigTab('djd')"><span id="djzdAmount"></span> <b> </b> </li>
						<li class="tab-nav-item" id="li_bzd_id" onclick="doSwithBigTab('bzd')">标准达 <b> </b> </li>
						<li class="tab-nav-item" id="li_jsd_id" onclick="doSwithBigTab('jsd')">极速达 <b> </b> </li>
					</ul>
				</div>
				<div class="tab-con" id="tab_djd_div">
					<div class="date-delivery date-delivery-freight" id="big-date-delivery0"></div>
					<div class="ftx-03 mt20">
					<i class="date-delivery-icon"></i>
						温馨提示：我们会努力按照您指定的时间配送，但因天气、交通等各类因素影响，您的订单有可能会有延误现象！
					</div>
                    <div class="tips-618 mt20 hide tips-618-for-calendar">
                        <div class="tips-con">
                            <p class="tips-m">双11大促恰逢周末，请确认好收货地址和时间以保证货物及时送达。</p>
                        </div>
                    </div>
					<div class="op-btns mt10 ac"> <a id="timeSaveDjdJzd" clstag="pageclick|keycount|trade_201602181|55" href="javascript:void(0);"  class="btn-1"> 确定  </a> <a href="javascript:jQuery.closeDialog();"  class="btn-9 ml10"> 取消 </a> </div>
		         </div>
				 <div class="tab-con hide" id="tab_bzd_div">
					<div class="date-delivery date-delivery-new" id="big-date-delivery1"></div>
					<div class="ftx-03 mt20">
					<i class="date-delivery-icon"></i>
						温馨提示：我们会努力按照您指定的时间配送，但因天气、交通等各类因素影响，您的订单有可能会有延误现象！
					</div>
                     <div class="tips-618 mt20 hide tips-618-for-calendar">
                         <div class="tips-con">
                             <p class="tips-m">双11大促恰逢周末，请确认好收货地址和时间以保证货物及时送达。</p>
                         </div>
                     </div>
					<div class="op-btns mt10 ac"> <a id="timeSaveBzd" clstag="pageclick|keycount|trade_201602181|54" href="javascript:void(0);"  class="btn-1"> 确定  </a> <a href="javascript:jQuery.closeDialog();"  class="btn-9 ml10"> 取消 </a> </div>
				 </div>

				 <div class="tab-con hide" id="tab_jsd_div">
					<div id="tab_jsd_msg"> 下单后或支付成功后2小时送达</div>
					<div class="ftx-03 mt20" id="message_show_djd_jsd">
						温馨提示：我们会努力按照您指定的时间配送，但因天气、交通等各类因素影响，您的订单有可能会有延误现象！
					</div>
					<div class="op-btns mt10 ac"> <a id="timeSaveDjdJsd" clstag="pageclick|keycount|trade_201602181|56" class="btn-1"> 确定 </a> <a href="javascript:jQuery.closeDialog();" class="btn-9 ml10"> 取消 </a> </div>
				</div>
	</script>
<!--隐藏的大家电配送日历结束-->
<!--隐藏的sop大件配送日历开始-->
<script id="sop_bigShipment_hidediv" type="text/temp">
		  <div class="date-thickbox">
				<div class="tab-nav">
					<ul>
						<li class="tab-nav-item tab-item-selected">标准达 <b> </b> </li>
					</ul>
				</div>
				 <div class="tab-con" id="tab_sop_bzd_div">
					<div class="date-delivery date-delivery-new" id="sop-big-date-delivery"></div>
					<div class="ftx-03 mt20">
					<i class="date-delivery-icon"></i>
						温馨提示：我们会努力按照您指定的时间配送，但因天气、交通等各类因素影响，您的订单有可能会有延误现象！
					</div>
                     <div class="tips-618 mt20 hide tips-618-for-calendar">
                         <div class="tips-con">
                             <p class="tips-m">双11大促恰逢周末，请确认好收货地址和时间以保证货物及时送达。</p>
                         </div>
                     </div>
					<div class="op-btns mt10 ac"> <a id="timeSaveSopBzd" clstag="pageclick|keycount|trade_201602181|54" href="javascript:void(0);"  class="btn-1"> 确定  </a> <a href="javascript:jQuery.closeDialog();"  class="btn-9 ml10"> 取消 </a> </div>
				 </div>
		  </div>
	</script>
<!--隐藏的sop大件配送日历结束-->
<script id="nostock-box01" type="text/temp">
    <div class="limited-thickbox">
    	<div class="tip-box icon-box">
    		<span class="warn-icon m-icon"></span>
    		<div class="item-fore">
    			<h3>下手慢了~部分商品被抢空，继续结算其它商品？</h3>
    		</div>
    	</div>
    	<div class="goods-items" id="out-skus">
    	</div>
    	<div class="op-btns ac">
    			<a href="javascript:continueBuy()" class="btn-1" clstag="trade|keycount|sop|bfwhjxjs">继续</a>
    			<a href="javascript:goCart()" class="btn-9 ml10" clstag="trade|keycount|sop|bfwhfhgwc">返回购物车</a>
    	</div>
    </div>
    </script>
<br><br>
<div id="trade-nostock-recommendation-render" style="display:none"></div>
<script id="nostock-box02" type="text/temp">
    <div class="limited-thickbox">
    	<div class="tip-box icon-box">
    		<span class="warn-icon m-icon"></span>
    		<div class="item-fore">
    			<h3>下手慢了~全部商品被抢空了
					<span class="extra">
                        <a href="javascript:goCart()" class="btn-9 ml10" clstag="trade|keycount|sop|qbwhfhgwc">返回购物车</a>
                    </span>
				</h3>
    		</div>
    	</div>
    	<div class="p-lists">
    		<div class="mt">
    			看看其他的...
    		</div>
    		<div class="mc" id="trade-nostock-recommendation">
    		</div>
    	</div>
    </div>
    </script>
<!--隐藏的无货代下单div-->
<script id="nostock-box03" type="text/temp">
    <div class="nostock-thickbox">
    	<div class="tip-box icon-box-new">
			<span class="warn-icon m-icon"></span>
			<div class="item-fore">
				<h3>下手慢了，部分商品被抢空，是否继续购买？</h3>
				<span>商品可能不满足某些优惠条件</span>
			</div>
		</div>
    	<div class="goods-items" id="out-skus">
    	</div>
    <div class="subs-info" id="detailAddr" style="display:none">
		<span class="sub-tit">到货代下单信息：</span>
		<br>
		<span class="fl">下一个月到货自动为您下单</span>
		<em class="fl ml10 mr10">|</em>
		<span class="fl">在线支付</span>
		<em class="fl ml10 mr10">|</em>
		<span class="fl ml5 mr5" id="name"></span>
		<span class="fl ml5 mr5" id="addrTel"></span>
		<span class="fl addr ml5" id="addrInfo"></span>
		<br>
		<span>可以去<em class="ml5 mr5">我的京东-京东代下单</em><a href="//skunotify.jd.com/storeOrderSubMvc/queryStoreSub.action" target="_blank" class="ftx-05">查看详情</a></span>
	</div>
	<div class="op-btns ar">
		<a href="javascript:continueBuy()" class="btn-1">确定</a>
		<a href="javascript:goCart()" class="btn-9 ml10">取消</a>
	</div>
    </div>
</script>
<!--无货代下单失败提示div-->
<script id="nostock-failed" type="text/temp">
		<div class="nostock-tipsbox" >
			<div class="tip-box icon-box-new">
				<span class="error-icon m-icon"></span>
				<div class="item-fore">
					<h3>提交失败</h3>
					<span>可能是由于网络问题，导致提交失败，尝试返回填写</span>
				</div>
			</div>
			<div class="op-btns ac mt20 ml30">
				<a href="javascript:goCart()" class="btn-1">返回</a>
				<a href="#nogo" id="nostock-failedClose" class="btn-9 ml10">关闭</a>
			</div>
		</div>
</script>
<!--无货代下单成功提示div-->
<script id="nostock-success" type="text/temp">
<div class="nostock-tipsbox">
	<div class="tip-box tip-box-succ icon-box-new">
		<span class="succ-icon m-icon"></span>
		<div class="item-fore">
			<h3>订阅消息成功！</h3>
		</div>
	</div>
	<div class="op-btns ac mt20 ml80">
		<a href='javascript:goCart()' class="btn-1">返回购物车</a>
		<a href='//skunotify.jd.com/storeOrderSubMvc/queryStoreSub.action' target='_blank' class="btn-9 ml10">查看代下单详情</a>
	</div>
</div>
</script>
<script>
    /**
     * 退换无忧浮层
     */
    $(".J-mode-infor-tips").hover(
            function() {
                $(this).find(".mode-infor-tips").show();
            },
            function() {
                $(this).find(".mode-infor-tips").hide();
            }
    );
</script>
        <div class="clr"></div>
  </div>
  <!--shopping-lists 结束-->  
</div>	
                </div>
            </div>
            <!--添加商品清单结束-->
            <!--添加备注信息-->
            <div class="order-remarks hide" id="orderRemarkItem">
            </div>
            <!--  /widget/invoice-step/invoice-step.tpl -->
                            <div class="hr"></div>
                <!-- 发票信息 -->
                <div class="step-tit" id="invoice-step">
    <h3>发票信息</h3>
	<div class="tips-new-white">
		<b></b><span><i></i>开企业抬头发票须填写纳税人识别号，以免影响报销</span>
    </div>    	</div>
<div class="step-content">
    <div id="part-inv" class="invoice-cont">
    	                	<span class="mr10"> 电子普通发票 <i class='invoice-tips-icon' data-tips='电子普通发票与纸质发票具有同等法律效力，可支持报销入账、商品售后凭证。'></i> &nbsp; </span>
        	<span class="mr10"> 个人&nbsp; </span>
        	<span class="mr10"> 商品明细&nbsp; </span>
			 &nbsp;
							                             <a href="#none" id="invoiceEdit" class="ftx-05 invoice-edit" onclick="edit_Invoice()" clstag="pageclick|keycount|trade_201602181|16">修改</a>
                        		    </div>
</div>
                <div class="clr"></div>
                <!--/ /widget/invoice-step/invoice-step.tpl -->
                <div class="hr"></div>
                <!--  /widget/order-coupon/order-coupon.tpl -->
                                      <div class="step-tit step-toggle-off" id="virtualdiv" onclick="vertualHidOrShow()" clstag="pageclick|keycount|xunizichan__2016031015|1" >
    <h3>使用优惠/礼品卡/抵用</h3>
    <i></i>
  </div>
    <div class="step-cont order-virtual" style="display: none;">
        <div class="order-virtual-tabs">
            <ul>
                            <li class="ui-switchable-item" id="couponitem" onclick="query_coupons_vertual()" clstag="pageclick|keycount|xunizichan__2016031015|2"><span>优惠券</span>
                <i style="display: none"></i>
              </li>
                                                        <li class="ui-switchable-item" id="jdbeanitem"  onclick="showOrHideJdBean()" clstag="pageclick|keycount|xunizichan__2016031015|4"><span>京豆</span><i style="display: none"></i></li>
                                              <li class="ui-switchable-item" id="giftitem" data-gift-type="3" clstag="pageclick|keycount|xunizichan__2016031015|3"><span>礼品卡</span><i style="display: none"></i></li>
                                          <li class="ui-switchable-item" id="consignmentitem" data-gift-type="5" clstag="pageclick|keycount|xunizichan__2016031015|3"><span>领货码</span><i style="display: none"></i></li>
                                          <li class="ui-switchable-item hide" id="balanceitem" clstag="pageclick|keycount|xunizichan__2016031015|5"><span>余额</span><i style="display: none"></i></li>
              
            </ul>
        </div>
        <div class="ui-switchable-panel-main" id>
            <div class="ftx01 virtual-warning ml20 hide" id="safeBalancePart">
              <span>
                为保障您的账户资金安全，请先
                <a target="_blank" href="http://safe.jd.com/user/paymentpassword/safetyCenter.action" class="ftx-05">
                  [开启支付密码]
                </a>
              </span>
            </div>
            <div class="hr hide"></div>
            <!-- coupon  -->
                         <div class="coupon-main ui-switchable-panel">
              <div class="coupon-optimal ml20" id="bestCouponDiv">
                  <label clstag="pageclick|keycount|xunizichan__2016031015|13">
                    <input id="bestCouponCheck" type="checkbox" onclick="getBastCouponList(this)" />
                    <span id="bestCoupon">
                      优惠组合推荐
                    </span>
                  </label>
              </div>
              <div class="hr" id="couponsplit"></div>
              <div class="coupon-cont">
                  <div class="coupon-tab ml20">
                    <ul>
                      <li class="coupon-tab-item curr" id="skucoupontit" clstag="pageclick|keycount|xunizichan__2016031015|6">商品优惠券</li>
                      <li class="coupon-tab-item" id="freightcoupontit" clstag="pageclick|keycount|xunizichan__2016031015|7">运费券</li>
                      <li class="coupon-tab-item" id="changecoupontit" clstag="pageclick|keycount|xunizichan__2016031015|8">优惠码兑换</li>
                    </ul>
                  </div>
                  <div class="coupon-tab-panel-main ml20" id="coupons">
                  </div>
              </div>
            </div>
                        <!-- red packet -->
                                    <!-- jdbean-->
            <div class="jdbean-main ui-switchable-panel">
                <div class="beans-2015 ml20" id="jdBeans-new">
                </div>
                 </div>
                         <!-- giftcard -->
                              <div class="giftcard-main ui-switchable-panel">
                     <div class="giftcard-cont"  id="gift_card">
                         <div class="giftcard-tab ml20" >
                             <ul>
                                 <li class="giftcard-tab-item "
                                     clstag="pageclick|keycount|xunizichan__2016031015|9">可用
                                 </li>
                                 <li class="giftcard-tab-item "
                                     clstag="pageclick|keycount|xunizichan__2016031015|9">不可用
                                 </li>
                                 <li class="giftcard-tab-item"
                                     clstag="pageclick|keycount|xunizichan__2016031015|10">添加礼品卡
                                 </li>
                             </ul>
                         </div>
                         <div class="giftcard-tab-panel-main ml20">
                             <div class="giftcard-tab-panel">
                                 <div class="giftcard-scrollbar-origin">
                                     <div class="ui-scrollbar-main-gift">
                                         <div class="giftcard-scroll">
                                             <div class="giftcard-enable">
                                             </div>
                                         </div>
                                         <p class="ac mt10 mb10 ftx08 fts14" style="display: none;">
                                             <span class="loading"><b></b>加载中...</span>
                                         </p>
                                         <p class="ac mt5 mb10 ftx08 fts14" style="display: none;">
                                             没有更多了~
                                         </p>
                                     </div>
                                     <div class="warn-tips" style="display: none;">
                                         <i></i>
                                         <span>已超出单笔订单E卡使用张数上限</span>
                                     </div>
                                 </div>
                             </div>
                         </div>
                         <div class="giftcard-tab-panel-main ml20">
                             <div class="giftcard-tab-panel">
                                 <div class="giftcard-scrollbar-origin">
                                     <div class="ui-scrollbar-main-gift">
                                         <div class="giftcard-scroll">
                                             <div class="giftcard-disable">
                                             </div>
                                         </div>
                                         <p class="ac mt10 mb10 ftx08 fts14" style="display: none;">
                                             <span class="loading"><b></b>加载中...</span>
                                         </p>
                                         <p class="ac mt5 mb10 ftx08 fts14" style="display: none;">
                                             没有更多了~
                                         </p>
                                     </div>
                                 </div>
                             </div>
                         </div>
                         <div class="giftcard-tab-panel ui-switchable-panel-selected hide">
                             <div class="giftcard-add">
                             </div>
                         </div>
                         <div class="ftx01 safeLpkPart" style="display:none;" id="safeLpkPart">为保障您的账户资金安全，张京东E卡/图书卡/京东卡暂不可用，请先
                             <a target="_blank" href="http://safe.jd.com/user/paymentpassword/safetyCenter.action">开启支付密码</a>
                         </div>
                         <div class="addsucc-tips" style="display: none">
                             <i></i>
                             <span>礼品卡已领取成功</span>
                         </div>
                     </div>
                 </div>
                          <!-- consignment -->
                              <div class="accesskey-main ui-switchable-panel" >
                     <div class="accesskey-cont" id="consignment_card">
                         <div class="accesskey-tab ml20" >
                             <ul>
                                 <li class="accesskey-tab-item"
                                     clstag="pageclick|keycount|xunizichan__2016031015|9">可用
                                 </li>
                                 <li class="accesskey-tab-item"
                                     clstag="pageclick|keycount|xunizichan__2016031015|9">不可用
                                 </li>
                                 <li class="accesskey-tab-item"
                                     clstag="pageclick|keycount|xunizichan__2016031015|10">添加领货码
                                 </li>
                             </ul>
                         </div>
                         <div class="accesskey-tab-panel-main ml20">
                             <div class="accesskey-tab-panel">
                                 <div class="accesskey-scrollbar-origin">
                                     <div class="ui-scrollbar-main-gift">
                                         <div class="accesskey-scroll">
                                             <div class="accesskey-enable">
                                             </div>
                                         </div>
                                         <p class="ac mt10 mb10 ftx08 fts14" style="display: none;">
                                             <span class="loading"><b></b>加载中...</span>
                                         </p>
                                         <p class="ac mt5 mb10 ftx08 fts14" style="display: none;">
                                             没有更多了~
                                         </p>
                                     </div>
                                     <div class="warn-tips" style="display: none;">
                                         <i></i>
                                         <span>已超出单笔订单领货码使用张数上限</span>
                                     </div>
                                 </div>
                             </div>
                         </div>
                         <div class="accesskey-tab-panel-main ml20">
                             <div class="accesskey-tab-panel">
                                 <div class="accesskey-scrollbar-origin">
                                     <div class="ui-scrollbar-main-gift">
                                         <div class="accesskey-scroll">
                                             <div class="accesskey-disable">
                                             </div>
                                         </div>
                                         <p class="ac mt10 mb10 ftx08 fts14" style="display: none;">
                                             <span class="loading"><b></b>加载中...</span>
                                         </p>
                                         <p class="ac mt5 mb10 ftx08 fts14" style="display: none;">
                                             没有更多了~
                                         </p>
                                     </div>
                                 </div>
                             </div>
                         </div>
                         <div class="accesskey-tab-panel ui-switchable-panel-selected hide ">
                             <div class="accesskey-add">

                             </div>
                         </div>
                         <div class="ftx01 safeLpkPart" style="display:none;" id="safeLpkPart">为保障您的账户资金安全，张京东E卡/图书卡/京东卡暂不可用，请先
                             <a target="_blank" href="http://safe.jd.com/user/paymentpassword/safetyCenter.action">开启支付密码</a>
                         </div>
                         <div class="addsucc-tips" style="display: none">
                             <i></i>
                             <span>礼品卡已领取成功</span>
                         </div>
                     </div>
                 </div>
                                    <!-- balance -->
            <div class="balance-main ui-switchable-panel">
                <div class="form v-balance ml20" id="jdBalance" clstag="pageclick|keycount|xunizichan__2016031015|12">
                      <input id="selectOrderBalance" type="checkbox" class="jdcheckbox"  value="" >
                      <label id="canUsedBalanceId" for="selectOrderBalance">
                        &nbsp;使用余额（账户当前余额：<span >0.00</span>元）
                                              </label>
                        <div class="ftx01 safeLpkPart hide" id="safeBalancePart">
                            为保障您的账户资金安全，余额暂不可用，请先
                            <a target="_blank"
                               href="//safe.jd.com/user/paymentpassword/safetyCenter.action">[开启支付密码]</a>
                        </div>

                </div>
            </div>
                        <div class="virtual-usedcont-new" id="virtual_status">
              <span class="virtual-usedcont-price">金额抵用<em id="total">￥</em></span>
              <ul class="virtual-usedcont-detail">
                <li id="couponTotalShow" style="display: none;">使用优惠券<em ></em>张，优惠<em></em>元 </li>
                <li id="freeFreightShow" style="display: none;">| 使用运费券<em></em>张，抵用运费<em></em>元 </li>
                <li id="redPacketShow" >| 使用红包，抵用<em>0.00</em>元<li>
                <li id="jdBeanShow" style="display: none;">| 使用京豆，抵用<em></em>元<li>
                <li id="giftCardShow" style="display: none;">| 使用京东E卡<em></em>张，抵用<em></em>元</li>
                <li id="consignmentCardShow" style="display: none;">| 使用领货码<em></em>张，抵用<em></em>元</li>
                <li id="balanceShow" style="display: none;">| 使用余额，抵用<em></em>元</li>
              </ul>
            </div>
        </div>
    </div>


<!-- TODO need delete-->
<script id="virtual_status_tmp" type="text/temp">
     <span class="virtual-usedcont-price">金额抵用<em id="total">￥{{orderPrice.virtualTotalDiscount}}</em></span>
     <ul class="virtual-usedcont-detail">
        <li id="couponTotalShow" style="display: {{if orderPrice.couponDiscount > 0}} {{set more = true}} {{else}} none{{/if}};">使用优惠券<em>{{orderPrice.couponNum}}</em>张，优惠<em>{{orderPrice.couponDiscount}}</em>元 </li>
        {{if orderPrice.freightCouponDiscount >0}} <li id="freeFreightShow"   style="display: ;">{{if more}}| {{/if}} 使用运费券<em>{{orderPrice.freightCouponNum}}</em>张，抵用运费<em>{{orderPrice.freightCouponDiscount}}</em>元 </li> {{set more = true}}{{else}}<li id="freeFreightShow" style="display: none;"></li>{{/if}}
        {{if orderPrice.redPacketDiscount > 0 && checked }}<li id="redPacketShow" style="display: ;">{{if more}}|{{/if}} 使用红包，抵用<em>{{orderPrice.redPacketDiscount}}</em>元</li> {{set more = true}}{{else}}<li id="redPacketShow" style="display: none;">{{/if}}
        {{if orderPrice.jdBeanDiscount >0 }}<li id="jdBeanShow" style="display: ;">{{if more}}|{{/if}}使用京豆，抵用<em>{{orderPrice.jdBeanDiscount}}</em>元</li>{{set more = true}}{{else}}<li id="jdBeanShow" style="display: none;"></li>{{/if}}
        {{if orderPrice.giftCardDiscount >0 }}<li id="giftCardShow" style="display: ;">{{if more}}|{{/if}}使用京东E卡<em>{{orderPrice.giftCardNum}}</em>张，抵用<em>{{orderPrice.giftCardDiscount}}</em>元</li>{{set more = true}}{{else}}<li id="giftCardShow" style="display: none;"></li>{{/if}}
        {{if orderPrice.consignmentCardDiscount >0 }}<li id="consignmentCardShow" style="display: ;">{{if more}}|{{/if}}使用领货码<em>{{orderPrice.consignmentCardNum}}</em>张，抵用<em>{{orderPrice.consignmentCardDiscount}}</em>元</li>{{set more = true}}{{else}}<li id="consignmentCardShow" style="display: none;"></li>{{/if}}
        {{if orderPrice.balanceDiscount >0 }}<li id="balanceShow" style="display: ;">{{if more}}|{{/if}}使用余额，抵用<em>{{orderPrice.balanceDiscount}}</em>元</li>{{set more = true}}{{else}}<li id="balanceShow" style="display: none;"></li>{{/if}}
      </ul>
</script>
<script id="virtual_balance_tmp" type="text/temp">
    <input id="selectOrderBalance" type="checkbox" class="jdcheckbox"  {{if checked}} checked="checked" {{/if}} />
    <label id="canUsedBalanceId" for="selectOrderBalance">&nbsp;使用余额（账户当前余额：<span >￥{{balance}}</span>元）
        {{if checked}} ，本次使用<span class='ftx-01'>￥{{balanceDiscount}}</span>{{/if}}
    </label>
    <div class="ftx01 safeLpkPart hide" id="safeBalancePart">
        为保障您的账户资金安全，余额暂不可用，请先
        <a target="_blank"
           href="//safe.jd.com/user/paymentpassword/safetyCenter.action">[开启支付密码]</a>
    </div>
</script>
                    <!--/  /widget/order-coupon/order-coupon.tpl -->
                                    </div>
        <!-- </div> -->
        <!-- </div> -->
        <!--  /widget/order-summary/order-summary.tpl -->
        <div class="order-summary">
            <!--  预售 计算支付展现方式 begin -->
                            <div class="statistic fr">
                    <div class="list">
                        <span><em class="ftx-01">1</em> 件商品，总商品金额：</span>
                        <em class="price" id="warePriceId"
                            v="5499.00">￥5499.00</em>
                    </div>
                    <div class="list" id="shuifeiId">
                        <span>税费：</span>
                        <em class="price" id="gstTaxAmountId" > <i class="freight-icon gstTaxAmount"></i><font color="#FF6600"> ￥0.00 </font></em>
                    </div>
                    <div class="list hide" id="crossRegionalFeetip">
                        <span>调货服务费：</span>
                        <em class="price" id="crossRegionalFeeId" > <i class="freight-icon crossRegionalFee"></i><font color="#FF6600"> ￥0.00 </font></em>
                    </div>
                    <div class="list">
                        <span>运费：</span>
                        <em class="price" id="freightPriceId"> ￥0.00</em>
                    </div>
                    <div class="list hide" id="honorFeetip">
                        <span>京尊达服务费：</span>
                        <em class="price" id="honorFeetipPrice" > <i class="freight-icon honorFeetipPrice"></i><font color="#FF6600"></font></em>
                    </div>
                    <div class="list hide" id="packagingServicesFeetip">
                        <span>循环包装服务费：</span>
                        <em class="price" id="packagingServicesFeetipPrice" ><font color="#FF6600"></font></em>
                    </div>
                    <div class="list"                          style="display:block;"  id="fuwufeeId">
                        <span>服务费：</span>
                        <em class="price" id="serviceFeeId">￥0.00</em>
                    </div>

                    <div class="list" id="showPeriodFee" style="display:none;">
                        <span>分期手续费(由分期银行收取)：</span><em class="price" id="periodFee">￥0.00</em>
                    </div>
                    <div class="list"                          style="display:;"  id="buyerFreightDivId">
                        <span>退换无忧：</span>
                        <em class="price" id="buyerFreightInsuranceId">￥0.00</em>
                    </div>
                    <div class="list hide" id="cachBackdivId">
                        <span>返现：</span>
                        <em class="price" id="cachBackId" v="0.00"> -￥0.00</em>
                    </div>
                    <div class="list"
                         id="showCouponPrice"  style="display:none;"  >
                        <input id="couponPriceNum" type="hidden" value="0"/>
                        <input id="couponPricehidden" type="hidden" value="0.00"/>
                        <span>商品优惠：</span><em class="price" id='couponPriceId'>-￥0.00</em>
                    </div>
                    <div class="list"
                         id="showFreeFreight"  style="display:none;"  >
                        <input id="freeFreightPriceNum" type="hidden" value="0"/>
                        <input id="freeFreightPricehidden" type="hidden" value="0.00"/>
                        <span>运费券：</span><em class="price" id="freeFreightPriceId"> -￥0.00</em>
                    </div>
                    <div class="list hide" id="sqqtsFeetip">
                        <span>运费优惠：</span>
                        <em class="price" id="sqqtsFeeId" > <i class="freight-icon sqqtsFee"></i><font color="#FF6600"></font></em>
                    </div>
                                        <div class="list" id="showUsedJdBean"  style="display:none;"  >
                        <input type="hidden" id="jdBeanexChange" value="0">
                        <span>京豆：</span><em class="price" id='usedJdBeanId'>-￥0</em>
                    </div>
                    <div class="list"
                         id="showGiftCardPrice"  style="display:none;"  >
                        <input id="giftCardPricehidden" type="hidden" value="0.00"/>
                        <input id="giftCardPriceNum" type="hidden" value="0"/>
                        <span> 礼品卡： </span><em class="price"
                                                                                       id='giftCardPriceId'>-￥ 0.00</em>
                    </div>
                    <div class="list"
                         id="consignmentCardPrice"  style="display:none;"  >
                        <input id="consignmentCardDiscounthidden" type="hidden" value="0"/>
                        <input id="consignmentCardNum" type="hidden" value="0"/>
                        <span>领货码： </span><em class="price"
                                              id='gconsignmentCardId'>-￥ 0</em>
                    </div>
                    <div class="list"
                         id="showUsedOrderBalance"  style="display:none;"  >
                        <input type="hidden" id="useBalanceShowDiscount" value="0.00">
                        <span>余额：</span><em class="price" id='usedBalanceId'>-￥0.00</em>
                    </div>


                </div>
                <div class="clr"></div>
                    </div>
        <!--/ /widget/order-summary/order-summary.tpl -->
        <!-- 运费弹窗显示 -->
        <div id="tooltip-box06" class="hide">
                        <div class="summary-freight-box-new">
                <div class="sfb-tit" >
                    <span>店铺运费明细</span>
                    <span class="ml5 ftx-03" id="frightDetail"></span>
                </div>
                <div class="sfb-con">
                                                                                                                <!-- 只包含延保商品的商家不显示 -->
                                                                                                                                                                                    <div class="sfb-item">
                                                                <div class="sfb-item-tit">
                                                                                                                        <span class="vendor_name_freight vendor_name_0" id="0">
                                                京东自营                                            </span>
                                                                                <em class="ftx-03 hide" id="xzweight-detail-bak">
                                            （总重2.680kg
                                                                                            ）
                                                                                    </em>
                                        <em class="ftx-03 hide" id="sxweight-detail-bak">
                                            （总重
                                                                                            ）
                                                                                    </em>
                                        <em class="ftx-03 hide" id="wmweight-detail-bak">
                                            （总重2.680kg
                                                                                            ）
                                                                                    </em>
                                                                    </div>
                                <!-- begin 运费明细块 -->
                                                                    <div class="sfb-item-info" id="normal-freight-container">
                                    <span class="sfb-item-info-tit normal-freight-title">非生鲜商品
                                        <em class="ftx-03 hide" id="xzweight-detail">
                                            （总重2.680kg
                                                                                            ）
                                                                                    </em>
                                    </span>
                                        <span>基础运费：<b class="ftx-01 base-freight"></b><a href="http://help.jd.com/user/issue/109-3492.html" target="_blank" class="ml5 ftx-05 hide" id="freighttips">查看港澳台地区收费标准</a></span>
                                        <span class="hide">续重运费：<b class="ftx-01 xz-freight"></b><a href="http://help.jd.com/user/issue/109-188.html" target="_blank" class="ml5 ftx-05">查看续重标准></a></span>
                                        <span class="hide">续重运费：<b class="ftx-01 overseaxz-freight"></b><a href="http://help.jd.com/user/issue/109-3492.html" target="_blank" class="ml5 ftx-05">查看续重标准></a></span>
                                        <span class="hide">海外地区附加燃油费：<b class="ftx-01 fuel-freight"></b></span>
										<span class="hide" id="fts-base">非图书基础运费：<b class="ftx-01 fts-base-freight"></b><a href="http://help.jd.com/user/issue/109-3492.html" target="_blank" class="ml5 ftx-05 hide" id="ftsfreighttips">查看港澳台地区收费标准</a></span>
										<span class="hide" id="ts-base">图书基础运费：<b class="ftx-01 ts-base-freight"></b><a href="http://help.jd.com/user/issue/109-3492.html" target="_blank" class="ml5 ftx-05 hide" id="tsfreighttips">查看港澳台地区收费标准</a></span>
                                        <span class="hide">免运费<b class="ftx-01 free-freight" freightByVenderId="0" popJdShipment="false"></b></span>
                                    </div>
                                    <div class="hr" id="sx-freight-split-line"></div>
                                    <div class="sfb-item-info hide" id="sx-freight-container">
                                    <span class="sfb-item-info-tit sx-freight-title">生鲜商品
                                        <em class="ftx-03 hide" id="sxweight-detail">
                                            （总重
                                                                                            ）
                                                                                    </em>
                                    </span>
                                        <span>基础运费：<b class="ftx-01 base-freight"></b></span>
                                        <span class="hide">续重运费：<b class="ftx-01 xz-freight">￥20.00</b><a href="http://help.jd.com/user/issue/109-188.html" target="_blank" class="ml5 ftx-05">查看续重标准></a></span>
                                        <span class="hide">免运费<b class="ftx-01 free-freight" freightByVenderId="0" popJdShipment="false"></b></span>
                                    </div>
                                    <div class="hr" id="ext-freight-split-line"></div>
                                    <div class="sfb-item-info hide" id="ext-freight-container">
                                        <span class="hide">非生鲜京准达运费：<b class="ftx-01 jzd-freight"></b></span>
                                        <span class="hide">非生鲜中小件极速达运费：<b class="ftx-01 jsd-freight"></b></span>
                                        <span class="hide">非生鲜大件极速达运费：<b class="ftx-01 djsd-freight"></b></span>
                                        <span class="hide">大件京准达运费：<b class="ftx-01 djzd-freight"></b></span>
                                        <span class="hide">生鲜京准达运费：<b class="ftx-01 jzdsx-freight"></b></span>
                                        <span class="hide">生鲜大件极速达运费：<b class="ftx-01 jzdsxdj-freight"></b></span>
                                        <span class="hide">生鲜极速达运费：<b class="ftx-01 jsdsx-freight"></b></span>
                                        <span class="hide">生鲜同城速配运费：<b class="ftx-01 sx-gsd-freight"></b></span>
                                        <span class="hide">非生鲜同城速配运费：<b class="ftx-01 fsx-gsd-freight"></b></span>
                                    </div>
									<div class="sfb-item-info hide" id="shds-freight-container">
                                        <span>基础运费：<b class="ftx-01 base-freight"></b></span>
                                        <span class="hide">续重运费：<b class="ftx-01 sds-xz-freight"></b><a href="http://help.jd.com/user/issue/109-188.html" target="_blank" class="ml5 ftx-05">查看续重标准></a></span>
                                        <span class="hide">闪电送运费：<b class="ftx-01 sds-freight"></b></span>
                                        <span class="hide">免运费<b class="ftx-01 free-freight" freightByVenderId="0" popJdShipment="false"></b></span>
                                    </div>
                                                                <div class="sfb-item-goods">
                                    <div class="ui-switchable-body">
                                        <div class="ui-switchable-panel-main" >
                                                                                                                                                                                        <div class="ui-switchable-panel" >
                                                <ul class="sfb-goods-list">
                                                                                                                                                                                                    <li id="6072622" class="sfb-goods-item" >
                                                        <a href="#none" title="联想ThinkPad 翼480（0VCD）英特尔8代酷睿14英寸轻薄窄边框笔记本电脑（i5-8250U 8G 128GSSD+500G 2G独显）"><img height="50" width="50" src="//img12.360buyimg.com/n3/jfs/t28210/176/166163755/271400/2e654ec0/5bea36b6N79ca2695.jpg" alt=""/></a>
                                                        														                                                    </li>
                                                                                                                                                                                                </ul>
                                                </div>
                                                                                                                                    </div>
                                    </div>
                                    <div class="sfb-ui-switchable-page" >
                                        <a href="javascript:void(0)" class="sfb-prev">&lt;</a>
                                        <a href="javascript:void(0)" class="sfb-next">&gt;</a>
                                    </div>
                                </div>
                            </div>
                                                            </div>
            </div>
        </div>
        <div id="tooltip-box11" class="hide">
			            <div class="summary-freight-box-new">
                <div class="sfb-tit">
                    <span>店铺运费明细</span>
					<span class="ml5 ftx-03"><em class="ml5 ftx-01" id="sqqtsFeetotal" ></em></span>
                </div>
                <div class="sfb-con">
                    <div class="sfb-item">
                        <div class="sfb-item-tit">
                            <span>京东自营</span>
                        </div>
						 <div class="sfb-item-info">
							<span class="hide" id="ftsyh-fee-span" >非图书运费优惠：<b class="ftx-01" id="ftsyh-fee"></b></span>
							<span class="hide" id="tsyh-fee-span">图书运费优惠：<b class="ftx-01"  id="tsyh-fee"></b></span>
                         </div>
                    </div>
					<div class="sfb-item-goods">
                                    <div class="ui-switchable-body">
                                        <div class="ui-switchable-panel-main" >
                                                                                                                                                                                        <div class="ui-switchable-panel" >
                                                <ul class="sfb-goods-list">
                                                                                                                                                                                                    <li id="6072622" class="sfb-goods-item" >
                                                        <a href="#none" title="联想ThinkPad 翼480（0VCD）英特尔8代酷睿14英寸轻薄窄边框笔记本电脑（i5-8250U 8G 128GSSD+500G 2G独显）"><img height="50" width="50" src="//img12.360buyimg.com/n3/jfs/t28210/176/166163755/271400/2e654ec0/5bea36b6N79ca2695.jpg" alt=""/></a>
                                                        														                                                    </li>
                                                                                                                                                                                                </ul>
                                                </div>
                                                                                                                                    </div>
                                    </div>
                                    <div class="sfb-ui-switchable-page" >
                                        <a href="javascript:void(0)" class="sfb-prev">&lt;</a>
                                        <a href="javascript:void(0)" class="sfb-next">&gt;</a>
                                    </div>
                                </div>
                            </div>
            </div>
        </div>
		
		<div id="tooltip-box10" class="hide">
            <div class="summary-freight-box-new">
                <div class="sfb-tit">
                    <span>调货服务费</span>
                    <span class="ml5 ftx-03"><em class="ml5 ftx-01" id="totalCrossRegionalFee" >总计 ¥0</em></span>
                </div>
                <div class="sfb-con">
                    <div class="sfb-item">
                        <div class="sfb-item-tit">
                            <span>调货商品</span>
                        </div>
                    </div>
                </div>
                <div class="sfb-item-goods" id="crossSkus">
                </div>
            </div>
        </div>
        <!-- 运费弹窗结束-->
        <div id="tooltip-box09" class="hide">
            <div class="plus-box-cont">
                <div class="pbox-tit">
                    <strong class="fl"><em class="ftx-01" id="totalNum">0</em>件商品有PLUS专享价</strong>
                    <span class="ml5 ftx-03 fr">可省<em class="ml5 ftx-01" id="totalPricetip">￥0</em></span>
                </div>
                <div class="pbox-con" id="plusProducts">
                    <ul>
                                            </ul>
                </div>
            </div>
        </div>
        <!--  /widget/checkout-floatbar/checkout-floatbar.tpl -->
        <div class="trade-foot">
            <div id="plusInfoByFreight" class="hide"></div>
            <div id="plusInfo" class="hide"></div>
            <div class="trade-foot-detail-com">
                                    <div class="fc-price-info">
                        <span class="price-tit">应付总额：</span>
                        <span class="price-num" id="sumPayPriceId">￥5499.00</span>
                    </div>
                    <div class="fc-baitiao-info" style="display: none;">
                        <span>白条支付：<em>不分期</em>（不使用优惠）<i class="bt-edit-icon" onclick="javascript:btDetail();" clstag="pageclick|keycount|PaymentLead__2016030411|5"></i></span>
                    </div>
                    <div class="giftbuy-info">
                        <label class="noShowMoney hide" id="giftBuyHidePriceDiv">
                            <input type="checkbox" id="giftBuyHidePrice" checked>包装内不显示礼品价格
                        </label>
                    </div>
                                <div class="fc-consignee-info">
                    <span class="mr20" id="sendAddr">寄送至： 湖北 武汉市 江夏区 城区  武汉工程大学流芳校区泰塑公寓</span>
                    <span id="sendMobile">收货人：曹炎 176****3600</span>
                </div>
            </div>
            <!-- 支付密码 -->
            <div class="pay-pwd mt10 hide" id="paypasswordPanel">
                <div id="payPassword_container" class="alieditContainer clearfix" data-busy="0">
                    <label for="i_payPassword" class="i-block">支付密码：</label>
                    <div class="i-block">
                        <div class="i-block six-password">
                            <input class="i-text sixDigitPassword" id="txt_paypassword" type="password" autocomplete="off" required="required" value="" name="payPassword_rsainput" data-role="sixDigitPassword" tabindex="" maxlength="6" minlength="6" aria-required="true" AUTOCOMPLETE="off" onchange='clearError()'>
                            <div tabindex="0" class="sixDigitPassword-box">
                                <i><b></b></i>
                                <i><b></b></i>
                                <i><b></b></i>
                                <i><b></b></i>
                                <i><b></b></i>
                                <i><b></b></i>
                                <span id="cardwrap" data-role="cardwrap"></span>
                            </div>
                        </div>
                        <span class="forgot-password">
	                  <a target="_blank" href="//safe.jd.com/user/paymentpassword/getBackPassword.action">
	                 	 忘记密码？
	                  </a>
	              </span>
                    </div>
                </div>
                <div id="no-pwd-error" class="pay-pwd-error hide">
                    <label class="error-msg" for="">请输入6位数字密码</label>
                </div>
                <div id="pwd-error" class="pay-pwd-error hide" style="margin-right:16px;">
                    <label class="error-msg" for=""></label>
                </div>
                <div class="payment-bt-tips hide">
                    <span class="bt-tips-cont">结算金额变动，请重新选择白条分期以及白条优惠</span><i class="bt-tips-close" onclick="closebtErrorTip();">×</i>
                </div>
            </div>
            <!-- 预售 -->
                        <!-- 全球售、台湾售、香港售 -->
            <div class="hkmtbuy-con hide" id="overseamtbuy-area">
                <div class="hkmtbuy-chk">
                    <label for=""><input type="checkbox" checked="" id="overseamtbuy" name="">已阅读并同意</label><a href="" class="ftx05" onclick="javascript:return openOverseaAgree();">《售全球服务协议》</a>
                </div>
            </div>
            <!-- 快递到车 -->
            <div class="hkmtbuy-con hide" id="car_Agreement_tips">
                <div class="hkmtbuy-chk">
                    <label for=""><input type="checkbox" id="car_Agreement_check" name="">我已阅读并同意</label><a href="#none" class="ftx05" id="J_kuaididaoche-btn">《送货到车免责协议》</a>
                </div>
            </div>

            <!-- 快递到车 -->
            <div class="hkmtbuy-con hide" id="car_Agreement_tips">
                <div class="hkmtbuy-chk">
                    <label for=""><input type="checkbox" id="car_Agreement_check" name="">我已阅读并同意</label><a href="#none" class="ftx05" id="J_kuaididaoche-btn">《送货到车免责协议》</a>
                </div>
            </div>


            <div id="checkout-floatbar" class="group">
                <div class="ui-ceilinglamp checkout-buttons">
                    <div class="sticky-placeholder hide" style="display: none;">
                    </div>
                    <div class="sticky-wrap">
                        <div class="inner">
                                                            <button type="submit" class="checkout-submit" id="order-submit"
                                        onclick="javascript:submit_Order(null,2);" clstag="pageclick|keycount|trade_201602181|25">
                                    提交订单<b></b>
                                </button>
                                                                                        <button type="submit" id="enterPriseUserPaymentSubmit" style="display:none;" class="checkout-submit-combine" onclick="javascript:submit_Order(1);" data-tips="若您要下多个订单，可以先提交订单再去订单中心合并支付，效率更高哟~">
                                    提交订单暂不支付
                                </button>
                                                        <span id="checkCodeDiv"></span>

                            <div class="checkout-submit-tip" id="changeAreaAndPrice" style="display: none;">
                                由于价格可能发生变化，请核对后再提交订单
                            </div>
                            <!--div style="display:none" id="factoryShipCodShowDivBottom" class="dispatching">
                              部分商品货到付款方式：先由京东配送“提货单”并收款，然后厂商发货。
                            </div-->
                        </div>
                        <span id="submit_message" style="display:none" class="submit-error"></span>

                        <div class="submit-check-info" id="submit_check_info_message" style="display:none"></div>
                    </div>
                </div>
            </div>

        </div>
        <!--/ /widget/checkout-floatbar/checkout-floatbar.tpl -->

        <!--  /widget/backpanel/backpanel.tpl -->
        <div id="backpanel">
            <div id="backpanel-inner" class="hide switchOn">
                                    <div class="bp-item bp-item-survey">
                        <a href="http://surveys.jd.com/index.php?r=survey/index/sid/416587/lang/zh-Hans" class="survey" target="_blank">我要反馈</a>
                    </div>
                                <div class="bp-item bp-item-backtop" data-top="0">
                    <a href="#none" class="backtop" target="_self">返回顶部</a>
                </div>
            </div>
        </div>
        <!--/ /widget/backpanel/backpanel.tpl -->

    </div>

</div>


<!-- /main -->

<!--  /widget/footer/footer.tpl -->
<!-- footer -->
<!--service start-->
<div id="service-2017">
	<div class="w">
		<ol class="slogen">
			<li class="item fore1">
				<i>多</i>品类齐全，轻松购物
			</li>
			<li class="item fore2">
				<i>快</i>多仓直发，极速配送
			</li>
			<li class="item fore3">
				<i>好</i>正品行货，精致服务
			</li>
			<li class="item fore4">
				<i>省</i>天天低价，畅选无忧
			</li>
		</ol>
	</div>
	<div class="jd-help">
		<div class="w">
			<div class="wrap">
				<dl class="fore1">
					<dt>购物指南</dt>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-29.html">购物流程</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-151.html">会员介绍</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-297.html">生活旅行/团购</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue.html">常见问题</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-136.html">大家电</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/index.html">联系客服</a></dd>
				</dl>
				<dl class="fore2">		
					<dt>配送方式</dt>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-81-100.html">上门自提</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-81.html">211限时达</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/103-983.html">配送服务查询</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/109-188.html">配送费收取标准</a></dd>				
					<dd><a target="_blank" href="//help.joybuy.com/help/question-list-201.html">海外配送</a></dd>
				</dl>
				<dl class="fore3">
					<dt>支付方式</dt>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-172.html">货到付款</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-173.html">在线支付</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-176.html">分期付款</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-174.html">邮局汇款</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-175.html">公司转账</a></dd>
				</dl>
				<dl class="fore4">		
					<dt>售后服务</dt>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/321-981.html">售后政策</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-132.html">价格保护</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/130-978.html">退款说明</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//myjd.jd.com/repair/repairs.action">返修/退换货</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-50.html">取消订单</a></dd>
				</dl>
				<dl class="fore5">
					<dt>特色服务</dt>	
					<dd><a target="_blank" href="//help.jd.com/user/issue/list-133.html">夺宝岛</a></dd>
					<dd><a target="_blank" href="//help.jd.com/user/issue/list-134.html">DIY装机</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//fuwu.jd.com/">延保服务</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//o.jd.com/market/index.action">京东E卡</a></dd>				
					<dd><a rel="nofollow" target="_blank" href="//mobile.jd.com/">京东通信</a></dd>
					<dd><a rel="nofollow" target="_blank" href="//s.jd.com/">京东JD+</a></dd>
				</dl>
				<span class="clr"></span>
			</div>
		</div>
	</div>
</div>
<!--service end-->

<script type="text/javascript" rel="stylesheet" src="//misc.360buyimg.com/user/purchase/2.0.0/widget/??/checkout-floatbar/checkout-floatbar.js,backpanel/backpanel.js" source="widget"></script>
<script type="text/javascript" rel="stylesheet" src="//misc.360buyimg.com/user/purchase/2.0.0/js/paypwd.js"></script>
<script>
    $("#consignee_id").val('138479095');
    $("#hideAreaIds").val('17-1381-50713-52576');
</script>
<!-- 不支持自提商品列表隐藏域  -->
<script id="noSupSkus_hideDiv" type="text/temp">&nbsp;</script>
<!-- 港澳售项目 -->
<script id="hkmt-box01" type="text/temp">
<div class="hkmt-thickbox-warn">
	<div class="tip-box icon-box-new">
		<span class="warn-icon-yellow m-icon"></span>
		<div class="item-fore">
			<span>订单中部分商品不支持对当前地址的配送<br>请返回购物车修改</span>
		</div>
	</div>
	<div class="op-btns ac mt30 mb30">
		<a href="//cart.jd.com" class="btn-1">返回购物车</a>
		<a href="#none" class="btn-9 ml10" onclick="javascript:closeDialog();">取消</a>
	</div>
</div>
</script>
<!-- 海外、台湾协议 -->
<style>
    .overseaConfirmBtn a {
        padding:5px 50px;
        margin-top:15px;
        color:#fff;
        background:#e22;
        border:0;
        font-size:16px;
        font-family:"Microsoft YaHei","Hiragino Sans GB";
    }
    .hkbuy-dialog p {
        line-height:20px;
        margin:10px;
    }
</style>
<style>
    .tableborder {
        border-right-width: 1px;
        border-bottom-width: 1px;
        border-right-style: solid;
        border-bottom-style: solid;
    }
    .tableborder th{
        border-top-width: 1px;
        border-left-width: 1px;
        border-top-style: solid;
        border-left-style: solid;
    }
    .tableborder td{
        border-top-width: 1px;
        border-left-width: 1px;
        border-top-style: solid;
        border-left-style: solid;
    }
</style>
<script id="overseabuy-box01" type="text/temp">
	<div class="hkbuy-dialog" style="height: 450px; width: 910px;overflow:auto;margin:10px;">
		<p class="agreement-cont">
			<h3>一、协议内容与效力</h3>
			<p>本服务协议由您与广州晶东贸易有限公司共同缔结，本协议具有合同效力。本协议中协议双方合称协议方，广州晶东贸易有限公司在本协议中亦称为京东。 </p>
			<p>您在JD.COM购买页面上勾选《售全球服务协议》前，请您仔细阅读本协议的全部内容。如果您对本协议的条款有疑问的，请通过京东客服渠道进行询问，京东将向您解释条款内容。如果您不同意本协议的任意内容，或者无法准确理解京东对条款的解释，请不要勾选《售全球服务协议》和进行后续操作。您通过网络页面点击勾选、确认或以其他方式选择接受本协议，即表示您同意接受本协议的全部内容。 </p>
			<p>您勾选该服务时，相应服务费用将向您进行相应展示，您勾选该服务，即视为您接受该服务的相应价格。服务商有权不定时修订该价格，服务商修改价格后，如您继续选择《售全球服务协议》，视为您接受修改后的价格。 </p>
			<p>如您不同意相关变更，应停止使用本服务。经修订的协议及规则一经公布后，立即自动生效，成为本协议的有效组成部分。登陆或继续使用“本服务”将表示您接受经修订的协议。如果您不同意本协议之内容，或者您所属的国家或地方排除本协议内容之一部或全部时，请您立即停止使用本服务。 </p>
			<p>您同意于使用本服务时，您全部之意思表示，均以电子文件作为表示方法，如您于各项服务与功能等页面点选同意或确认等功能键时，即视为您正式之意思表示。 </p>
			<p>本协议是京东为向您提供售全球服务而与您特别订立的协议。本协议的生效不代表您与京东订立的其他协议失去效力。除非另有特别约定，您与京东订立的包括《用户注册协议》在内的任何协议均继续有效，您仍然应当遵守各协议的相关约定。各协议之间约定存在冲突的，以特别约定优先于一般约定，后订立的约定优先于先订立的约定为原则进行处理。</p>
			<br/>
			<h3>二、服务及相关约定</h3>
			<p>1. 京东向您提供售全球服务，服务模式为：</p>
			<p>（1）如您在京东商城提交订单时填写港澳、台湾、海外收货地址，则系统默认使用港澳、台湾、海外直运。 </p>
			<p>（2）合作承运商按照您的收货地址信息安排运输并配送到您指定的港澳、台湾、海外收货地址。</p>
			<p>2. 在您选择直运服务过程中，您承诺遵守以下约定： </p>
			<p>（1） 您同意一旦使用本服务即同意您所授权京东的合作承运商有权知晓及使用您的相关交易信息，包括收件人姓名，身份证件号码及联系方式等，且该等信息因清关及为符合法律的规定而经由承运商提供给海关及/或其他相关部门。 </p>
			<p>（2）您同意在领取包裹时需确认外包装完好后方进行签收，您签收包裹即表示包裹外包装完好；您同意并在此确认，如您收货时包裹外包装完好，则直运服务即符合本协议相应约定。签收后发生的包裹损坏、毁损、遗失等情况京东不承担相关责任。</p>
			<p>3、本网站提供的商品说明：</p>
			<p>（1）本网站所售商品（包含电器类商品），除特别说明的商品外，均为中国大陆地区版本；</p>
			<p>（2）非中国大陆地区用户购买使用3C数码及电器类商品，如商品使用地区插头插座与商品所附插头插座标准不一致，用户需自行单独购买符合当地标准的“转换器”配套使用；</p>
			<p>（3）本网站所售商品仅符合中国大陆地区安全标准和使用习惯，如若商品使用地区安全标准和使用习惯与中国大陆地区不一致，请谨慎购买使用，因此可能造成的损失，京东不承担相关责任；</p>
			<p>（4）生产商提供的质保及售后服务可能不覆盖目的国；</p>
			<p>（5）本网站所售商品的商品标签和包装、手册、说明书及安全警示可能未涵盖目的国语言版本；</p>
			<br/>
			<h3>三、用户行为规则</h3>
			<p>用户通过京东账户操作的各种行为应符合法律法规规定、平台规则规定及注册协议约定，当出现（包含但不限于）以下行为时，视为用户自愿同意接受京东或商家进行权益降级，扣除京豆，冻结或关闭京东账户，取消订单，不再提供服务等操作，且同意京东或商家不进行任何赔偿或补偿。如给京东或相关方造成损失，用户愿意承担相应责任：</p>
			<p>（1） 注册资料内容含虚假信息；</p>
			<p>（2） 虚假交易、虚假好评,发布无根据的恶意评价；</p>
			<p>（3） 购买正品商品，退货时退回非京东平台对应订单中销售的商品、以次充好、以假乱真等行为；</p>
			<p>（4） 无故、无正常理由拒收签收订单货物的行为（此种情况下，京东不予退款）；</p>
			<p>（5） 符合非正常订单中的行为；</p>
			<br/>
			<h3>四、下单</h3>
			<p>1. 订购的商品价格以您下订单时京东网上价格为准。</p>
			<p>2. 请您清楚准确地填写您的真实姓名、送货地址及联系方式。因如下情况造成订单延迟或无法配送等，京东将不承担责任：</p>
			<p>A. 客户提供错误信息和不详细的地址； </p>
			<p>B. 货物送达无人签收，由此造成的重复配送所产生的费用及相关的后果； </p>
			<p>C. 不可抗力，例如：自然灾害、交通戒严、突发战争等。</p>
			<br/>
			<h3>五、配送</h3>
			<p>1、配送费用</p>
			<p>售全球运费将按照商品重量或者体积，两者取其大进行收取（若商品重量30kg或以上或商品体积的单边长度大于或等于90厘米，属于售全球不予销售范围），具体订单的运费以订单结算页公示金额为准。 如对运费收取有任何异议，请联系京东客服进行咨询沟通。</p>
			<p>2、进口责任</p>
			<p>购买售全球商品时，您对合法进口商品到目的国负全责，且为目的国清关时的进口方。商品的灭失风险及所有权自我们将其交付给承运人时即转移给您。您可能需缴纳目的国海关及税务部门征收的税费，这些税费会在货物进口至目的国时产生。关于此部分的详细信息请参见下文。您特别同意，您是商品的最终消费者或您将把商品作为礼物送给其他个人，且在任何情况下均为个人用途，非为转售而购买商品。</p>
			<p>3 、清关及进口税费</p>
			<p>3.1 商品到达目的国家清关时，根据目的国海关要求，收件人可能需要配合提供例如身份证明等相关资料进行清关，如因收件人提供清关资料不及时或不完整，导致货物清关失败，相关责任由收件人自行承担。</p>
			<p>3.2  进口税费</p>
			<p>&nbsp;&nbsp;京东不承担目的国的进口税费（包含关税、增值税、消费税等），通过京东销售的商品价格均未包含进口税费。如遇目的国海关查验、查扣等情景，您作为所购产品进口方有义务根据要求配合缴纳税费，否则无法保证配送成功。相关税费的具体缴纳方式应以当地承运商的通知为准。</p>
			<p>&nbsp;&nbsp;有些国家和地区的当地承运商会提前代垫进口税费（如关税，增值税，消费税等），并就代垫税费部分产生相应的服务费，您在签收包裹时需同时支付向承运商支付承运商所垫付的税费及相应服务费。如果您拒绝支付，我们将无法豁免此费用，同时您还需承担所购货物往返的运费。</p>
			<p>4、派送</p>
			<p>&nbsp;&nbsp;在正常派件失败后，会联系您前往承运商在收件地附近的派送点进行自提或联系承运商进行再次派送；承运商将为您在派送点保管包裹5个自然日，您需承担因此而产生的仓租费用及额外配送费用。逾期如您仍未到派送点自提或联系承运商进行再次派送，则京东有权按照当地的法律、行业惯例自行处理，不再对该包裹的存储，灭失等风险承担责任。 （注：根据承运商提供的实际承运方式的不同，部分承运方式在正常派件失败后，则需要您主动联系，前往包裹被存放的邮局进行自提；邮局保管包裹之时间与费用视您当地邮局政策所定，京东将不再另行通知于您；逾期行为之处理办法同上文所述。</p>
			<p>5、订单完成前的订单取消及商品退回</p>
			<p>&nbsp;&nbsp;若在订单跟踪详情里如显示该商品未转交至承运商，您可以取消订单；但由于跨境物流的特殊性，一旦京东将商品交至了物流承运商后您如选择取消订单，货物往返的运费及可能产生的关税费用需您自行承担。</p>
			<br/>
			<h3>六、适用法律及争议解决</h3>
			<p>本协议之解释与适用，以及与本协议有关的争议，均应依照中华人民共和国法律（不包括香港、澳门、台湾法律）予以处理。如发生任何争议，双方应尽力友好协商解决；协商不成时，任何一方均可向有管辖权的中华人民共和国大陆地区法院提起诉讼，同时您同意放弃因任何原因可能适用的任何其他司法管辖权。 </p>
			<br/>
			<h3>七、售后服务总则（只适用于港澳、台湾、海外地区）</h3>
			<p>&nbsp;&nbsp;售全球商品如属于下列“京东原因”支持订单完成后7天内退货，暂不支持换货、维修和补发。退回的货物所有权及灭失风险在货物抵达京东指定的库房后转移至京东。</p>
			<p>&nbsp;&nbsp;京东有权自主选择在不要求退货或者享有退回商品的所有权的前提下进行退款。</p>
			<table cellspacing="0" cellpadding="0" class="oversea-table tableborder">
				<tbody>
					<tr>
	                    <th><b>退货类别</b></th>
	                    <th><b>具体描述</b></th>
	                    <th><b>申请时间期限</b></th>
	                    <th><b>是否收取返回运费</b></th>
	                    <th><b>退回方式</b></th>
	                    <th><b>退回金额</b></th>
	                    <th><b>退款方式</b></th>
	                    <th><b>备注</b></th>
	                </tr>
	                <tr>
	                    <td>到货物流损、缺件或商品描述与网站不符等京东原因</td>
	                    <td>物流损指在运输过程中造成的损坏、漏液、破碎、性能故障，于收到货后24小时内反馈，经售后人员核查情况属实。缺件指商品原装配件缺失。</td>
	                    <td>收货后（且订单状态为完成）7天内申请售后退货</td>
	                    <td>否</td>
	                    <td>客户寄回</td>
	                    <td>全额（包括退回运费）</td>
	                    <td>退至账户余额</td>
	                    <td>京东审核期间可能需要您提供实物照片、视频等，以便售后人员快速做出判断并及时处理。</td>
	                </tr>
	                <tr>
	                    <td>不支持7天无理由退货</td>
	                    <td>非京东原因造成的，不支持顾客7天无理由退货</td>
	                    <td>不 支 持</td>
	                    <td>不 支 持</td>
	                    <td>不 支 持</td>
	                    <td>不 支 持</td>
	                    <td>不 支 持</td>
	                    <td>不 支 持</td>
	                </tr>
				</tbody>
			</table>
			<p>说明：</p>
			<p>1. 实际收货日期按照第三方物流平台显示的实际签收日期为准。</p>
			<p>2. 在商品退货时，需扣除购买该商品时通过评价或晒单所获得的京豆及相应优惠，如账户京豆已使用，则从商品退款金额中相应扣除；有赠品的主商品发生退货时，需将赠品一并提交退货返回，如赠品未退回，则主商品无法全额退款。</p>
			<p>3. 以下商品不支持“非京东原因”退货：</p>
			<p>（1） 个人定作类商品；</p>
			<p>（2）鲜活易腐类商品；</p>
			<p>（3）在线下载或者您拆封的音像制品，计算机软件等数字化商品； </p>
			<p>（4）交付的报纸期刊类商品；</p>
			<p>（5）其他根据商品性质不适宜退货，经您在购买时确认不宜退货的商品。</p>
			<h3>八、相关责任</h3>
			<p>&nbsp;&nbsp;在适用法律所允许的最大限度内，京东不承诺所有明示或默示的担保，包括但不限于对满足特定目的的默示担保。除非另有明确的书面说明，京东不对任何直接、间接或附带的惩罚性和结果性损害赔偿承担责任；且在任何情况下，京东承担的最大责任均不应超过就相关商品您所支付的成本。</p>
		</p>
	</div>
	<div id="overseabuy-box01-btn" class="op-btns overseaConfirmBtn ac">
		<a href="#none" class="btn-1">同意并继续</a>
	</div>
</script>
<script id="virtual-box01" type="text/temp">
    <div class="submit-warn-thickbox">
        <div class="tip-box icon-box-new">
            <span class="warn-icon m-icon"></span>
            <div class="item-fore">
                <h3>视频会员商品在实物订单妥投后不支持退货和退款，是否继续付款</h3>
            </div>
        </div>
        <div class="op-btns ac mt20 mb10">
            <a href="#none" onclick="javascript:parent.continue_SubmitOrder_for_norefund();closeDialog();" class="btn-1">继续支付</a>
            <a href="#none" class="btn-9 ml20" onclick="javascript:closeDialog();">取消</a>
        </div>
    </div>
</script>

<script type="text/javascript">
    function clearError(){
        $(".pay-pwd-error").hide();
    }
    /**
     * 关闭温馨提示
     */
    function closeorderInfotip(){
        $(".orderInfo-tip").hide();
    }

    $('.J_picksite_disable_info').hover(function() {
        $(this).next('.picksite-nosuport-box').show().css({
            left: $(this).offset().left - 17,
            top: $(this).offset().top + 28
        });
    });

    //$('.picksite-nosuport-box').mouseleave(function(event) {
    //   $(this).hide();
    //});
    $('.picksite-nosuport-cont').mouseleave(function(event) {
        $('.picksite-nosuport-box').hide();
    });



</script>
<script id="J_agreement_box1" type="text/temp">
  <div class="agreement-box">
      <div class="agreement-cont">
          
<div class="ui-scrollbar-main"> 
              <h3>快递到车服务用户协议</h3>  
              <p>请您在开始使用快递到车服务之前务必仔细阅读并理解以下服务条款（“本协议”）。</p>
			  <p>快递到车服务是由京东向汽车的所有权人及其授权使用人（“您”或“用户”）提供京东网站购买商品的快递配送到汽车的服务（“快递到车服务”或“本服务”）。</p>
              <h3 class="mt20">确认与接受</h3>
              <p>1.1京东在此特别提醒您认真阅读、充分理解本协议中各条款，包括免除或者限制配送责任的免责条款、限制用户权利的限制条款以及法律适用和争议解决条款。请您审慎阅读并选择接受或不接受本协议(未成年人应在法定监护人陪同下阅读）。当您在京东购物，进入结算页第一次选择快递到车服务，勾选并同意本协议后，即表示您已充分阅读、理解并接受本协议的全部内容，并与京东达成一致，成为使用快递到车服务的用户，本协议即构成您和京东之间的具有法律约束力的协议。阅读本协议的过程中，如果您不同意本协议或其中任何条款约定，请您停止勾选，如您停止勾选您仅可以阅读我们的信息和选择我们的其他服务但无法接受我们的快递到车服务。</p>
              <h3 class="mt20">服务内容</h3>    
              <p>2.1 用户可通过京东网站使用快递到车服务。</p>
              <p>2.2 用户理解并同意，京东有权根据适用法律法规及自身业务发展需要，单方面不提前通知用户的情况下暂停、变更、终止、限制所提供的本服务，且京东无须因此对用户负责。如因维护或升级的需要而暂停服务，京东将尽可能事先进行通告。</p>
              <p>2.3 除非本协议另有明确规定，快递到车服务任何功能的增加或强化，包括所推出的升级或更新版本，均受到本协议的规范。</p>
			  <h3 class="mt20">服务方式</h3>
              <p>3.1 为实现本服务，京东开发了用于用户下达快递到车服务、跟踪快递信息等功能。</p>
              <p>3.2 用户在申请使用本服务时，必须向汽车厂商或者汽车销售公司（“车企”）提供及时、详尽及准确的注册信息（包括但不限于用户名、密码、联系人、联系电话、地址等）。用户填写的信息应真实准确，如因用户信息填写错误等原因导致用户无法使用本服务，或者因注册信息不真实或更新不及时而引发任何问题，京东不承担任何责任；用户须根据需要维护并及时更新注册信息，使之始终保持最新、完整且准确。</p>
              <p>3.3 用户知悉并同意京东向用户提供快递到车服务。为实现快递到车服务，京东与车企合作，将车企系统接入京东网站，使京东能够通过京东网站将用户的订单信息推送至车企系统，并且该车企系统中有关该笔订单部分信息、物流跟踪信息等与京东订单跟踪同步，使用户能够通过京东或车企系统获取该信息。</p>
              <p>3.4 用户知悉并同意由京东向用户提供快递寄送服务。受限于车企及用户的事先同意，京东有权合理调整快递寄送服务适用的地区、寄送物品或其他条件。除非车企/用户与京东另有约定，京东与用户之间的快递服务关系同时适用京东对外公布的规则。用户同意接受京东东与车企就快递寄送服务条件和规则作出的合理调整。</p>
			  <p>3.5  京东可以选择是否通过京东网站将商品订单和运单信息告知用户，以便用户确认订单信息。</p>
			  <p>3.6  若用户就快递到车服务提出任何咨询或投诉，车企将先行接待和受理。若经车企合理判断认为需由京东处理该等咨询或投诉的，车企可将该等咨询或投诉转至京东妥善处理。若用户直接向京东提出咨询或投诉的，京东同样会予以处理。</p>
              <h3 class="mt20">服务费用</h3>    
              <p>4.1 京东有权在与车企协商一致的情况下，自行酌情决定向用户收取费用。具体收费标准将届时事先通知用户。</p>
              <h3 class="mt20">车辆授权及隐私政策</h3>
              <p>5.1 用户每次通过京东商城使用快递到车服务，即视为用户授予京东（及其合法授权的第三方，包括但不限于京东物流及其快递员）为提供本服务而所需的全部必要权限，包括但不限于开启用户绑定的汽车的尾门、远程鸣笛、远程亮灯等。</p>
              <p>5.2 为保障用户使用快递到车服务，车企可以在京东物流及其快递员提供服务过程中开启汽车上的监控装置，对服务过程进行远程记录，车企有权为本服务之目的收集、保留、接入、使用或以其他方式处分所记录的信息，用户确认并同意京东有权通过车企或用户获取该远程记录信息。</p>
              <p>5.3 用户确认并授权京东将用户的订单信息推送至车企系统，使用户能够通过京东或车企系统获取该信息。</p>
              <p>5.4 用户确认并同意，京东及其关联公司及前述公司的合作伙伴可以根据法律法规及《京东隐私政策》（“隐私政策”）（详见京东帮助中心的规定，采集、使用并处置用户不时同意提供的相关公司或个人信息，从而确保用户及京东能够适时并妥善地完成快递到车服务事宜，以及法律法规及隐私政策中规定的京东及其关联公司及前述公司的合作伙伴可以从事的其他事宜。</p>
              <h3 class="mt20">用户使用规则及限制</h3>    
              <p>6.1 用户确认并同意，京东承诺的寄送服务范围与京东官网公示的配送范围一致，如用户通过京东商城下达的订单超出京东物流配送范围，京东有权拒送。</p>
			  <p>6.2  京东物流快递员将根据用户提供的地址，通过车辆定位、详细地址、远程鸣笛、远程亮灯等多种方式自行找到车辆，无需打扰用户。</p>
			  <p>6.3  用户在使用本服务时，应自行妥善保管车辆内所有贵重物品，京东或车企在提供本服务过程中不对车辆及车辆内的任何物品承担任何保管责任。</p>
			  <p>6.4  用户在使用服务过程中，必须遵循以下原则：</p>
			  <p>6.4.1  遵守中国有关的法律和法规，不得为任何非法目的使用快递到车服务；</p>
			  <p>6.4.2  遵守所有与网络服务有关的网络协议、规定和程序；</p>
			  <p>6.4.3  用户不能以任何方式通过任何手段或设备来干扰或试图干扰快递到车服务的操作或使用，包括但不限于垃圾邮件、黑客以及上传计算机病毒或定时炸弹，或者任何其他方式；</p>
			  <p>6.4.4  不得以任何形式侵犯京东的权利和/或商业利益或作出任何不利于京东的行为；</p>
			  <p>6.4.5  不得以任何方式侵犯其他任何第三方的专利权、著作权、商标权、商业秘密等知识产权，或名誉权、肖像权、隐私权等人身权益或其他任何合法权益；</p>
			  <p>6.4.6  不得进行任何其他不利于京东及快递到车服务的行为，不得为其他任何非法目的而使用快递到车服务。</p>
			  <p>6.5  京东有权对用户使用本服务的情况进行审查和监督，如用户在使用服务时违反任何上述规定，京东或其授权人士有权要求用户改正或直接采取一切必要的措施（包括但不限于暂停或终止用户使用本服务的权利）以减轻用户的不当行为造成的影响。</p>
              <h3 class="mt20">赔偿</h3>
              <p>7.1 用户确认并同意，对于因以下原因或与之相关的任何和全部第三方索赔、诉讼、责任、损失、损害、判决、成本和费用（统称为“索赔”），用户需自行承担全部责任，并免除京东及其管理人员、代理和员工或者任何代表京东开展业务的其他方的任何责任和损失（包括合理律师费用）：(i) 在使用快递到车服务时，用户或者用户授权使用快递到车服务的任何人员未遵守或违反本协议中的任何条款，或者 (ii) 用户或者用户授权使用快递到车服务的任何人员违反了任何适用法律、法规或侵犯了第三方的权利。</p>
              <p>7.2 若因京东物流或其快递员原因导致托寄物、用户车辆或其他财物毁损、灭失，或导致用户遭受任何其他损失的，车企将根据适用法律和对外公布规则进行赔偿。车企可酌情决定是否代替京东先行向用户进行赔偿，若用户直接向京东提出咨询或投诉的，京东同样会予以处理。</p>
			  <h3 class="mt20">免责条款</h3>
              <p>8.1 京东快递到车服务是为提供本服务而开发且按现状向用户提供，并非为满足用户个人要求而开发。因此京东对快递到车服务不作以下任何担保或保证：(i) 与用户的硬件和/或软件兼容；(ii) 适合用户的要求或者满足任何特定的性能或功能；(iii) 始终可用、无中断、安全或者没有错误。京东明确声明，不以明示或默示及其他任何形式对车企系统所提供服务的及时性、安全性、准确性做出担保。</p>
              <p>8.2 除本协议另行书面约定外，下列原因造成京东无法提供快递到车服务或者影响快递到车服务效果的，京东不承担责任：</p>
			  <p>8.2.1 车辆自身原因导致影响服务效果，包括但不限于无法通过正常授权开启车辆尾门、车辆未按约定用途使用构成违约导致服务暂停或终止等；</p>
			  <p>8.2.2 用户原因影响服务效果，包括但不限于提供信息错误、变更或撤销订单或授权、存在违约行为导致服务暂停或终止等；</p>
			  <p>8.2.3 第三方原因影响服务效果，包括但不限于任何情况下由于第三方(如网络通讯服务运营商、电力供应商、快递公司)原因造成用户个人信息泄露或服务的无法使用；</p>
			  <p>8.2.4 意外事件或不可抗力，包括但不限于暴乱、恐怖袭击、战争、火灾、洪水、地震、政府行为、司法行政命令。</p>
              <h3 class="mt20">终止</h3>
              <p>9.1 本协议自用户阅读并勾选之日起生效，在用户使用快递入口服务的过程中持续有效，直至依据本协议终止。</p>
              <p>9.2 一旦本协议终止，用户使用本服务的权利即告终止。京东不因终止本协议对用户承担任何责任，包括终止用户的用户账户和删除用户的用户内容。</p>
          </div>

      </div>
      <div class="opts ac mt20" id="doKnow">
          <a href='javascript:closeDialog()' class="btn-1">知道了</a>
      </div>
    </div>
</script>

<script id="J_agreement_box2" type="text/temp">
  <div class="agreement-box">
      <div class="agreement-cont">
          
<div class="ui-scrollbar-main"> 
              <h3>快递到车服务用户协议</h3>  
              <p>请您在开始使用快递到车服务之前务必仔细阅读并理解以下服务条款（“本协议”）。</p>
			  <p>快递到车服务是由京东向汽车的所有权人及其授权使用人（“您”或“用户”）提供京东网站购买商品的快递配送到汽车的服务（“快递到车服务”或“本服务”）。</p>
              <h3 class="mt20">确认与接受</h3>
              <p>1.1京东在此特别提醒您认真阅读、充分理解本协议中各条款，包括免除或者限制配送责任的免责条款、限制用户权利的限制条款以及法律适用和争议解决条款。请您审慎阅读并选择接受或不接受本协议(未成年人应在法定监护人陪同下阅读）。当您在京东购物，进入结算页第一次选择快递到车服务，勾选并同意本协议后，即表示您已充分阅读、理解并接受本协议的全部内容，并与京东达成一致，成为使用快递到车服务的用户，本协议即构成您和京东之间的具有法律约束力的协议。阅读本协议的过程中，如果您不同意本协议或其中任何条款约定，请您停止勾选，如您停止勾选您仅可以阅读我们的信息和选择我们的其他服务但无法接受我们的快递到车服务。</p>
              <h3 class="mt20">服务内容</h3>    
              <p>2.1 用户可通过京东网站使用快递到车服务。</p>
              <p>2.2 用户理解并同意，京东有权根据适用法律法规及自身业务发展需要，单方面不提前通知用户的情况下暂停、变更、终止、限制所提供的本服务，且京东无须因此对用户负责。如因维护或升级的需要而暂停服务，京东将尽可能事先进行通告。</p>
              <p>2.3 除非本协议另有明确规定，快递到车服务任何功能的增加或强化，包括所推出的升级或更新版本，均受到本协议的规范。</p>
			  <h3 class="mt20">服务方式</h3>
              <p>3.1 为实现本服务，京东开发了用于用户下达快递到车服务、跟踪快递信息等功能。</p>
              <p>3.2 用户在申请使用本服务时，必须向汽车厂商或者汽车销售公司（“车企”）提供及时、详尽及准确的注册信息（包括但不限于用户名、密码、联系人、联系电话、地址等）。用户填写的信息应真实准确，如因用户信息填写错误等原因导致用户无法使用本服务，或者因注册信息不真实或更新不及时而引发任何问题，京东不承担任何责任；用户须根据需要维护并及时更新注册信息，使之始终保持最新、完整且准确。</p>
              <p>3.3 用户知悉并同意京东向用户提供快递到车服务。为实现快递到车服务，京东与车企合作，将车企系统接入京东网站，使京东能够通过京东网站将用户的订单信息推送至车企系统，并且该车企系统中有关该笔订单部分信息、物流跟踪信息等与京东订单跟踪同步，使用户能够通过京东或车企系统获取该信息。</p>
              <p>3.4 用户知悉并同意由京东向用户提供快递寄送服务。受限于车企及用户的事先同意，京东有权合理调整快递寄送服务适用的地区、寄送物品或其他条件。除非车企/用户与京东另有约定，京东与用户之间的快递服务关系同时适用京东对外公布的规则。用户同意接受京东东与车企就快递寄送服务条件和规则作出的合理调整。</p>
			  <p>3.5  京东可以选择是否通过京东网站将商品订单和运单信息告知用户，以便用户确认订单信息。</p>
			  <p>3.6  若用户就快递到车服务提出任何咨询或投诉，车企将先行接待和受理。若经车企合理判断认为需由京东处理该等咨询或投诉的，车企可将该等咨询或投诉转至京东妥善处理。若用户直接向京东提出咨询或投诉的，京东同样会予以处理。</p>
              <h3 class="mt20">服务费用</h3>    
              <p>4.1 京东有权在与车企协商一致的情况下，自行酌情决定向用户收取费用。具体收费标准将届时事先通知用户。</p>
              <h3 class="mt20">车辆授权及隐私政策</h3>
              <p>5.1 用户每次通过京东商城使用快递到车服务，即视为用户授予京东（及其合法授权的第三方，包括但不限于京东物流及其快递员）为提供本服务而所需的全部必要权限，包括但不限于开启用户绑定的汽车的尾门、远程鸣笛、远程亮灯等。</p>
              <p>5.2 为保障用户使用快递到车服务，车企可以在京东物流及其快递员提供服务过程中开启汽车上的监控装置，对服务过程进行远程记录，车企有权为本服务之目的收集、保留、接入、使用或以其他方式处分所记录的信息，用户确认并同意京东有权通过车企或用户获取该远程记录信息。</p>
              <p>5.3 用户确认并授权京东将用户的订单信息推送至车企系统，使用户能够通过京东或车企系统获取该信息。</p>
              <p>5.4 用户确认并同意，京东及其关联公司及前述公司的合作伙伴可以根据法律法规及《京东隐私政策》（“隐私政策”）（详见京东帮助中心的规定，采集、使用并处置用户不时同意提供的相关公司或个人信息，从而确保用户及京东能够适时并妥善地完成快递到车服务事宜，以及法律法规及隐私政策中规定的京东及其关联公司及前述公司的合作伙伴可以从事的其他事宜。</p>
              <h3 class="mt20">用户使用规则及限制</h3>    
              <p>6.1 用户确认并同意，京东承诺的寄送服务范围与京东官网公示的配送范围一致，如用户通过京东商城下达的订单超出京东物流配送范围，京东有权拒送。</p>
			  <p>6.2  京东物流快递员将根据用户提供的地址，通过车辆定位、详细地址、远程鸣笛、远程亮灯等多种方式自行找到车辆，无需打扰用户。</p>
			  <p>6.3  用户在使用本服务时，应自行妥善保管车辆内所有贵重物品，京东或车企在提供本服务过程中不对车辆及车辆内的任何物品承担任何保管责任。</p>
			  <p>6.4  用户在使用服务过程中，必须遵循以下原则：</p>
			  <p>6.4.1  遵守中国有关的法律和法规，不得为任何非法目的使用快递到车服务；</p>
			  <p>6.4.2  遵守所有与网络服务有关的网络协议、规定和程序；</p>
			  <p>6.4.3  用户不能以任何方式通过任何手段或设备来干扰或试图干扰快递到车服务的操作或使用，包括但不限于垃圾邮件、黑客以及上传计算机病毒或定时炸弹，或者任何其他方式；</p>
			  <p>6.4.4  不得以任何形式侵犯京东的权利和/或商业利益或作出任何不利于京东的行为；</p>
			  <p>6.4.5  不得以任何方式侵犯其他任何第三方的专利权、著作权、商标权、商业秘密等知识产权，或名誉权、肖像权、隐私权等人身权益或其他任何合法权益；</p>
			  <p>6.4.6  不得进行任何其他不利于京东及快递到车服务的行为，不得为其他任何非法目的而使用快递到车服务。</p>
			  <p>6.5  京东有权对用户使用本服务的情况进行审查和监督，如用户在使用服务时违反任何上述规定，京东或其授权人士有权要求用户改正或直接采取一切必要的措施（包括但不限于暂停或终止用户使用本服务的权利）以减轻用户的不当行为造成的影响。</p>
              <h3 class="mt20">赔偿</h3>
              <p>7.1 用户确认并同意，对于因以下原因或与之相关的任何和全部第三方索赔、诉讼、责任、损失、损害、判决、成本和费用（统称为“索赔”），用户需自行承担全部责任，并免除京东及其管理人员、代理和员工或者任何代表京东开展业务的其他方的任何责任和损失（包括合理律师费用）：(i) 在使用快递到车服务时，用户或者用户授权使用快递到车服务的任何人员未遵守或违反本协议中的任何条款，或者 (ii) 用户或者用户授权使用快递到车服务的任何人员违反了任何适用法律、法规或侵犯了第三方的权利。</p>
              <p>7.2 若因京东物流或其快递员原因导致托寄物、用户车辆或其他财物毁损、灭失，或导致用户遭受任何其他损失的，车企将根据适用法律和对外公布规则进行赔偿。车企可酌情决定是否代替京东先行向用户进行赔偿，若用户直接向京东提出咨询或投诉的，京东同样会予以处理。</p>
			  <h3 class="mt20">免责条款</h3>
              <p>8.1 京东快递到车服务是为提供本服务而开发且按现状向用户提供，并非为满足用户个人要求而开发。因此京东对快递到车服务不作以下任何担保或保证：(i) 与用户的硬件和/或软件兼容；(ii) 适合用户的要求或者满足任何特定的性能或功能；(iii) 始终可用、无中断、安全或者没有错误。京东明确声明，不以明示或默示及其他任何形式对车企系统所提供服务的及时性、安全性、准确性做出担保。</p>
              <p>8.2 除本协议另行书面约定外，下列原因造成京东无法提供快递到车服务或者影响快递到车服务效果的，京东不承担责任：</p>
			  <p>8.2.1 车辆自身原因导致影响服务效果，包括但不限于无法通过正常授权开启车辆尾门、车辆未按约定用途使用构成违约导致服务暂停或终止等；</p>
			  <p>8.2.2 用户原因影响服务效果，包括但不限于提供信息错误、变更或撤销订单或授权、存在违约行为导致服务暂停或终止等；</p>
			  <p>8.2.3 第三方原因影响服务效果，包括但不限于任何情况下由于第三方(如网络通讯服务运营商、电力供应商、快递公司)原因造成用户个人信息泄露或服务的无法使用；</p>
			  <p>8.2.4 意外事件或不可抗力，包括但不限于暴乱、恐怖袭击、战争、火灾、洪水、地震、政府行为、司法行政命令。</p>
              <h3 class="mt20">终止</h3>
              <p>9.1 本协议自用户阅读并勾选之日起生效，在用户使用快递入口服务的过程中持续有效，直至依据本协议终止。</p>
              <p>9.2 一旦本协议终止，用户使用本服务的权利即告终止。京东不因终止本协议对用户承担任何责任，包括终止用户的用户账户和删除用户的用户内容。</p>
          </div>

      </div>
	  <div class="opts ac mt20" id="dosubmit">
		  <a href='javascript:submit_Order(null,1)' class="btn-1">同意并提交订单</a>
		  <a href='javascript:closeDialog()' class="btn-9 ml10">取消</a>
      </div>
    </div>
</script>

<!---->
<script type="text/javascript">
    function secondHandWarm () {
        var id=$('#secondHandFlag').val();
        $('body').dialog({
            title:'二手商品购买提醒',
            width:940,
            height:240,
            type:'iframe',
            source:OrderAppConfig.DynamicDomain + "/consignee/obtainSecondHandWarmConfig.action?id="+id
        });
    }window.secondHandWarm=secondHandWarm;
</script>
<!---->
<script id="tooltip-box-hwjy-2018" type="text/temp">
    <div class="al">
        <p class="pl10"><i class="hwjy-tips-logo-2018"></i></p>
        <p class="mt20 ftx-08">包裹从商家配送至集运仓后，在"我的京东-我的集运"<strong>再次支付跨境运费</strong>后，由国际快递集团将包裹统一打包寄送，可省运费。</p>
    </div>
</script>
<!---->
<script id="J_hwbuy_agreementbox" type="text/temp">
  <div class="hwbuy-agreement-box">
      <div class="hwbuy-agreement-cont">
       
<h2 class="ac mb20 mt20">《海外集运服务协议》</h2>  
<p>本协议是您与京东网站（简称"本站"，网址：www.jd.com）所有者（以下简称为"京东"）之间就京东网站服务等相关事宜所订立的契约，请您仔细阅读本注册协议，您点击"同意并继续"按钮后，本协议即构成对双方有约束力的法律文件。</p>
<p>1.1本站的各项电子服务的所有权和运作权归京东所有。用户同意所有注册协议条款并完成注册程序，才能成为本站的正式用户。用户确认：本协议条款是处理双方权利义务的契约，始终有效，法律另有强制性规定或双方另有特别约定的，依其规定。</p>
<p>1.2用户点击同意本协议的，即视为用户确认自己具有享受本站服务、下单购物等相应的权利能力和行为能力，能够独立承担法律责任。</p>
<p>1.3如果您在18周岁以下，您只能在父母或监护人的监护参与下才能使用本站。</p>
<p>1.4京东保留在中华人民共和国大陆地区法施行之法律允许的范围内独自决定拒绝服务、关闭用户账户、清除或编辑内容或取消订单的权利。</p>
<p>本协议是您与京东网站（简称"本站"，网址：www.jd.com）所有者（以下简称为"京东"）之间就京东网站服务等相关事宜所订立的契约，请您仔细阅读本注册协议，您点击"同意并继续"按钮后，本协议即构成对双方有约束力的法律文件。</p>
<p>1.1本站的各项电子服务的所有权和运作权归京东所有。用户同意所有注册协议条款并完成注册程序，才能成为本站的正式用户。用户确认：本协议条款是处理双方权利义务的契约，始终有效，法律另有强制性规定或双方另有特别约定的，依其规定。</p>
<p>1.2用户点击同意本协议的，即视为用户确认自己具有享受本站服务、下单购物等相应的权利能力和行为能力，能够独立承担法律责任。</p>
<p>1.3如果您在18周岁以下，您只能在父母或监护人的监护参与下才能使用本站。</p>
<p>1.4京东保留在中华人民共和国大陆地区法施行之法律允许的范围内独自决定拒绝服务、关闭用户账户、清除或编辑内容或取消订单的权利。</p>
<p>本协议是您与京东网站（简称"本站"，网址：www.jd.com）所有者（以下简称为"京东"）之间就京东网站服务等相关事宜所订立的契约，请您仔细阅读本注册协议，您点击"同意并继续"按钮后，本协议即构成对双方有约束力的法律文件。</p>
<p>1.1本站的各项电子服务的所有权和运作权归京东所有。用户同意所有注册协议条款并完成注册程序，才能成为本站的正式用户。用户确认：本协议条款是处理双方权利义务的契约，始终有效，法律另有强制性规定或双方另有特别约定的，依其规定。</p>
<p>1.2用户点击同意本协议的，即视为用户确认自己具有享受本站服务、下单购物等相应的权利能力和行为能力，能够独立承担法律责任。</p>
<p>1.3如果您在18周岁以下，您只能在父母或监护人的监护参与下才能使用本站。</p>
<p>1.4京东保留在中华人民共和国大陆地区法施行之法律允许的范围内独自决定拒绝服务、关闭用户账户、清除或编辑内容或取消订单的权利。</p>

      </div>
      <div class="opts ac mt20 mb10">
          <a href="#none" class="btn-1">继续购买</a>
      </div>
    </div>
</script>
<script id="J_hwbuy_yc" type="text/temp">
  <div class="hwbuy-yc-box">
      <div class="ycskujy-cont">
      	移除商品成功
      </div>
      <div class="opts ac mt20 mb10">
          <a href="#none" class="btn-1">确定</a>
      </div>
    </div>
</script>
<script id="jxj-confirm-dialog" type="text/temp">
  <div class="jxj-confirm-box ac pt10">
      <div class="icon-box-new"><i class="m-icon confirm-icon-blue"></i></div>
      <h3>膨胀金不可用，继续结算？</h3>
      <p>您的订单中存在不可使用膨胀金的商品</p>
      <p>继续结算将不可使用膨胀金优惠</p>
      <div class="op-btns mt20">
          <a href="//cart.jd.com" class="btn-1 mr10">返回修改购物车</a>
          <a href="#none" class="btn-9">继续结算</a>
      </div>
  </div>
</script>
<script id="tooltip-box-hwsf" type="text/temp">
    <div class="al">
        <p class="ftx-08">澳洲税务局规定，自2018年7月1日起，由电商平台代收代缴入境澳洲低价值商品GST，GST=订单金额*10%(GST税率)。</p>
    </div>
</script>
<script id="e_card_list" type="text/temp">
 <ul>
    {{each giftCardList giftCard index}}
    <li>
        {{include 'e_card_item' giftCard}}
    </li>
    {{/each}}
</ul>
</script>
<script id="e_card_item" type="text/temp">
<div class="{{if showType == 2}}accesskey-item-new{{else}}giftcard-item-new {{/if}}">
    <div class="{{if  yn == 1}} g-detail{{else}} g-detail-disable {{/if}}  {{if selected}} item-selected {{/if}} " data-gift-id="{{id}}"  data-gift-key="{{key}}" data-page-no="{{pageNo}}">
        <div class="g-msg">
            <div class="item-selected-cancel hide">取消勾选</div>
            <div class="g-origin {{if cardBrand == 0 }} g-origin-red {{else}} g-origin-blue {{/if}}">
                <b></b>
                {{if showType == -1}}
                <span class="ml5" title="京品卡|{{cardBrandName}}">京品卡|{{cardBrandName}}</span>
                {{else if showType == 0}}
                <span class="ml5" title="京东卡">京东卡</span>
                {{else if showType == 1}}
                <span class="ml5" title="京东E卡">京东E卡</span>
                {{else if showType == 2}}
                <span class="ml5" title="京东领货码">京东领货码</span>
                {{/if}}
            </div>
            <div class="g-price">
                <em>余</em><strong>￥{{balance}}</strong>
            </div>
            <div class="g-limit">
                <span>面值：￥<em>{{amount}}</em></span>
            </div>
        </div>
        <div class="g-type">
            <span class="g-type-l">限自营商品<b></b></span>
            <span class="g-type-r"><em>|</em>有效期至{{timeEnd}}</span>
            <span class="g-type-tips hide"><b></b>{{ableDesc}}</span>
        </div>
    </div>
    <div class="g-info">
        {{if discountCurUsed > 0}}
            <strong class="ftx01">本次使用：￥{{discountCurUsed}}</strong>
         {{/if}}
        {{if  yn == 0}}
            <i class="g-info-qmark"></i>
            <span>{{disableDesc}}</span>
        {{/if}}
    </div>

</div>
</script>
<script id="e_card_add" type="text/temp">
<div>
    <span class="label">{{if type == 0}} 请输入礼品卡（京东卡&nbsp;/&nbsp;图书卡&nbsp;/&nbsp;京东E卡）密码：{{else}} 请输入领货码密码：{{/if}}</span>
    </div>
    <div class="form virtual-add-input">
        <input id="lpkKeyPressFirst" type="text" class="itxt" maxlength="4" onpaste="pasteCardPassWord(event,this)">
        <div class="c-gap"></div>
        <input id="lpkKeyPressSecond" type="text" class="itxt" maxlength="4" onpaste="pasteCardPassWord(event,this)">
        <div class="c-gap"></div>
        <input id="lpkKeyPressThird" type="text" class="itxt" maxlength="4" onpaste="pasteCardPassWord(event,this)">
        <div class="c-gap"></div>
        <input id="lpkKeyPressFourth" type="text" class="itxt" maxlength="4" onpaste="pasteCardPassWord(event,this)">
        <span class="tips-msg">密码只包含数字 0-9，大写字母 A-F</span>
        <span class="error-msg" style="display:none;">请输入密码</span>
    </div>
    <div class="clr"></div>
    {{if useAuthCode}}
    <div class="form mt5">
        <p>请输入验证码 </p>
        <input id="authCode" type="text" class="itxt itxt-long mt10" maxlength="10">
        <img class="idcode-img mt10 ml10 fl" src="https://authcode.jd.com/authcode?a=1&amp;acid=9326911e-5aba-4df9-8f61-f7e2af2f0d54&amp;srcid=trackWeb">
        <div class="idcode-change-btn ml10 mt10 fl">看不清换一张</div>
        <span id="gift_tips"><span class="tips-msg mt10">请输入验证码</span></span>
        <div class="idcode-loading ml10 mt10" style="display: none"><b></b>加载中...</div>
    </div>
   {{/if}}
    <div class="clr"></div>
    <div class="mt10 mb5">
        <input type="button" class="btn-add btn-4 btn-add-new" {{if type == 0 }} id="giftCardBtn" {{else}}id="accesskeyBtn"{{/if}} value="添加并使用">
</div>
</script>
<script id="J_common-risk-control-dialog" type="text/temp">
<div class="common-tips-dialog ac risk-control-dialog">
  <p class="common-tips-tit">请输入手机验证码认证</p>
  <p class="common-tips-cont">当前手机号{{mobile}}</p>
  <div class="rc-input-cont">
    <input class="rc-input" type="search" placeholder="请输入手机验证码" maxlength="6">
    <div class="rc-extra" id="accountCode" ><i class="mail-icon"></i>获取短信验证码</div>
  </div>
  <div class="rc-input-tip al hide"><i class="succ"></i>验证码已发送至您的手机，有效期2分钟</div>
  <p class="mt15"><p>
  <p class="common-tips-opts">
    <a href="#none" class="comon-tips-btn yes rc-btn disable">提交认证</a>
  </p>
  <input type="hidden" value="{{param}}"/>
</div>
</script>
<script id="J_common-tips-error-dialog" type="text/temp">
<div class="common-tips-dialog ac">
  <div class="common-tips-icon-cont"><i class="common-tips-icon error" /></div>
  <p class="common-tips-tit">{{title}}</p>
  {{if subtitle }}
    <p class="common-tips-cont">{{subtitle}}</p>
  {{/if}}
  {{if context}}
    <p class="common-tips-cont">{{context}}</p>
  {{/if}}
  <p class="common-tips-opts mt15">
    <a href="#none" class="comon-tips-btn yes">确定</a>
  </p>
</div>
</script>
		<!--footer start-->
<div id="footer-2017">
	<div class="w">
		<div class="copyright_links">
			<p>
				<a href="//about.jd.com" target="_blank">关于我们</a><span class="copyright_split">|</span>
				<a href="//about.jd.com/contact/" target="_blank">联系我们</a><span class="copyright_split">|</span>
				<a href="//help.jd.com/user/custom.html" target="_blank">联系客服</a><span class="copyright_split">|</span>
				<a href="//vc.jd.com/cooperation.html" target="_blank">合作招商</a><span class="copyright_split">|</span>
				<a href="//helpcenter.jd.com/venderportal/index.html" target="_blank">商家帮助</a><span class="copyright_split">|</span>
				<a href="//jzt.jd.com" target="_blank">营销中心</a><span class="copyright_split">|</span>
				<a href="//app.jd.com/" target="_blank">手机京东</a><span class="copyright_split">|</span>
				<a href="//club.jd.com/links.aspx" target="_blank">友情链接</a><span class="copyright_split">|</span>
				<a href="//media.jd.com/" target="_blank">销售联盟</a><span class="copyright_split">|</span>
				<a href="//club.jd.com/" target="_blank">京东社区</a><span class="copyright_split">|</span>
				<a href="//sale.jd.com/act/FTrWPesiDhXt5M6.html" target="_blank">风险监测</a><span class="copyright_split">|</span>
				<a href="//about.jd.com/privacy/" target="_blank">隐私政策</a><span class="copyright_split">|</span>
				<a href="//gongyi.jd.com" target="_blank">京东公益</a><span class="copyright_split">|</span>
				<a href="//en.jd.com/" target="_blank">English Site</a><span class="copyright_split">|</span>
				<a href="//corporate.jd.com/" target="_blank">Media & IR</a>
			</p>
		</div>
		<div class="copyright_info">
			<p>
				<a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000088" target="_blank">京公网安备 11000002000088号</a><span class="copyright_split">|</span><span>京ICP证070359号</span><span class="copyright_split">|</span>
				<a href="//img14.360buyimg.com/da/jfs/t256/349/769670066/270505/3b03e0bb/53f16c24N7c04d9e9.jpg" target="_blank">互联网药品信息服务资格证编号(京)-经营性-2014-0008</a><span class="copyright_split">|</span><span>新出发京零 字第大120007号</span></p>
			<p><span>互联网出版许可证编号新出网证(京)字150号</span><span class="copyright_split">|</span>
				<a href="//sale.jd.com/act/pQua7zovWdJfcIn.html" target="_blank">出版物经营许可证</a><span class="copyright_split">|</span>
				<a href="//misc.360buyimg.com/wz/wlwhjyxkz.jpg" target="_blank">网络文化经营许可证京网文[2014]2148-348号</a><span class="copyright_split">|</span><span>违法和不良信息举报电话：4006561155</span></p>
			<p><span class="copyright_text">Copyright &copy; 2004 - <em id="copyright_year">2018</em>  京东JD.com 版权所有</span><span class="copyright_split">|</span><span>消费者维权热线：4006067733</span>
				<a href="//sale.jd.com/act/7Y0Rp81MwQqc.html" target="_blank" class="copyright_license">经营证照</a>
				<span class="copyright_split">|</span>
				<span>(京)网械平台备字(2018)第00003号</span>
				<span class="copyright_split">|</span>
				<a href="//storage.jd.com/imgtools/cbdaa22553-dccaf290-d1af-11e8-a840-89f99f5f0056.jpeg" target="_blank" class="mod_business_license">营业执照</a>
			</p>
			<p class="mod_copyright_inter">
				<a class="mod_copyright_inter_lk" href="//www.joybuy.com/?source=1&visitor_from=3" target="_blank" clstag="h|keycount|btm|btmnavi_null0501"><i class="mod_copyright_inter_ico mod_copyright_inter_ico_global"></i><span class="languagefont">&#xe901;</span></a>
				<span class="copyright_split">|</span>
				<a class="mod_copyright_inter_lk" href="//www.jd.ru/?source=1&visitor_from=3" target="_blank" clstag="h|keycount|btm|btmnavi_null0502"><i class="mod_copyright_inter_ico mod_copyright_inter_ico_rissia"></i><span class="languagefont">&#xe904;</span></a>
				<span class="copyright_split">|</span>
				<a class="mod_copyright_inter_lk" href="//www.jd.id/?source=1&visitor_from=3" target="_blank" clstag="h|keycount|btm|btmnavi_null0503"><i class="mod_copyright_inter_ico mod_copyright_inter_ico_indonesia"></i><span class="languagefont">&#xe902;</span></a>
				<span class="copyright_split">|</span>
				<a class="mod_copyright_inter_lk" href="//www.joybuy.es/?source=1&visitor_from=3" target="_blank" clstag="h|keycount|btm|btmnavi_null0504"><i class="mod_copyright_inter_ico mod_copyright_inter_ico_spain"></i><span class="languagefont">&#xe903;</span></a>
				<span class="copyright_split">|</span>
				<a class="mod_copyright_inter_lk" href="//www.jd.co.th/?source=1&visitor_from=3" target="_blank" clstag="h|keycount|btm|btmnavi_null0505"><i class="mod_copyright_inter_ico mod_copyright_inter_ico_thailand"></i><span class="languagefont">&#xe900;</span></a>
			</p>
			<p><span>京东旗下网站：</span>
				<a href="https://www.jdpay.com/" target="_blank">京东钱包</a><span class="copyright_split">|</span>
				<a href="http://www.jcloud.com" target="_blank">京东云</a>
			</p>
		</div>
		<p class="copyright_auth">
			<script type="text/JavaScript">function CNNIC_change(eleId){var str= document.getElementById(eleId).href;var str1 =str.substring(0,(str.length-6));str1+=CNNIC_RndNum(6);
				document.getElementById(eleId).href=str1;}function CNNIC_RndNum(k){var rnd=""; for (var i=0;i
				< k;i++) rnd+=Math.floor(Math.random()*10); return rnd;};(function(){var d=new Date;document.getElementById(
				 "copyright_year").innerHTML=d.getFullYear()})();</script>
					<a id="urlknet" class="copyright_auth_ico copyright_auth_ico_2" onclick="CNNIC_change('urlknet')" oncontextmenu="return false;"
					 name="CNNIC_seal" href="https://ss.knet.cn/verifyseal.dll?sn=2008070300100000031&ct=df&pa=294005" target="_blank">可信网站信用评估</a>
					<a class="copyright_auth_ico copyright_auth_ico_3" href="http://www.cyberpolice.cn/" target="_blank">网络警察提醒你</a>
					<a class="copyright_auth_ico copyright_auth_ico_4" href="https://search.szfw.org/cert/l/CX20120111001803001836" target="_blank">诚信网站</a>
					<a class="copyright_auth_ico copyright_auth_ico_5" href="http://www.12377.cn" target="_blank">中国互联网举报中心</a>
					<a class="copyright_auth_ico copyright_auth_ico_6" href="http://www.12377.cn/node_548446.htm" target="_blank">网络举报APP下载</a>
		</p>
	</div>
</div>
<!--footer end-->

<!-- footer end -->
	<script type="text/javascript" src="//trade.jd.com/shopping/misc/js/json2.js?r=2016112803091"></script>
	<script type="text/javascript" src="//trade.jd.com/shopping/misc/js/payAndShipment.js?r=2018102703091"></script>
	<script type="text/javascript" src="//trade.jd.com/shopping/misc/js/order_virtual.js?r=2018101103091"></script>
	<script type="text/javascript" src="//trade.jd.com/shopping/misc/js/order.js?r=2018121203091"></script>
	<script type="text/javascript" src="//trade.jd.com//shopping/misc/js/jdpay.js?r=2016112803091"></script>
	<script type="text/javascript" id="tak_trv" src="//tak.jd.com/a/tr.js?biz=ONG2NYPNNZ67"></script>
<script type="text/javascript"  src="//trade.jd.com/static/js/lib/other/class.mini.js" ></script>
<script type="text/javascript"  src="//trade.jd.com/static/js/modules/order/order.mini.js" ></script>
<!--art-template compatible -->
<script type="text/javascript" src="//trade.jd.com/static/js/lib/other/ie-compatible/es5-shim.min.js"></script>
<script type="text/javascript" src="//trade.jd.com/static/js/lib/other/ie-compatible/es5-sham.min.js"></script>
<script type="text/javascript" src="//trade.jd.com/static/js/lib/other/ie-compatible/json3.min.js"></script>
<script type="text/javascript" src="//trade.jd.com/static/js/lib/other/template-web.js"></script>
<script type="text/javascript"  src="//trade.jd.com/static/js/modules/virtual/virtual.mini.js" ></script>
<script type="text/javascript">
    window.orderApi = new trade.order.api({'time':60 });
</script>
<script type="text/javascript">
    $('.giftcard-tab-panel-main').delegate('.g-type-l', 'mouseenter', function(event) {
        $(this).siblings('.g-type-tips').removeClass('hide');
    });
    $('.giftcard-tab-panel-main').delegate('.g-type-l', 'mouseleave', function(event) {
        $(this).siblings('.g-type-tips').addClass('hide');
    });
    $('.accesskey-tab-panel-main').delegate('.g-type-l', 'mouseenter', function(event) {
        $(this).siblings('.g-type-tips').removeClass('hide');
    });
    $('.accesskey-tab-panel-main').delegate('.g-type-l', 'mouseleave', function(event) {
        $(this).siblings('.g-type-tips').addClass('hide');
    });
    window.virtual = new trade.virtual({});
</script>
<script type="text/javascript"  src="//trade.jd.com/static/js/modules/virtual/giftCard.mini.js"></script>
<script type="text/javascript">
    window.virtualGiftCard = new trade.virtual.giftCard({'useAuthCode':true,'pagesize':100,'virtual':window.virtual});
</script>


<script type="text/javascript"  src="//trade.jd.com/static/js/modules/virtual/balance.mini.js"></script>
<script type="text/javascript">
    window.virtualBalance = new trade.virtual.balance({'virtual':window.virtual});
</script>

<!-- 不降级  -->
<script src="//payrisk.jd.com/js/td.js"></script>


	<!--/ /widget/footer-2015/footer-2015.tpl -->
	<script type="text/javascript">
	//<![CDATA[
	var couponToggle = (function(){
		var obj = $('[data-bind="coupon"]'),
			tObj = obj.find(".item");

		var init = function(){
			tObj.each(function(){
				var that = $(this);
				var toggler = $(this).find(".toggler");
				var toggled = false;

				toggler.bind("click", function(e){
					e.preventDefault();
					toggled = !toggled;

					toggler.parent().parent()[toggled ? "addClass" : "removeClass"]("toggle-active");

					that.find(".toggle-wrap")[toggled ? "removeClass" : "addClass"]("hide").css("display", toggled ? "block" : "none");
				});
			});
		};

		return {
			init: init
		};
	})();


	var invoiceMore = (function(){
		var expandHolder = $("#invoice-list"),
			expandHandle = $("#invoice-more-btn"),
			item = expandHolder.find(".item-fore");
			expand = false;

		var init = function(){
			expandHandle.bind("click", function(){
				expand = !expand;

				item[expand ? "removeClass" : "addClass"]("hide").css("display", expand ? "block" : "none");


				expandHandle.removeClass(expand ? "select-expand" : "select-collapse").addClass(expand ? "select-collapse" : "select-expand").find("span").html(expand ? "\u6536\u8D77" : "\u66F4\u591A\u5E38\u7528\u5730\u5740");

				if(expand) {

				} else {

				}
			});
		};

		return {
			init: init
		};
	})();
	$(function(){
		$("input.textbox").focus(function(){
			$(this).addClass("focus");
		}).blur(function(){
			$(this).removeClass("focus");
		});

		couponToggle.init();

		invoiceMore.init();

		$(".step-action a").bind("click", function(){
			$("#step-3").expose();
		});
	});
	//]]>
	//统计js	
    (function() {
        var ja = document.createElement('script');
        ja.type = 'text/javascript';
        ja.async = true;
        ja.src = ('https:' == document.location.protocol ? 'https://wlssl' : 'http://wl') + '.jd.com/wl.js';
		        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ja, s);
    })();

	
	//防止窗口变换，弹窗错位
	$(window).resize(function(){
           var obj=$("#freightSpan");	
           if($("#transport").html()!=null){
	           $("#transport").css({
					position:"absolute",
					top:obj.offset().top+"px",
					left:(obj.offset().left-345)+"px"
	           })
           }
	});
	</script>
	</body>
</html>

Process finished with exit code 0

"""
soup = BeautifulSoup(html,'html5lib')

s = soup.find(attrs={'id':'eid'})
print(s.get('value'))



