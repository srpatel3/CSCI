(window.webpackJsonp=window.webpackJsonp||[]).push([[131],{"2C5c":function(e,t,a){},"4ycz":function(e,t,a){"use strict";var n=a("Yz+Y"),r=a.n(n),s=a("iCc5"),o=a.n(s),i=a("V7oC"),l=a.n(i),c=a("FYw3"),u=a.n(c),d=a("mRg0"),p=a.n(d),m=a("cDcd"),g=a.n(m),h=a("17x9"),f=a.n(h),v=a("TSYQ"),b=a.n(v),E=a("2VWb"),y=a("OJx6"),k=a.n(y),C=a("wuQx"),S=a.n(C),w=a("mFgg"),P=a("x/Cr"),N=a("tVtT"),_=(a("bQ39"),a("eOGF")),T=function(e){function t(){o()(this,t);var e=u()(this,(t.__proto__||r()(t)).call(this));return e.onModalClose=function(){var t=e.props,a=t.onClose,n=t.analyticsKey,r=t.analyticsAttribute;t.allowClose&&(n&&k.a.track("Click",n+"Close",r),a())},e.state={windowWidth:1280,windowHeight:768},e}return p()(t,e),l()(t,[{key:"componentDidMount",value:function(){this.calculateWindowSize(),this.trackModalViewed()}},{key:"componentWillReceiveProps",value:function(){this.calculateWindowSize()}},{key:"trackModalViewed",value:function(){var e=this.props.badge,t=e.analyticsKey,a=e.analyticsAttribute;t&&k.a.track("Viewed",t,a)}},{key:"calculateWindowSize",value:function(){this.setState({windowWidth:window.innerWidth,windowHeight:window.innerHeight})}},{key:"badgeSocialShare",value:function(){var e=this.props.badge;return g.a.createElement("div",{className:"badge-share-modal"},g.a.createElement(N.a,{badge:e,align:"center",page:"badge_share"}))}},{key:"renderBadgeContent",value:function(){var e=this.props,t=e.badge,a=e.button,n=e.title,r=e.message,s=e.badgeShare,o=this.state,i=o.windowWidth,l=o.windowHeight,c=P.b[P.c[t.level]||"bronze"].confetti;return g.a.createElement("div",{className:"modal-content"},g.a.createElement(w.a,{badge:t}),g.a.createElement("div",{className:"progress-title"},n),g.a.createElement("div",{className:"progress-message"},r),a,s&&this.badgeSocialShare(),g.a.createElement(S.a,{colors:c,shapes:["rectangle"],width:i,height:l,className:"confetti"}))}},{key:"render",value:function(){var e=this.props,t=e.open,a=e.allowClose,n=e.modalClass;return g.a.createElement(E.a,{open:t,onClose:this.onModalClose,modalClass:b()("badge-confetti-modal",n)},a&&g.a.createElement("div",{className:"icon2-close close",onClick:this.onModalClose}),g.a.createElement("div",{className:"status-wrap"},this.renderBadgeContent()))}}]),t}(m.PureComponent);T.propTypes={badge:f.a.object.isRequired,open:f.a.bool.isRequired,onClose:f.a.func.isRequired,title:f.a.string,message:f.a.oneOfType([f.a.string,f.a.element]).isRequired,button:f.a.element,analyticsKey:f.a.string,analyticsAttribute:f.a.object,allowClose:f.a.bool,modalClass:f.a.string,badgeShare:f.a.bool},T.defaultProps={onClose:_.F,title:"Congrats!",allowClose:!0},t.a=T},"6mHp":function(e,t,a){"use strict";var n=a("QbLZ"),r=a.n(n),s=a("Yz+Y"),o=a.n(s),i=a("iCc5"),l=a.n(i),c=a("V7oC"),u=a.n(c),d=a("FYw3"),p=a.n(d),m=a("mRg0"),g=a.n(m),h=a("cDcd"),f=a.n(h),v=a("17x9"),b=a.n(v),E=(a("TSYQ"),a("p0DI")),y=function(e){function t(){l()(this,t);var e=p()(this,(t.__proto__||o()(t)).call(this));return e.loaderId="hr-loader-"+Math.ceil(1e7*Math.random()),e.animationDuration=1,e.totalParts=9,e}return g()(t,e),u()(t,[{key:"renderAnimationTag",value:function(e){var t=this.props,a=t.color,n=t.loadingColor,r=this.animationDuration,s=r/3,o=this.loaderId+"-"+e,i=r/this.totalParts*(this.totalParts-e);return f.a.createElement("animate",{attributeName:"fill",from:n,to:a,id:o,dur:s+"s",begin:i+"s;"+o+".end+"+.6666*r+"s"})}},{key:"render",value:function(){var e=this.props,t=e.diameter,a=e.color,n=r()({},e);return["diameter","color","loadingColor"].forEach(function(e){delete n[e]}),f.a.createElement(E.a,null,f.a.createElement("svg",r()({version:"1.1",id:"Layer_1",xmlns:"http://www.w3.org/2000/svg",x:"0px",y:"0px",width:t+"px",height:t+"px",viewBox:"0 0 1100 1100"},n),f.a.createElement("g",null,f.a.createElement("path",{d:"M382.662,164.463c-10.904,0-114.259,98.957-106.185,107.011c8.012,8.033,202.659,8.033,210.629,0 C495.151,263.42,393.593,164.463,382.662,164.463z",fill:a}),f.a.createElement("path",{d:"M724.819,929.33c-11.007,0-114.606-99.256-106.562-107.328c8.042-8.072,203.238-8.072,211.297,0 C837.683,830.074,735.786,929.33,724.819,929.33z",fill:a}),f.a.createElement("line",{fill:"none",stroke:a,strokeWidth:"140",strokeMiterlimit:"8",x1:"431.362",y1:"548.118",x2:"696.214",y2:"548.467"}),f.a.createElement("line",{fill:"none",stroke:a,strokeWidth:"140",strokeMiterlimit:"8",x1:"723.914",y1:"332.673",x2:"723.914",y2:"842.504"}),f.a.createElement("line",{fill:"none",stroke:a,strokeWidth:"140",strokeMiterlimit:"8",x1:"381.794",y1:"239.607",x2:"381.794",y2:"761.195"})),f.a.createElement("path",{d:"M1013.021,546.036c0.001,0.287,0.001,0.573,0.001,0.861c-0.002,45.46-6.576,89.267-18.808,130.652 c-12.233,41.379-30.134,80.332-52.821,115.977l67.489,42.957c26.628-41.836,47.67-87.611,62.05-136.254 c14.381-48.639,22.092-100.145,22.09-153.332c0-0.336,0-0.672-0.001-1.008L1013.021,546.036z",fill:a},this.renderAnimationTag(1)),f.a.createElement("path",{d:"M904.944,250.653c27.515,32.649,50.56,69.167,68.201,108.6c17.642,39.436,29.885,81.781,35.81,126.175l79.297-10.58 c-6.953-52.12-21.353-101.935-42.082-148.265c-20.729-46.334-47.781-89.19-80.051-127.483L904.944,250.653z",fill:a},this.renderAnimationTag(2)),f.a.createElement("path",{d:"M632.321,93.7c43.962,7.635,85.753,21.502,124.488,40.676c38.731,19.173,74.4,43.658,106.037,72.503l53.9-59.116 c-37.103-33.828-78.947-62.559-124.446-85.083c-45.495-22.523-94.65-38.834-146.292-47.801L632.321,93.7z",fill:a},this.renderAnimationTag(3)),f.a.createElement("path",{d:"M322.559,148.697c33.884-19.656,70.484-35.1,109.11-45.635c38.628-10.533,79.281-16.164,121.353-16.166 c6.342,0,12.65,0.128,18.926,0.382l3.229-79.935c-7.351-0.297-14.736-0.447-22.155-0.447c-49.221-0.001-97.003,6.601-142.403,18.985 c-45.402,12.382-88.423,30.539-128.204,53.617L322.559,148.697z",fill:a},this.renderAnimationTag(4)),f.a.createElement("path",{d:"M120.489,389.924c30.023-82.728,83.202-154.506,151.696-207.38l-48.888-63.325C142.968,181.24,80.603,265.367,45.29,362.627 L120.489,389.924z",fill:a},this.renderAnimationTag(5)),f.a.createElement("path",{d:"M120.751,704.592c-17.934-49.16-27.726-102.199-27.729-157.695c0-33.914,3.661-66.905,10.596-98.658l-78.157-17.073 c-8.151,37.312-12.44,76.054-12.439,115.731c-0.004,64.933,11.492,127.349,32.577,185.119L120.751,704.592z",fill:a},this.renderAnimationTag(6)),f.a.createElement("path",{d:"M323.241,945.492c-75.442-43.586-137.431-108.066-177.952-185.41l-70.86,37.131 c47.609,90.838,120.217,166.359,208.787,217.545L323.241,945.492z",fill:a},this.renderAnimationTag(7)),f.a.createElement("path",{d:"M633.137,999.951c-25.995,4.563-52.754,6.945-80.115,6.945c-62.193-0.006-121.31-12.299-175.322-34.578l-30.513,73.951 c63.456,26.189,133.062,40.633,205.835,40.627c32.01,0,63.412-2.791,93.945-8.15L633.137,999.951z",fill:a},this.renderAnimationTag(8)),f.a.createElement("path",{d:"M905.481,842.504c-27.755,33.055-60.081,62.156-95.98,86.316c-35.9,24.16-75.367,43.377-117.443,56.701l24.151,76.268 c98.934-31.334,185.438-90.313,250.539-167.844L905.481,842.504L905.481,842.504z",fill:a},this.renderAnimationTag(9))))}}]),t}(h.PureComponent);y.propTypes={diameter:b.a.oneOfType([b.a.string,b.a.number]),color:b.a.string,loadingColor:b.a.string},y.defaultProps={diameter:64,color:"#eeeeee",loadingColor:"#666666"},t.a=y},DOuS:function(e,t,a){"use strict";a.d(t,"e",function(){return i}),a.d(t,"f",function(){return l}),a.d(t,"h",function(){return c}),a.d(t,"g",function(){return u}),a.d(t,"c",function(){return d}),a.d(t,"b",function(){return p}),a.d(t,"a",function(){return m}),a.d(t,"d",function(){return g}),a.d(t,"i",function(){return h});var n=a("FyfS"),r=a.n(n),s=a("0SFc"),o=void 0;function i(e){var t=e.status_code;return!(0===t||3===t)}function l(e){return 3===e.score_processed}function c(e,t,a){if(function(e){var t=e.status||"";return t.startsWith("Wrong")||t.startsWith("Terminated")||t.startsWith("Compilation")||t.startsWith("Runtime")}(e))return"failed";var n=t.track&&"tutorials"===t.track.track_slug;return!a.is_admin&&!n&&t.is_solution_unlocked||t.solved?"solutionUnlocked":"passed"}function u(e){return!e||!l(e)}function d(e){var t=e.codechecker_time,a=e.is_additional_testcase,n=e.is_sample_testcase,r=e.individual_test_case_score,s=e.testcase_message,o=e.testcase_status,l=e.live_status||{};function c(e,t){return Array.isArray(e)?e[t]:null}return!i(e)&&l.testcase_status&&l.testcase_status.length>0&&(o=l.testcase_status,s=l.testcase_message),n.map(function(e,n){return{id:n,message:c(s,n),codeCheckerTime:c(t,n),isAdditional:c(a,n),isSample:e,status:c(o,n),testCaseScore:c(r,n)}})}function p(e){var t=e.is_sample_testcase,a=e.status_code,n=e.progress,r=e.progress_states,s=e.contest_slug,o=l(e),i=2+t.length,c=0;3===a?"number"==typeof n&&"number"==typeof r?(c=n,i=r):c=2:1!==a&&2!==a||(c=i);var u="master"===s?95:100,d=Math.max(Math.round(c*u/i),2);return o&&95===u&&(d+=5),d}function m(e,t){var a=e.next_challenge,n=e.contest_slug,r=e.random_challenge_slug,o=a&&a.status,i=t.search,c=void 0===i?"":i,u=l(e),d="",p="",m="h_r=next-challenge&h_v=zen";return m=c?c+"&"+m:"?"+m,a&&a.url&&("locked"===o?p=Object(s.f)({slug:r,contest_slug:n}):a.url&&(p=a.url),d=""+p+m),u?d:""}function g(e,t){var a=e.compile_status,n=e.custom,s=e.status,o=i(e);if(t&&o){var l=(s||"").startsWith("Accepted"),c=!!a&&!l;if(!c&&!n&&!l){var u=d(e),p=!0,m=!1,g=void 0;try{for(var h,f=r()(u);!(p=(h=f.next()).done);p=!0){1!==h.value.status&&(c=!0)}}catch(e){m=!0,g=e}finally{try{!p&&f.return&&f.return()}finally{if(m)throw g}}}return c}}function h(e){var t=0,a=3e3,n=e.challengeSlug,r=e.contestSlug,s=e.submissionId,i=e.submissionActions,l=e.profileActions,c=e.onComplete,d=e.postCompleteActions,p=e.playlistSlug;!function e(){i.getSubmissionDetail({challengeSlug:n,contestSlug:r,submissionId:s,playlistSlug:p}).then(function(n){var r=n.model;u(r)?((t+=1)>10&&a<2e4&&(a*=1.05),o&&clearTimeout(o),o=setTimeout(e,a)):(c(r),d&&(i.setGlobalSubmissionStatus(r),l.invalidateProgress()))})}();return function(){o&&clearTimeout(o)}}},FGZ8:function(e,t,a){"use strict";var n=a("ZdSA"),r=a.n(n),s=a("LvY/"),o=a.n(s),i=a("wpen"),l=a.n(i),c=a("u7UQ"),u=a.n(c),d=a("eeNd"),p=a.n(d),m=a("i1Qb"),g=a.n(m),h=a("ecfV"),f=a.n(h),v=a("cDcd"),b=a.n(v),E=a("TSYQ"),y=a.n(E),k=a("EA6I"),C=a("xeH2"),S=a.n(C);a("Fwgg");var w=function(e){function t(){o()(this,t);var e=u()(this,(t.__proto__||r()(t)).call(this));return e.onAnyPulsePopupOpen=function(t,a){a!==e.state.target&&e.state.target&&e.setState({popupOpen:!1,target:void 0})},e.openPulsePopover=function(t){var a=e.props.disabled;if(!e.state.popupOpen&&!a){var n={popupOpen:!0,target:t.currentTarget.querySelector(".inner-dot")};e.setState(n,function(){S()(window).trigger("onUIPulsePopupOpen",e.state.target)})}},e.closePulsePopover=function(){e.setState({popupOpen:!1,target:void 0}),e.props.onPopupClose()},e.state={popupOpen:!1,target:void 0},e}return p()(t,e),l()(t,[{key:"componentDidMount",value:function(){S()(window).on("onUIPulsePopupOpen",this.onAnyPulsePopupOpen)}},{key:"componentWillUnmount",value:function(){S()(window).off("onUIPulsePopupOpen",this.onAnyPulsePopupOpen)}},{key:"renderPopover",value:function(){var e=this.props,t=this.state,a=e.popupContent,n=(e.className,e.popupClass),r=(e.showPulse,e.onPopupClose,e.pulseDotProps,f()(e,["popupContent","className","popupClass","showPulse","onPopupClose","pulseDotProps"])),s=t.target,o=void 0;return o="function"==typeof a?a():a,b.a.createElement(k.a,g()({},r,{className:y()("pulse-popup",n),open:!0,onClose:this.closePulsePopover,showTip:!1,target:s,popoverSpace:0}),b.a.createElement("div",{className:"popup-content"}," ",o," "))}},{key:"renderPulse",value:function(){var e=this.props,t=e.showPulse,a=e.pulseDotProps,n=t?"pulse":"";return b.a.createElement("div",g()({className:"pulse-dot "+n,onClick:this.openPulsePopover},a),b.a.createElement("div",{className:"inner-dot"}," "))}},{key:"render",value:function(){var e=this.props.className,t=this.state.popupOpen;return b.a.createElement("div",{className:y()("pulse-popup",e)},this.renderPulse(),t&&this.renderPopover())}}]),t}(v.Component);w.defaultProps={open:!1,disabled:!1,onPopupClose:function(){}},t.a=w},Fwgg:function(e,t,a){},"IM5/":function(e,t,a){"use strict";a.r(t),a.d(t,"PureOnboardingChallenge",function(){return W});var n=a("Yz+Y"),r=a.n(n),s=a("iCc5"),o=a.n(s),i=a("V7oC"),l=a.n(i),c=a("FYw3"),u=a.n(c),d=a("mRg0"),p=a.n(d),m=a("cDcd"),g=a.n(m),h=a("17x9"),f=a.n(h),v=a("faye"),b=a.n(v),E=a("TSYQ"),y=a.n(E),k=a("xeH2"),C=a.n(k),S=a("/MKj"),w=a("fvjX"),P=a("MGin"),N=a("Q9J+"),_=a("laJX"),T=a("OEX3"),M=a("wqqT"),O=a("FGZ8"),U=a("EA6I"),j=a("p7rj"),L=a("alL8"),A=a("TkKc"),D=a("0SFc"),H=a("nzQk"),x=a("RuCt"),I=a("DOuS"),R=a("/IYb"),F=a("B1T4"),Y=a("4ycz"),z=(a("pdmS"),a("r4aX"),function(e){function t(){o()(this,t);var e=u()(this,(t.__proto__||r()(t)).call(this));return e.onCompileTest=function(t){e.clearCompileStates(),e.setState({submitInProgress:!0}),e.compileTimeout&&clearTimeout(e.compileTimeout),e.compileTestStatus(t)},e.onSubmitCode=function(t){var a=e.props,n=a.challenge,r=a.submissionActions.submitChallenge,s=t.code,o=t.language;r({contestSlug:n.contest_slug,challengeSlug:n.slug,code:s,language:o}).then(function(t){t.status?e.pollSubmission(t.model.id):t.message&&e.setState({submitInProgress:!1,submissionError:t.message})},function(){e.setState({submitInProgress:!1})})},e.toggleFullScreen=function(t){t!==e.state.fullScreenMode&&e.setState({fullScreenMode:t},function(){var a=e.leftPane,n=e.rightPane;t?(N.a.hideScrollBars(),e.splitInstance=Object(_.a)([a,n],{sizes:[50,50]})):e.splitInstance&&(N.a.showScrollBars(),e.splitInstance.destroy(),e.splitInstance=void 0)})},e.toggleErrorDetails=function(){e.setState({showErrorDetails:!e.state.showErrorDetails})},e.triggerCompile=function(t){t&&t.preventDefault(),C()(e.rightPane).find("button.bb-compile").click()},e.triggerSubmit=function(t){t&&t.preventDefault(),C()(e.rightPane).find("button.bb-submit").click()},e.challengeHintEventHandler=function(t){e.setState({challengeHintOpen:!0,challengeHintTarget:t.currentTarget})},e.onChallengeHintClose=function(){e.setState({challengeHintOpen:!1})},e.closePulse=function(){e.setState({pulsatingNode:!1}),e.renderPulse()},e.navigate=function(t){var a=e.props.appUtil,n=t.target.href,r=void 0===n?"/dashboard":n;t.preventDefault(),e.setState({navigatingTo:r}),e.markOnboardingDone().then(function(){a.goto(r)})},e.langChange=function(t){var a=e.props.challenge;a.onboarding[t]&&a.onboarding[t].hint&&e.setState({challengeHint:a.onboarding[t].hint,currentLanguage:t})},e.setWrapper=function(t){e.editorWrapper=t,e.renderPulse()},e.state={pulsatingNode:!0,fullScreenMode:!1,challengeHintOpen:!1,challengeHintTarget:void 0,challengeHint:"Type return a+b in the SolveMeFirst function"},e}return p()(t,e),l()(t,[{key:"componentDidMount",value:function(){this.startSolveTimer()}},{key:"componentWillUnmount",value:function(){this.stopPoll&&this.stopPoll(),this.compileTimeout&&clearTimeout(this.compileTimeout),this.skipOnboardingTimeout&&clearTimeout(this.skipOnboardingTimeout)}},{key:"startSolveTimer",value:function(){var e=this;this.showOutboundLink()&&(this.skipOnboardingTimeout=setTimeout(function(){e.setState({skipOnboarding:!0})},15e4))}},{key:"showOutboundLink",value:function(){return this.props.abTest.isVariant("onboarding-outbound-link",["trm1"])}},{key:"markOnboardingDone",value:function(){return this.props.profileActions.updateProfile("me",{badges_onboarding_status:"done"})}},{key:"clearCompileStates",value:function(){this.setState({errorMarkers:void 0,submissionError:void 0,submitInProgress:!1,compileData:null,showErrorDetails:!1})}},{key:"compileHasError",value:function(e){var t=e.error_markers,a=e.errors,n=e.status,r=e.testcase_status;return e.result||2===n||-1!==r.indexOf(0)||a||t&&t.markers}},{key:"compileTestStatus",value:function(e,t){var a=this,n=this.props.challenge;Object(D.a)({challenge:n,codeshellData:e,compileId:t}).then(function(t){var n=t.model,r=n.error_markers,s=n.status,o=n.errors,i=n.id;r&&r.markers&&a.setState({errorMarkers:r}),2===s&&o?a.setState({submitInProgress:!1}):s>0?a.compileHasError(n)?a.setState({submitInProgress:!1,compileData:n}):a.triggerSubmit():a.compileTimeout=setTimeout(function(){a.compileTestStatus(e,i)},1500)},function(){a.setState({submitInProgress:!1})})}},{key:"pollSubmission",value:function(e){var t=this,a=this.props,n=a.challenge,r=a.submissionActions,s=a.profileActions,o=n.contest_slug,i=n.slug;this.stopPoll=Object(I.i)({contestSlug:o,challengeSlug:i,submissionId:e,submissionActions:r,profileActions:s,postCompleteActions:!1,onComplete:function(){t.clearCompileStates(),t.markOnboardingDone(),t.setState({successfullSubmit:!0})}})}},{key:"renderPulsePopup",value:function(e,t){var a=t.nodeName,n=t.message,r=t.showPulse,s=t.wrapperClass,o=t.placeholderSelector,i=this[a],l=g.a.createElement(O.a,{pulseDotProps:{"data-analytics":"OnboardingPluse","data-attr1":a},className:"dot",popupContent:n,showPulse:r,onPopupClose:this.closePulse,align:"bottom-right"});i||(i=C()("<div class="+s+"></div>"),e.find(o).append(i),this[a]=i),b.a.unstable_renderSubtreeIntoContainer(this,l,i[0])}},{key:"renderPulse",value:function(){var e=this.state.currentLanguage,t=this.editorWrapper,a={nodeName:"editorNode",message:"This is your editor. You can code your solution here.",showPulse:this.state.pulsatingNode,wrapperClass:"pulse-wrapper-editor",placeholderSelector:".grey-header.fixed-hand0"};this.renderPulsePopup(t,a),this.renderPulsePopup(t,{nodeName:"settingsNode",message:"You can change the editor settings here",showPulse:!1,wrapperClass:"pulse-wrapper-settings",placeholderSelector:".settings-editor"}),this.renderPulsePopup(t,{nodeName:"languageNode",message:"You can choose your language here",showPulse:!1,wrapperClass:"pulse-wrapper-language",placeholderSelector:".lang-placeholder"});var n=this.hintNode,r=g.a.createElement("span",{className:"ui-icon-bulb","data-analytics":"OnboardingChallengeShowHint","data-attr1":e,onClick:this.challengeHintEventHandler}," ");n||(n=C()('<div class="hint-wrapper"> </div>'),t.find("#codeeditor-statusbar").append(n),this.hintNode=n),b.a.unstable_renderSubtreeIntoContainer(this,r,n[0])}},{key:"renderErrorMsg",value:function(){var e=this.state,t=e.compileData,a=e.submissionError,n=t||{},r=n.errors,s=n.result,o=n.testcase_status;return a?"There is some error while submitting code.":s?"Compile time error.":Array.isArray(o)&&-1!==o.indexOf(0)?"Your code did not pass the test case.":r&&r.length?"Codechecker error.":"There is some error with the code."}},{key:"renderError",value:function(){var e=this.props.challenge,t=this.state,a=t.compileData,n=t.submissionError,r=t.showErrorDetails;if(a||n)return g.a.createElement("div",{className:"error-wrap"},g.a.createElement("div",{className:"short-message"},g.a.createElement("i",{className:"ui-icon-warning-hexagon error-warning"}),g.a.createElement("span",{className:"message-text"},this.renderErrorMsg()),g.a.createElement("span",{className:"toggle-error-detail",onClick:this.toggleErrorDetails,"data-analytics":"OnboardingErrorShowMore"},r?"Less":"More")),r&&a&&g.a.createElement(F.a,{compileData:a,forkCodeSnippetEnabled:!1,challenge:e}),r&&n&&g.a.createElement("div",{className:"submission-error"},n))}},{key:"renderSuccess",value:function(){var e=this.state.successfullSubmit,t=g.a.createElement("span",null,"You just solved your first challenge."),a=g.a.createElement(P.Link,{to:"/dashboard","data-analytics":"OnboardingDashboardNav"},g.a.createElement(T.b,null,"Continue"));return g.a.createElement(Y.a,{open:!!e,allowClose:!1,message:t,button:a,modalClass:"theme-m onboarding-success-modal",badge:{level:0,badge_type:"problem-solving",stars:1,badge_name:"Problem Solving"},analyticsKey:"OnboardingChallengeSolvedModal"})}},{key:"renderEditor",value:function(){var e=this.props,t=e.challenge,a=e.profile,n=this.state,r=n.submitInProgress,s=n.errorMarkers,o=n.currentLanguage,i=n.skipOnboarding,l=n.navigatingTo,c={languages:t.languages,dynamicMode:!0,initialLanguage:a.preferred_lang,showCustomInput:!1,showCompileTest:!0,showSubmit:!0,showFullScreen:!0,autoSaveNamespace:"hr-onboarding-challenge:"+t.id};return g.a.createElement("div",null,g.a.createElement("div",{className:"codeeditor-wrapper"},g.a.createElement(R.a,{editorConfig:c,languageTemplate:Object(H.a)(t),onCompileTest:this.onCompileTest,onSubmitCode:this.onSubmitCode,toggleFullScreen:this.toggleFullScreen,errorMarkers:s,theme:"theme-m",onEditorLoad:this.setWrapper,onLangChange:this.langChange}),this.renderError()),g.a.createElement("div",{className:"onboarding-btn-wrap"},i&&g.a.createElement(T.c,{role:"link",to:"/dashboard",className:"ui-btn-secondary skip-btn","data-analytics":"OnboardingSkipChallenge",loading:"/dashboard"===l,onClick:this.navigate},"Skip"),g.a.createElement(T.b,{className:"run-btn","data-analytics":"OnboardingRunCode","data-attr1":o,color:"#FFFFFF",loading:r,onClick:this.triggerCompile},"Run Code")))}},{key:"renderChallengeHint",value:function(){var e=this.state,t=e.challengeHintTarget,a=e.challengeHintOpen,n=e.challengeHint;return g.a.createElement(U.a,{className:"popover-challenge-hint",target:t,align:"left",popoverSpace:0,open:a,onClose:this.onChallengeHintClose,showTip:!1},g.a.createElement("div",{className:"popover-content"},n))}},{key:"renderTutorialLink",value:function(){var e=this.state.navigatingTo;if(this.showOutboundLink())return g.a.createElement("span",null,"New to Programming? Check out our ",g.a.createElement(P.Link,{to:"/domains/tutorials/30-days-of-code",className:"link tutorial-link",onClick:this.navigate,"data-analytics":"OnboardingTutorialNav"},"Beginner’s tutorial.","/domains/tutorials/30-days-of-code"===e&&g.a.createElement(M.a,{className:"tutorial-link-loader",diameter:20})))}},{key:"render",value:function(){var e=this,t=this.props,a=t.challenge,n=t.globalMessage,r=this.state.fullScreenMode,s=a.preferred_body_html||a.body_html;return g.a.createElement("div",{className:"onboarding-challenge container"},this.renderChallengeHint(),g.a.createElement("div",{className:y()("full-screen-split split-wrap",{"is-fullscreen":r})},g.a.createElement("section",{ref:function(t){e.leftPane=t},className:"problem-statement-container split"},g.a.createElement("div",{className:"problem-note-header"},"This is an introductory challenge to help you get familiar with the HackerRank coding environment."),g.a.createElement("div",{className:"problem-statement",dangerouslySetInnerHTML:{__html:s}}),g.a.createElement("div",{className:"problem-note-footer"},this.renderTutorialLink())),g.a.createElement("section",{ref:function(t){e.rightPane=t},className:y()("code-editor-section split",{"move-down":!!n})},this.renderEditor()),this.renderSuccess()))}}]),t}(m.Component));z.propTypes={profile:f.a.object.isRequired,challenge:f.a.object.isRequired,submissionActions:f.a.object.isRequired,profileActions:f.a.object.isRequired,globalMessage:f.a.string,appUtil:f.a.object,abTest:f.a.object};var W=z;z=Object(S.b)(function(e){var t={challengeSlug:"solve-me-first",contestSlug:"master"},a=e.community,n=a.globalMessage,r=a.profile;return{challenge:Object(D.d)(e,t).detail,profile:r,globalMessage:n}},function(e){return{submissionActions:Object(w.b)(x.a,e),profileActions:Object(w.b)(A.a,e)}})(z),z=Object(j.a)(z),z=Object(L.b)(z),t.default=z},bQ39:function(e,t,a){},h3H1:function(e,t,a){},hKLl:function(e,t,a){},pdmS:function(e,t,a){},r4aX:function(e,t,a){},zNi8:function(e,t,a){"use strict";a.r(t);var n=a("GQeE"),r=a.n(n),s=a("Yz+Y"),o=a.n(s),i=a("iCc5"),l=a.n(i),c=a("V7oC"),u=a.n(c),d=a("FYw3"),p=a.n(d),m=a("mRg0"),g=a.n(m),h=a("cDcd"),f=a.n(h),v=a("17x9"),b=a.n(v),E=a("/MKj"),y=a("fvjX"),k=a("MrcO"),C=a("+g7O"),S=a("nzQk"),w=a("OJx6"),P=a.n(w),N=a("vmXh"),_=a.n(N),T=a("EA6I"),M=a("p7rj"),O=a("TkKc"),U=a("TSYQ"),j=a.n(U);a("h3H1");function L(e){var t=e.onLanguageClick,a=e.langKey,n=e.langName,r=e.disabled;return f.a.createElement("div",{className:j()("language-tile",{"disable-tile":r}),onClick:t.bind(null,a)},f.a.createElement("div",{className:"language-name"}," ",n," "))}L.propTypes={langKey:b.a.string.isRequired,langName:b.a.string.isRequired,disabled:b.a.bool,onLanguageClick:b.a.func};var A=L,D=a("QbLZ"),H=a.n(D),x=a("jo6Y"),I=a.n(x),R=a("eOGF"),F=a("ZaSc"),Y=a("lJF8"),z=a("P2sY"),W=a.n(z),q=a("OnOE"),V=a.n(q),Q=a("5UHj"),K=function(e){function t(){l()(this,t);var e=p()(this,(t.__proto__||o()(t)).call(this));return e.inputId="input"+Math.ceil(1e3*Math.random()),e}return g()(t,e),u()(t,[{key:"componentDidUpdate",value:function(){var e=this.refs,t=e.tooltip,a=e.input;this.props.error?(t.showTooltip({currentTarget:a}),t.updateTooltip({currentTarget:a})):t.hideTooltip({currentTarget:document.body})}},{key:"render",value:function(){var e=this.props,t=e.message,a=e.error,n=(e.value,e.icon),r=e.wrapperClass,s=e.loading,o=this.inputId,i=W()({},this.props);return["message","error","icon","wrapperClass","loading"].forEach(function(e){delete i[e]}),f.a.createElement("div",{className:j()("input-wrap",r,{"has-icon":!!n})},n&&f.a.createElement("i",{className:j()("input-icon",n)}),f.a.createElement("input",H()({ref:"input"},i,{"data-tip":t,"data-for":o,className:j()(i.className,{error:a})})),f.a.createElement(V.a,{ref:"tooltip",id:o,event:"none",eventOff:"none",globalEventOff:"none",place:"right",effect:"solid"}),s&&f.a.createElement(Q.a,{className:"input-loading"}))}}]),t}(f.a.Component);K.propTypes={message:b.a.string,error:b.a.bool,value:b.a.string,icon:b.a.string,wrapperClass:b.a.string,loading:b.a.bool},K.defaulProps={message:"",error:!1,value:"",icon:"",loading:!1};var J=K,X=function(){},B=function(e){function t(e){l()(this,t);var a=p()(this,(t.__proto__||o()(t)).call(this,e));return a.state={errorMessage:""},a.debouncedValidate=Object(R.e)(a.validateUsername.bind(a),200),a}return g()(t,e),u()(t,[{key:"componentWillReceiveProps",value:function(e){this.props.value!==e.value&&this.debouncedValidate(e.value)}},{key:"validateUsername",value:function(e){var t=this,a=this.props,n=a.onError,r=a.onSuccess,s=a.savedUsername;this.usernameXhr&&this.usernameXhr.abort(),this.setState({errorMessage:""}),e!==s&&(e.length<5||e.length>16?this.setState({errorMessage:"Username should have 5 to 16 characters."},function(){n(t.state.errorMessage)}):this.usernameXhr=Object(F.e)({url:Y.a.validateUsername,data:{username:e},success:function(e){e.errors&&e.errors.length?t.setState({errorMessage:e.errors},function(){n(t.state.errorMessage)}):r()}}))}},{key:"render",value:function(){var e=this.state.errorMessage,t=this.props,a=t.formInput,n=(t.onError,t.onSuccess,t.savedUsername,I()(t,["formInput","onError","onSuccess","savedUsername"]));return a?f.a.createElement(J,H()({},n,{error:!!e,message:e})):f.a.createElement("input",H()({},n,{type:"text"}))}}]),t}(f.a.PureComponent);B.propTypes={value:b.a.string,onError:b.a.func,onSuccess:b.a.func,savedUsername:b.a.string,formInput:b.a.bool},B.defaultProps={value:"",onError:X,onSuccess:X,formInput:!0};var G=B,Z=(a("hKLl"),function(e){function t(e){l()(this,t);var a=p()(this,(t.__proto__||o()(t)).call(this,e));return a.setEditUsername=function(){a.setState({editUsername:!0}),a.props.onEditingUsername(!0)},a.unsetEditUsername=function(){var e=a.props.profile;a.setState({editUsername:!1,username:e.username,errorMessage:"",submissionError:""}),a.props.onEditingUsername(!1)},a.updateUsername=function(e){a.setState({username:e.target.value})},a.saveUsername=function(){var e=a.state.username,t=a.props,n=t.profile,r=t.profileActions,s=void 0;s=n.me?"me":n.username?n.username:n.id,a.setState({savingUsername:!0}),r.updateProfile(s,{username:e,username_autoset_remove:1}).then(function(e){var t=e.model;a.setState({savingUsername:!1}),t.errors&&t.errors.username?a.setState({submissionError:t.errors.username}):a.unsetEditUsername()})},a.onUsernameError=function(e){a.setState({errorMessage:e})},a.onUsernameSuccess=function(){a.setState({errorMessage:""})},a.state={username:e.profile.username,submissionError:"",errorMessage:""},a}return g()(t,e),u()(t,[{key:"renderUsernameMessage",value:function(){var e=this.props.profile,t=this.state,a=t.editUsername,n=t.username,r=t.errorMessage,s=t.submissionError,o=f.a.createElement("div",{className:"bottom-message"}," Welcome to HackerRank! "),i="",l="",c="";return!0===a&&(n===e.username?(i="ui-icon-user",l="You can change your username."):r?(i="ui-icon-minus-circle ",l=r):s.length>0?(i="ui-icon-minus-circle ",l=s):(i="ui-icon-check-circle",l="This username is available",c=[f.a.createElement("span",{key:"save",className:"message-action save-option",onClick:this.saveUsername,"data-analytics":"OnboardingUsername","data-attr1":"save"}," Take it "),f.a.createElement("span",{key:"bar",className:"action-bar"}," | ")]),o=f.a.createElement("div",{className:"bottom-message"},f.a.createElement("span",{key:"icon",className:j()("username-inline",i)}," "),f.a.createElement("span",{key:"text",className:"message-text"},l),c,f.a.createElement("span",{key:"cancel",className:"message-action cancel-option",onClick:this.unsetEditUsername,"data-analytics":"OnboardingUsername","data-attr1":"cancel"}," Cancel "))),f.a.createElement("div",{className:"username-message"},f.a.createElement("div",{className:"bottom-message"},o))}},{key:"renderEditUsername",value:function(){var e=this.state,t=e.username,a=e.editUsername,n=this.props.profile;return a?f.a.createElement("div",{className:"username-inline"},f.a.createElement(G,{className:"edit-username",name:"username",type:"text",formInput:!1,value:t,savedUsername:n.username,onChange:this.updateUsername,onError:this.onUsernameError,onSuccess:this.onUsernameSuccess,autoComplete:"off",spellCheck:!1,onFocus:function(e){e.target.value="",e.target.value=t},autoFocus:!0})):[f.a.createElement("span",{className:"fixed-username username-inline",key:"username-value"},t),f.a.createElement("span",{className:"ui-icon-edit edit-username-icon",key:"edit-icon",onClick:this.setEditUsername,"data-analytics":"OnboardingUsername","data-attr1":"edit"}," ")]}},{key:"renderUsername",value:function(){return f.a.createElement("div",{className:"username"},f.a.createElement("div",{className:"username-top"},f.a.createElement("span",{className:"username-hello username-inline"}," Hello "),this.renderEditUsername()),this.renderUsernameMessage())}},{key:"renderMascot",value:function(){var e=this.props.appUtil,t=this.state.errorMessage?"onboarding/hr-mascot-error.png":"onboarding/hr-mascot.png";return f.a.createElement("div",{className:"mascot"},f.a.createElement("img",{title:"Hello there, my name is Hacktor!",src:e.assetPath(t),className:"mascot-png"}))}},{key:"render",value:function(){return f.a.createElement("div",{className:"heading-username"},f.a.createElement("div",{className:"container"},f.a.createElement("div",{className:"username-flex"},this.renderUsername(),this.renderMascot())))}}]),t}(f.a.Component));Z.propTypes={profile:b.a.object.isRequired,profileActions:b.a.object.isRequired,appUtil:b.a.object.isRequired,onEditingUsername:b.a.func.isRequired};Z=Object(E.b)(function(e){return{profile:e.community.profile}},function(e){return{profileActions:Object(y.b)(O.a,e)}})(Z);var $=Z=Object(M.a)(Z),ee=a("JB0c");a("2C5c");a.d(t,"PureOnboardingLanguage",function(){return ne});var te={c:"C",cpp:"C++",cpp14:"C++14",csharp:"C#",go:"Go",java:"Java 7",java8:"Java 8",javascript:"JavaScript",julia:"Julia",perl:"Perl",php:"PHP",pypy:"PyPy 2",pypy3:"PyPy 3",python:"Python 2",python3:"Python 3",ruby:"Ruby",scala:"Scala",sql:"SQL",swift:"Swift",visualbasic:"VB.NET"},ae=function(e){function t(){l()(this,t);var e=p()(this,(t.__proto__||o()(t)).call(this));return e.handleLanguage=function(t){var a=e.props,n=a.appUtil,r=a.profileActions;!0!==e.state.editingUsername&&("sql"!==t?(P.a.batch_track("Click","OnboardingLanguage",{attribute1:t}),k.a.set("codeshellUserOpts"),r.updateProfile("me",{preferred_lang:t,badges_onboarding_status:"usernameDone"}).then(function(){n.goto("/onboarding/challenge")})):n.goto("/domains/sql"))},e.setUsernameEdit=function(t){e.setState({editingUsername:t})},e.viewMorePopupEventHandler=function(t){P.a.track("Click","OnboardingViewMore",null),e.setState({viewMoreTarget:t.currentTarget})},e.viewMorePopoverClose=function(){e.setState({viewMoreTarget:void 0})},e.state={editingUsername:!1,viewMoreTarget:void 0},e}return g()(t,e),u()(t,[{key:"componentDidMount",value:function(){this.preloadChallengeResource(),this.setOnboardingCookie()}},{key:"setOnboardingCookie",value:function(){_.a.set("onboarding_started_at",Date.now())}},{key:"preloadChallengeResource",value:function(){var e=this.props.appUtil;window.HR.preloadPageData("/onboarding/challenge"),Object(C.a)([e.assetPath("codeshell_editor_theme_m.css")]),Object(S.c)(e)}},{key:"filterRemainingLanguages",value:function(){return ee.c.filter(function(e){return!te[e]})}},{key:"renderRemainingLanguages",value:function(){var e=this;return this.filterRemainingLanguages().map(function(t,a){return f.a.createElement("div",{key:a,className:"popover-language-item",onClick:e.handleLanguage.bind(e,t)},ee.a[t])})}},{key:"renderViewMorePopover",value:function(){var e=this.state.viewMoreTarget;return f.a.createElement(T.a,{className:"popover-languages-wrapper",target:e,align:"top",popoverSpace:0,open:!!e,onClose:this.viewMorePopoverClose,showTip:!1},f.a.createElement("div",{className:"popover-languages"},this.renderRemainingLanguages()))}},{key:"renderLanguage",value:function(){var e=this,t=this.state.editingUsername;return f.a.createElement("div",{className:"language"},f.a.createElement("div",{className:"container"},f.a.createElement("div",{className:"language-heading"}," Choose your preferred programming language: "),f.a.createElement("div",{className:"language-choose"},r()(te).map(function(a,n){return f.a.createElement(A,{langKey:a,langName:te[a],key:a+"-language-tile",disabled:t,onLanguageClick:e.handleLanguage})}),this.renderViewMorePopover(),f.a.createElement("div",{className:"language-more-link"},f.a.createElement("div",{className:"language-more-text",onClick:this.viewMorePopupEventHandler},"View More"))),f.a.createElement("div",{className:"language-footer"}," You can change your preferred language later. Languages are listed in alphabetical order. ")))}},{key:"render",value:function(){return f.a.createElement("div",{className:"hrc-onboarding"},f.a.createElement($,{onEditingUsername:this.setUsernameEdit}),this.renderLanguage())}}]),t}(f.a.Component);ae.propTypes={profile:b.a.object.isRequired,profileActions:b.a.object.isRequired,appUtil:b.a.object.isRequired};var ne=ae;ae=Object(E.b)(function(e){return{profile:e.community.profile}},function(e){return{profileActions:Object(y.b)(O.a,e)}})(ae),ae=Object(M.a)(ae);t.default=ae}}]);
//# sourceMappingURL=https://staging.hackerrank.net/assets/sourcemaps/hackerrank_r_onboarding-ff9cf50cfad95722a6bf.js.map