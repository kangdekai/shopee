var AppHeaderController=function(n,e){function t(n){r.init(n),i(r)}function i(n){n.on(n.Targets.USER_AVATAR,n.Events.TAP,function(){e.globalVersionFallback(function(){r.isLoggedIn()?e.navigate("/me/"):showSecond()},function(){showSecond()})}),n.on(n.Targets.IC_FILTER,n.Events.TAP,function(){BJBridgeReceiver.triggerBridgeEvent("onEventCallback",{key:"filter"})})}var r=function(n){function e(n){u=n,t(u)}function t(e){f=new n,i(f,e),r(f)}function i(n,e){l=e.find(".user_avatar"),n.registerTarget(g.USER_AVATAR,l),$filter=e.find(".ic_filter_pc"),n.registerTarget(g.IC_FILTER,$filter)}function r(n){n.registerEventTrigger(g.USER_AVATAR,c.TAP),n.registerEventTrigger(g.IC_FILTER,c.TAP)}function o(n,e,t){f.on(n,e,t)}function a(){return!!l.data("logged-in")}var g={USER_AVATAR:"user_avatar",IC_FILTER:"ic_filter_pc"},c={TAP:"tap"},u=null,l=null,f=null;return{init:e,Targets:g,Events:c,on:o,isLoggedIn:a}}(n);return{init:t}}(MultiTargetEventDispatcher,BJUtil);
//# sourceMappingURL=../../source_maps/common/app_header_controller.js.map
