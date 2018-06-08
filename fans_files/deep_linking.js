function getDeepLinkURLScheme(){var e={sg:{K_URL:"shopeesg://"},my:{K_URL:"shopeemy://"},th:{K_URL:"shopeeth://"},vn:{K_URL:"shopeevn://"},ph:{K_URL:"shopeeph://"},tw:{K_URL:"shopeetw://"},ir:{K_URL:"shopeeir://"},hk:{K_URL:"shopeeintl://"},mm:{K_URL:"shopeemm://"},id:{K_URL:"shopeeid://"}},t=e[LOCALE.toLowerCase()],o=t.K_URL;return o}function FB_fix(e){if(navigator.userAgent.indexOf("FBAV/")!==-1||1==e){$(".lure-hold .get_app_btns_wrapper").hide();var t="<div>"+i18n.t("msg_facebook_please_copy_link")+"</div>",o=$("<dl id='deeplink-copy'>"),r=$("<dd>").css({"-webkit-user-select":"all","-moz-user-select":"all","user-select":"all"}),a=$("<p>").css({"-webkit-user-select":"all","-moz-user-select":"all","user-select":"all"});o.css({"-webkit-user-select":"all","-moz-user-select":"all","user-select":"all",padding:"4px 0",color:"#ff5722"});var n=location.host.replace("mall.","");return n.indexOf("shopee.")==-1&&(n="test.shopee.sg"),"undefined"==typeof itemid?a.text("http://"+n+"/"+username):a.text("http://"+n+"/"+username+"/"+itemid),r.append(a).appendTo(o),showProm(t+o[0].outerHTML,!0),!0}return!1}function openApp(e,t){function o(){var e=isIOS()?3e3:500;alert_message_with_loader("",e),setTimeout(function(){t()},e)}function r(e){e.close(),e.window&&setTimeout(function(){r(e)},50)}var a=getDeepLinkURLScheme(),n=a+e;if(isIOS()){window.location=n;var i=+new Date,l=setInterval(function(){var e=+new Date;e-i>2e3&&hideProm(),e-i>1500&&clearInterval(l)},100),c=setTimeout(function(){if(document.hasFocus()){if(FB_fix())return;o()}},500);$(window).on("blur",function(){clearTimeout(c),hideProm()})}else if(isAndroid()){if(isGasApp())return void t();var s=!1,d=navigator.userAgent;if(s=d.indexOf("Chrome/4")>=0||d.indexOf("MiuiBrowser/")>=0)return window.location=n,void o();var p=window.open(n);TIMEOUT=500,navigator.userAgent.indexOf("SM-G130H")>=0&&(TIMEOUT=1e3),navigator.userAgent.indexOf("XiaoMi")>=0&&(TIMEOUT=800),setTimeout(function(){p&&p.window&&r(p),o()},TIMEOUT)}else t()}function addBiDataToUrl(e,t){return window._bi_addGSrcToUrl?_bi_addGSrcToUrl(e,location.pathname+location.search,t):e}function constructCollectionPageUrlJson(e,t){if(e.collectionId){var o=window.location,r=o.protocol+"//"+o.host+"/collections/"+e.collectionId+"/",a={url:t?addBiDataToUrl(r):r};return{webNav:a}}return null}function constructCategoriesPageUrlJson(e){if(e.categoryId&&e.categoryName){var t=location.origin+"/categories/"+e.categoryId+"/",o={url:t,navbar:{title:e.categoryName,searchParam:e.categoryId,searchType:1,searchPlaceholder:i18n.t("label_search_within")+": "+e.categoryName,rightItemsConfig:{items:[{type:"search"}]}}};return{webNav:o}}return!1}function constructCategoryPageUrlJson(e){if(e.categoryId&&e.categoryName){var t=window.location,o=t.protocol+"//"+t.host+"/category-item/?categoryid="+e.categoryId+"&categoryname="+encodeURIComponent(e.categoryName),r={url:o,tabRightButton:{type:"button",key:"filter",iconType:"filter"},navbar:{title:e.categoryName,searchParam:e.categoryId,searchPlaceholder:i18n.t("label_search_within")+": "+e.categoryName,rightItemsConfig:{items:[{type:"search"},{type:"button",key:"filter",iconType:"filter"}]}}};return{webNav:r}}return!1}function constructShopPageUrlJson(e){if(e.userId&&e.username&&e.shopId){var t=window.location,o=t.protocol+"//"+t.host+"/shop/#shopid="+e.shopId,r={url:addBiDataToUrl(o),navbar:{rightItemsConfig:{items:[{type:"more",items:[{type:"home"},{type:"reportuser",userID:e.userId}]}]}}};return{webNav:r}}return null}function constructItemPageUrlJson(e){if(e.itemId&&e.shopId){var t=window.location,o=t.protocol+"//"+t.host+"/item/#shopid="+e.shopId+"&itemid="+e.itemId,r={url:addBiDataToUrl(o),config:{},navbar:{rightItemsConfig:{items:[{type:"more",items:[{type:"home"},{type:"reportitem",itemID:e.itemId,shopID:e.shopId}]}]}}};return{webNav:r}}return!1}function encodeDeepLinkUrl(e){if(window.Base64){var t=JSON.stringify(e);return encodeURIComponent(Base64.encode(t))}return null}function constructGenericPageUrlJson(e){var t={url:wrapUrlWithBridgeCMDNavigate(addBiDataToUrl(e,!0))};return encodeDeepLinkUrl({paths:[{webNav:t}]})}function updateDeepLinkMeta(e){var t=get_app_ids(),o=get_app_agent(),r=t[LOCALE][o];if(e||(e="home","/"!=location.pathname&&(e+="?navRoute="+constructGenericPageUrlJson(location.href))),isIOS()){$("meta[name=apple-itunes-app]").remove();var a=", app-argument="+getDeepLinkURLScheme()+e;$("head").append('<meta name="apple-itunes-app" content="app-id=${APPID} ${APPARG}">'.replace("${APPID}",r).replace("${APPARG}",a))}}function _simple_nav_(e){function t(e){if(e){var t=e.split("|");e={};for(var o=0;o<t.length;o++){var r=t[o].split("=")[0],a=t[o].split("=")[1];e[r]=a}return e}return null}if(window.WebViewJavascriptBridge){var o=window.WebViewJavascriptBridge,e=t(e),r=e.s,a=e.i,n=e.ca,i=e.co;if(r&&a){var l={url:location.origin+"/item/#shopid="+r+"&itemid="+a};if(n){var c=$("div[categoryid='{{categoryId}}']".replace("{{categoryId}}",n)),s="placeholder";0!=c.length&&(s=c.text());var d=constructCategoryPageUrlJson({categoryId:n,categoryName:s}),p=constructItemPageUrlJson({itemId:a,shopId:r}),u={paths:[d,p]},g="home?navRoute="+encodeDeepLinkUrl(u);o.callHandler("jump",{path:g},function(){})}else if(i){var m=constructCollectionPageUrlJson({collectionId:i},!1),p=constructItemPageUrlJson({itemId:a,shopId:r}),u={paths:[m,p]},g="home?navRoute="+encodeDeepLinkUrl(u);o.callHandler("jump",{path:g},function(){})}else bridgeCallHandler("navigate",l,function(){})}else if(n){var c=$("div[categoryid='{{categoryId}}']".replace("{{categoryId}}",n)),s="placeholder";0!=c.length&&(s=c.text());var l=constructCategoryPageUrlJson({categoryId:n,categoryName:s}).webNav;bridgeCallHandler("navigate",l,function(){})}else if(i){var l=constructCollectionPageUrlJson({collectionId:i},!0).webNav;bridgeCallHandler("navigate",l,function(){})}}else console.log("simple nav failed, bridge is not ready")}$(function(){updateDeepLinkMeta(null)});
//# sourceMappingURL=../../source_maps/common/deep_linking.js.map
