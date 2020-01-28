function verc() {
    $("#JD_Verification1").click();
}
var useSlideAuthCode = "1" == $("#useSlideAuthCode").val();
window.jdSlide = null;
useSlideAuthCode && j();
function j() {
    initJdSlide({
            id: "paipaiLoginSubmit",
            appId: $("#slideAppId").val() || "1604ebb2287",
            scene: "login",
            product: "bind-suspend",
            width: "100%",
            lang:$("#language").val(),
            eventListener: !1,
            top:$('#sildeAuthCodeTopPx').val()+"px",
            getInstance: function(a) {
                jdSlide = a
            }
        },
        function(a) {
            var b = a.getValidate();
            $("#paipaiLoginSubmit").attr("data-code", b);
            loginSubmit();
    })
}
window.smartInitSlide = j;


$("#paipaiLoginSubmit").click(function () {
    if(useSlideAuthCode){
        $("#nloginpwd").blur();
        jdSlide.verify();
    }else{
        loginSubmit();
    }
});


/**
 * 加密密码
 * @param pwd
 */
function getEntryptPwd(pwd){
    // var pubKey = $('#pubKey').val();
    var pubKey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDC7kw8r6tq43pwApYvkJ5laljaN9BZb21TAIfT/vexbobzH7Q8SUdP5uDPXEBKzOjx2L28y7Xs1d9v3tdPfKI2LR7PAzWBmDMn8riHrDDNpUpJnlAGUqJG9ooPn8j7YNpcxCa1iybOlc2kEhmJn5uwoanQq+CA6agNkqly2H4j6wIDAQAB';
    if(!pwd || !pubKey){
        return pwd;
    }
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(pubKey);
    return encrypt.encrypt(pwd);
}

/**
 * 获取查询字符串
 * @returns {Object}
 * @constructor
 */
function GetUrlParms()
{
    var args=new Object();
    var query=location.search.substring(1);//获取查询串
    var pairs=query.split("&");//在逗号处断开
    for(var i=0;i<pairs.length;i++)
    {
        var pos=pairs[i].indexOf('=');//查找name=value
        if(pos==-1)   continue;//如果没有找到就跳过
        var argname=pairs[i].substring(0,pos);//提取name
        var value=pairs[i].substring(pos+1);//提取value
        args[argname]=unescape(value);//存为属性
    }
    return args;
}
var validateRegExp = {
    intege: "^-?[1-9]\\d*$", //整数
    intege1: "^[1-9]\\d*$", //正整数
    intege2: "^-[1-9]\\d*$", //负整数
    num: "^([+-]?)\\d*\\.?\\d+$", //数字
    num1: "^[1-9]\\d*|0$", //正数（正整数 + 0）
    num2: "^-[1-9]\\d*|0$", //负数（负整数 + 0）
    ascii: "^[\\x00-\\xFF]+$", //仅ACSII字符
    chinese: "^[\\u4e00-\\u9fa5]+$", //仅中文
    date: "^\\d{4}(\\-|\\/|\.)\\d{1,2}\\1\\d{1,2}$", //日期
    email: "^\\w+((-\\w+)|(\\.\\w+))*\\@[A-Za-z0-9]+((\\.|-)[A-Za-z0-9]+)*\\.[A-Za-z0-9]+$", //邮件
    letter: "^[A-Za-z]+$", //字母
    letter_l: "^[a-z]+$", //小写字母
    letter_u: "^[A-Z]+$", //大写字母
    mobile: "^0?(13|15|18|14)[0-9]{9}$", //手机
    notempty: "^\\S+$", //非空
    password: "^.*[A-Za-z0-9\\w_-]+.*$", //密码
    fullNumber: "^[0-9]+$", //数字
    tel: "^[0-9\-()（）]{7,18}$", //电话号码的函数(包括验证国内区号,国际区号,分机号)
    url: "^http[s]?:\\/\\/([\\w-]+\\.)+[\\w-]+([\\w-./?%&=]*)?$", //url
    username: "^[A-Za-z0-9_\\-\\u4e00-\\u9fa5]+$" //用户名
};
//主函数
(function ($) {
    $.fn.jdValidate = function (option, callback, def) {
        var ele = this;
        var id = ele.attr("id");
        var type = ele.attr("type");
        var rel = ele.attr("rel");
        var _onFocus = $("#" + id + validateSettings.onFocus.container);
        var _succeed = $("#" + id + validateSettings.succeed.container);
        var _isNull = $("#" + id + validateSettings.isNull.container);
        var _error = $("#" + id + validateSettings.error.container);
        if (def == true) {
            var str = ele.val();
            var tag = ele.attr("sta");
            if (str == "" || str == "-1") {
                validateSettings.isNull.run({
                    prompts: option,
                    element: ele,
                    isNullEle: _isNull,
                    succeedEle: _succeed
                }, option.isNull);
            } else if (tag == 1 || tag == 2) {
                return;
            } else {
                callback({
                    prompts: option,
                    element: ele,
                    value: str,
                    errorEle: _error,
                    succeedEle: _succeed
                });
            }
        } else {
            if (typeof def == "string") {
                ele.val(def);
            }
            if (type == "checkbox" || type == "radio") {
                if (ele.attr("checked") == true) {
                    ele.attr("sta", validateSettings.succeed.state);
                }
            }
            switch (type) {
                case "text":
                case "password":
                    ele.bind("focus", function () {
                        var str = ele.val();
                        if (str == def) {
                            ele.val("");
                        }
                        if (id == "pwd") {
                            $("#pwdstrength").hide();
                        }
                        validateSettings.onFocus.run({
                            prompts: option,
                            element: ele,
                            value: str,
                            onFocusEle: _onFocus,
                            succeedEle: _succeed
                        }, option.onFocus);
                    })
                        .bind("blur", function () {
                            var str = ele.val();
                            if (str == "") {
                                ele.val(def);
                            }
                            if (validateRules.isNull(str)) {
                                validateSettings.isNull.run({
                                    prompts: option,
                                    element: ele,
                                    value: str,
                                    isNullEle: _isNull,
                                    succeedEle: _succeed
                                }, "");
                            } else {
                                callback({
                                    prompts: option,
                                    element: ele,
                                    value: str,
                                    errorEle: _error,
                                    isNullEle: _isNull,
                                    succeedEle: _succeed
                                });
                            }
                        });
                    break;
                default:
                    if (rel && rel == "select") {
                        ele.bind("change", function () {
                            var str = ele.val();
                            callback({
                                prompts: option,
                                element: ele,
                                value: str,
                                errorEle: _error,
                                isNullEle: _isNull,
                                succeedEle: _succeed
                            });
                        })
                    } else {
                        ele.bind("click", function () {
                            callback({
                                prompts: option,
                                element: ele,
                                errorEle: _error,
                                isNullEle: _isNull,
                                succeedEle: _succeed
                            });
                        })
                    }
                    break;
            }
        }
    }
})(jQuery);

//配置
var validateSettings = {
    onFocus: {
        state: null,
        container: "_error",
        style: "focus",
        run: function (option, str) {
            if (!validateRules.checkType(option.element)) {
                option.element.removeClass(validateSettings.INPUT_style2).addClass(validateSettings.INPUT_style1);
            }
            option.onFocusEle.removeClass().addClass(validateSettings.onFocus.style).html(str);
        }
    },
    isNull: {
        state: 0,
        container: "_error",
        style: "null",
        run: function (option, str) {
            option.element.attr("sta", 0);
            if (!validateRules.checkType(option.element)) {
                if (str != "") {
                    option.element.removeClass(validateSettings.INPUT_style1).addClass(validateSettings.INPUT_style2);
                } else {
                    option.element.removeClass(validateSettings.INPUT_style2).removeClass(validateSettings.INPUT_style1);
                }
            }
            option.succeedEle.removeClass(validateSettings.succeed.style);
            if (str != "") {
                option.isNullEle.removeClass().addClass(validateSettings.isNull.style).html(str);
            }
        }
    },
    error: {
        state: 1,
        container: "_error",
        style: "error",
        run: function (option, str) {
            option.element.attr("sta", 1);
            if (!validateRules.checkType(option.element)) {
                option.element.removeClass(validateSettings.INPUT_style1).addClass(validateSettings.INPUT_style2);
            }
            option.succeedEle.removeClass(validateSettings.succeed.style);
            option.errorEle.removeClass().addClass(validateSettings.error.style).html(str);
        }
    },
    succeed: {
        state: 2,
        container: "_succeed",
        style: "succeed",
        run: function (option) {
            option.element.attr("sta", 2);
            option.errorEle.empty();
            if (!validateRules.checkType(option.element)) {
                option.element.removeClass(validateSettings.INPUT_style1).removeClass(validateSettings.INPUT_style2);
            }
            option.succeedEle.addClass(validateSettings.succeed.style);
        }
    },
    INPUT_style1: "highlight1",
    INPUT_style2: "highlight2"
};

//验证规则
var validateRules = {
    isNull: function (str) {
        return (str == "" || typeof str != "string");
    },
    betweenLength: function (str, _min, _max) {
        return (str.length >= _min && str.length <= _max);
    },
    isUid: function (str) {
        return new RegExp(validateRegExp.username).test(str);
    },
    fullNumberName: function (str) {
        return new RegExp(validateRegExp.fullNumber).test(str);
    },
    isEmail: function (str) {
        return new RegExp(validateRegExp.email).test(str);
    },
    isTel: function (str) {
        return new RegExp(validateRegExp.tel).test(str);
    },
    isMobile: function (str) {
        return new RegExp(validateRegExp.mobile).test(str);
    },
    checkType: function (element) {
        return (element.attr("type") == "checkbox" || element.attr("type") == "radio" || element.attr("rel") == "select");
    }
};
//验证文本
var validatePrompt = {
    username: {
        onFocus: "4-20位字符，可由中文、英文、数字及“_”、“-”组成",
        succeed: "",
        isNull: "请输入用户名",
        error: {
            beUsed: "该用户名已被使用，请使用其它用户名注册，如果您是&quot;{1}&quot;，请<a href='../uc/login' class='flk13'>登录</a>",
            badLength: "用户名长度只能在4-20位字符之间",
            badFormat: "用户名只能由中文、英文、数字及“_”、“-”组成",
            fullNumberName: "用户名不能全为数字"
        }
    },
    pwd: {
        onFocus: "6-20位字符，可使用字母、数字或符号的组合",
        succeed: "",
        isNull: "请输入密码",
        error: {
            badLength: "密码长度只能在6-20位字符之间",
            badFormat: "密码只能由英文、数字及标点符号组成",
            simplePwd: "密码太弱，有被盗风险，建议设置多种字符组成的复杂密码"
        }
    },
    authcode: {
        onFocus: "请输入图片中的字符，不区分大小写",
        succeed: "",
        isNull: "请输入验证码",
        error: "验证码错误"
    },
    empty: {
        onFocus: "",
        succeed: "",
        isNull: "",
        error: ""
    }
};

var nameold, emailold, authcodeold;
var namestate = false, emailstate = false, authcodestate = false;
//回调函数
var validateFunction = {
    authcode: function (option) {
        validateSettings.succeed.run(option);
        authcodestate = true;
    },
    FORM_submit: function (elements) {
        var bool = true;
        for (var i = 0; i < elements.length; i++) {
            if ($(elements[i]).attr("sta") == 2) {
                bool = true;
            } else {
                bool = false;
                break;
            }
        }
        return bool;
    }
};
function strTrim(str) {
    return str.replace(/(^\s*)|(\s*$)/g, "");
}
var inputLoginName = $("#inputLoginName").val();
if(inputLoginName == null || inputLoginName == "" || inputLoginName == undefined){
    inputLoginName = "请输入邮箱/用户名/已验证手机";
}
//jdvalidate.newentry2013.js
$.extend(validatePrompt, {
    username: {
        onFocus: "",
        succeed: "",
        isNull: inputLoginName,
        error: "不存在此用户名"
    }
});
$.extend(validateFunction, {
    username: function (option) {
        validateSettings.succeed.run(option);
    },
    pwd: function (option) {
        validateSettings.succeed.run(option);
    },

    FORM_validate: function () {
        $("#loginname").jdValidate(validatePrompt.username, validateFunction.username, true);
        $("#nloginpwd").jdValidate(validatePrompt.pwd, validateFunction.pwd, true);
        return validateFunction.FORM_submit(["#loginname", "#nloginpwd"]);
    }
});

$("#loginname").jdValidate(validatePrompt.username, validateFunction.username);
$("#nloginpwd").jdValidate(validatePrompt.empty, validateFunction.pwd);
$("#authcode").jdValidate(validatePrompt.empty, validateFunction.authcode);
$("#loginname,#nloginpwd, #authcode").bind('keyup', function (event) {
    if (event.keyCode == 13) {
        $("#paipaiLoginSubmit").click();
    }
});


function loginNameOk() {
    var loginName = $("#loginname").val();
    if (validateRules.isNull(loginName) || loginName == '用户名/邮箱/已验证手机') {
        $("#loginname").attr({ "class": "text highlight2" });
        $("#loginname_error").html("请输入用户名/邮箱/已验证手机").show().attr({ "class": "error" });
        return false;
    }
    return true;
}

$("#paipaiRapidLoginSubmit").click(function () {
    paipaiRapidLogin();
});

$("#imgRapidLoginSubmit").click(function () {
    paipaiRapidLogin();
});

$("#nickNameRapidLoginSubmit").click(function () {
    paipaiRapidLogin();
});

function getSSOHostNew() {

    var retURL;
    var params = GetUrlParms();
    if (params) {
        retURL = params['ReturnUrl'];
    }
    if (!retURL) {
        return false;
    }
    var hostName = gethostName(retURL);
    if(hostName == false){
        return false;
    }
    var firstName =hostName.slice(hostName.indexOf("."),hostName.length);
    var domainArr = SysConfig.ssoArr;
    for (var i = 0; i < domainArr.length; i++) {
        var ssourl = domainArr[i];
        if (ssourl.indexOf(firstName) > 0) {
            return ssourl;
        }
    }
    return false
}


function gethostName(url){
    var arr=url.split(/\:\/\/|\/|\?/);
    if(arr.length <2){
        return false;
    }
    return arr[1];
}

/**
 * 快速登录
 * @return
 */
function paipaiRapidLogin(){
    $(this).attr({"disabled": "disabled"});
    $.ajax({
        type: "POST",
        url: "/common/rapidLoginService?nr=1&" + location.search.substring(1) + "&r=" + Math.random(),
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        error: function () {
            $("#nloginpwd").attr({ "class": "text highlight2" });
            $("#loginpwd_error").html("网络超时，请稍后再试").show().attr({ "class": "error" });
            $("#paipaiRapidLoginSubmit").removeAttr("disabled");
        },
        success: function (result) {
            if (result) {
                var obj = eval(result);
                if (obj.closeapp) {
                    window.top.location = obj.closeapp;
                    return;
                }
                if (obj.success) {
                    var ssoHost = getSSOHostNew();
                    if (ssoHost) {
                        if (isJcloudDomain(ssoHost) && obj.doubleJcloudDomain) {
                            $.getJSON("//sso.jd.com/setCookie?t=sso.jcloud.com" + "&callback=?", function () {
                            });
                            $.getJSON("//sso.jd.com/setCookie?t=sso.jdcloud.com" + "&callback=?", function () {
                                window.top.location = obj.success;
                            });
                        } else {
                            $.getJSON("//sso.jd.com/setCookie?t=" + ssoHost + "&callback=?", function () {
                                window.top.location = obj.success;
                            });
                        }
                    }else{
                        window.top.location = obj.success;
                    }
                    return;
                }

                if (obj.venture) {
                    window.top.location = "//safe.jd.com/dangerousVerify/index.action?username=" + obj.venture + "&p=" +obj.p+ "&t=" + new Date().getTime();
                    return;
                }

                if (obj.resetpwd) {
                    window.top.location = "//safe.jd.com/resetPwd/reset.action?username=" + obj.resetpwd;
                    return;
                }
                if(obj._t){
                    $("#token").val(obj._t);
                }

                $("#paipaiRapidLoginSubmit").removeAttr("disabled");
            }
        }
    });
}

function isJcloudDomain(url) {
    var jcloudDomain = ".jcloud.com";
    var jdcloudDomain = ".jdcloud.com";
    return url.indexOf(jcloudDomain, url.length - jcloudDomain.length) > 0 || url.indexOf(jdcloudDomain, url.length - jdcloudDomain.length) > 0;
}

/**
 * 登录成功后，重定向,IE浏览器6-8需要通过a href方式实现添加referer
 */
function successRedirectURL(url){
    var isIE = !-[1,];
    if(isIE){
        var link = document.createElement("a");
        link.href = url;
        link.style.display = 'none';
        document.body.appendChild(link);
        link.target = "_top";
        link.click();
    }else{
        window.top.location = url;
    }
}


function loginSubmit() {
    var flag = validateFunction.FORM_validate();
    if (flag) {
        var srcValue = $("#JD_Verification1").attr("src");
        if (!srcValue) {
            srcValue = $("#JD_Verification1").attr("src2");
        }
        var uuid = srcValue.split("&uid=")[1].split("&")[0];
        $(this).attr({ "disabled": "disabled" });

        var authcode;
        if(useSlideAuthCode){
            authcode = $("#paipaiLoginSubmit").attr('data-code');
        }else{
            authcode = $('#authcode').val();
        }

        $.ajax({
            type: "POST",
            url: "/common/loginService?nr=1&uuid=" + uuid + "&" + location.search.substring(1) + "&r=" + Math.random(),
            contentType: "application/x-www-form-urlencoded; charset=utf-8",
            data: {
                uuid:$('#uuid').val(),
                eid:$('#eid').val(),
                fp:$('#sessionId').val(),
                _t:$('#token').val(),
                loginname:$('#loginname').val(),
                nloginpwd:getEntryptPwd($('#nloginpwd').val()),
                authcode:authcode,
                pubKey:$('#pubKey').val(),
                sa_token:$('#sa_token').val(),
                seqSid:window._jdtdmap_sessionId,
                useSlideAuthCode:$("#useSlideAuthCode").val()
            },
            error: function () {
                $("#nloginpwd").attr({ "class": "text highlight2" });
                $("#loginpwd_error").html("网络超时，请稍后再试").show().attr({ "class": "error" });
                $("#paipaiLoginSubmit").removeAttr("disabled");
                if(useSlideAuthCode) {
                    smartInitSlide();
                }
            },
            success: function (result) {
                if (result) {
                    var obj = eval(result);
                    if (obj.closeapp) {
                        window.top.location  = obj.closeapp;
                        return;
                    }
                    if (obj.success) {
                        var ssoHost = getSSOHostNew();
                        if(ssoHost){
                            if (isJcloudDomain(ssoHost) && obj.doubleJcloudDomain) {
                                $.getJSON("//sso.jd.com/setCookie?t=sso.jcloud.com" + "&callback=?", function () {
                                });
                                $.getJSON("//sso.jd.com/setCookie?t=sso.jdcloud.com" + "&callback=?", function () {
                                    successRedirectURL(obj.success);
                                });
                            } else {
                                $.getJSON("//sso.jd.com/setCookie?t=" + ssoHost + "&callback=?", function () {
                                    successRedirectURL(obj.success);
                                });
                            }
                        }else{
                            successRedirectURL(obj.success);
                        }
                        return;
                    }
                    if(useSlideAuthCode && !obj.success) {
                        smartInitSlide();
                    }

                    if (obj.rescue) {
                        window.top.location = obj.rescue;
                        return;
                    }
                    if (obj.newSafeVerify) {
                        window.top.location = obj.safeVerifyUrl;
                        return;
                    } else {
                        if (obj.venture) {
                            window.top.location = "//safe.jd.com/dangerousVerify/index.action?username=" + obj.venture + "&p=" + obj.p + "&t=" + new Date().getTime();
                            return;
                        }

                        if (obj.resetpwd) {
                            window.top.location = "//safe.jd.com/resetPwd/reset.action?username=" + obj.resetpwd;
                            return;
                        }
                    }

                    if(obj._t){
                        $("#token").val(obj._t);
                    }

                    $("#paipaiLoginSubmit").removeAttr("disabled");


                    // if (obj.verifycode || obj.authcode1 || obj.authcode2) {
                    //     $("#o-authcode").show();
                    //
                    // }
                    if (obj.verifycode || obj.authcode1 || obj.authcode2 || obj.emptyAuthcode) {
                        if(useSlideAuthCode){
                            // $("#s-authcode").show();
                        }else{
                            $("#o-authcode").show();
                        }
                    }
                    if(!useSlideAuthCode){
                        verc();
                    }
                    if (obj.authcode2) {
                        $("#loginname").attr({ "class": "text highlight2" });
                        $("#loginname_error").html("您的账号有安全隐患，建议您登录后修改为复杂密码").show().attr({ "class": "message" });
                        $("#authcode_error").hide();
                        $("#loginpwd_error").hide();
                    }
                    if (obj.username) {
                        $("#loginname").attr({ "class": "text highlight2" });
                        $("#loginname_error").html(obj.username).show().attr({ "class": "error" });
                        $("#authcode_error").hide();
                        $("#loginpwd_error").hide();
                    }
                    if (obj.pwd) {
                        $("#nloginpwd").attr({ "class": "text highlight2" });
                        $("#loginpwd_error").html(obj.pwd).show().attr({ "class": "error" });
                        $("#authcode_error").hide();
                        $("#loginname_error").hide();
                    }
                    if (obj.emptyAuthcode) {
                        if(!useSlideAuthCode){
                            $("#o-authcode").show();
                            $("#authcode").attr({ "class": "text text-1 highlight2" });
                        }
                        $("#authcode_error").html(obj.emptyAuthcode).show().attr({ "class": "error" });
                        $("#loginpwd_error").hide();
                        $("#loginname_error").hide();
                    }
                }
            }
        });
    }else{
        if(useSlideAuthCode) {
            smartInitSlide();
        }
    }
};
$("#nloginpwd").bind('focus',function(){
    $("#loginpwd_error").empty();
    $("#loginpwd_error").removeClass().addClass("hide");
});