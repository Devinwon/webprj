	function hz6d$(id)
	{
		return document.getElementById(id) ? document.getElementById(id) : null;
	}
	var hz6d_guest_id = "";
	var hz6d_get_guest_id_over = 0;
	var hz6d_get_guest_id_num = 5;
	var hz6d_get_guest_id_timer = 0;
	var hz6d_cus_web_msg_gids = "";
	var hz6d_block_trace_guest = false;
	var hz6d_block_trace_over = false;

	var hz6d_flash_html='<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0" width="1" height="1" align="middle" id="mainserverim"><param name="allowScriptAccess" value="always" /><param name="movie" value="http://chat.53kf.com/flash/hz6d_53kf_kf_gid.swf"/><param name="quality" value="high" /><param name="wmode" value="transparent"><param name="bgcolor" value="#ffffff" /><embed name="mainserverim" src="http://chat.53kf.com/flash/hz6d_53kf_kf_gid.swf" quality="high" wmode="transparent" bgcolor="#ffffff" width="1" height="1" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" swLiveConnect="true"/></object>';
	document.write(hz6d_flash_html);

	function returnGid(args){
		hz6d_guest_id = args;
		hz6d_get_guest_id_over = 1;
	}

	function hz6d_get_guest_id(){
		if(hz6d_get_guest_id_over==0 && hz6d_get_guest_id_num>0){
			hz6d_get_guest_id_num--;
			setTimeout("hz6d_get_guest_id()", 500);
		}else{
			clearTimeout(hz6d_get_guest_id_timer);

			// guest_id guest_ip 是否在block_trace中，即是否阻止轨迹 
      hz6d_block_trace_guest = (function(){
        var ip = "",
            id = hz6d_guest_id,
            block_trace_guest_id = [],
            block_trace_guest_ip = [];
        for (var i = 0; i < block_trace_guest_id.length; i++)
        {
          if (id == block_trace_guest_id[i] && id != '') return true;
        }
        
        for(var i = 0; i < block_trace_guest_ip.length; i++)
        {
          if (ip == block_trace_guest_ip[i] && ip != '') return true;
        }
        return false;
      })();
			hz6d_block_trace_over = true;

			if(hz6d_guest_id!="" && hz6d_guest_id>0){
				if(hz6d_cus_web_msg_gids.indexOf(hz6d_guest_id)>=0){
					var url = "http://www3.53kf.com/lword_reply.php?company_id=70824690&guest_id="+hz6d_guest_id;
					hz6d_createScript("hz6d_lword_reply", url);
				}
			}
		}
	}

	function hz6d_createScript(id, url){
		var oldS=hz6d$(id);
		if(oldS!=null) oldS.parentNode.removeChild(oldS);
		var t=document.createElement('script');
		t.src = url;
		t.type = 'text/javascript';
		t.id = id;
		document.getElementsByTagName('head')[0].appendChild(t);
	}

	function hz6d_cus_web_msg_open(){
		var openurl = "http://www.tgjy.cn/53.htm?arg=tgjy&style=1&kf=&kflist=off&kf=&zdkf_type=1&language=cn&charset=gbk&username=&userinfo=&introurl=&lyurl=&lytype=0&copartner=&referer=http%3A%2F%2Fwww.tgjy.cn%2F&keyword=&brief=&logo=&question=";
		try{
			window.open(openurl,"_blank","height=473,width=703,top=200,left=200,status=yes,toolbar=no,menubar=no,resizable=yes,scrollbars=no,location=no,titlebar=no");
		}catch(e){}
	}

	hz6d_get_guest_id_timer = setTimeout("hz6d_get_guest_id()", 500);///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
      // 发送acc 
			var hz6d_filter_time = "";

      function hz6d_sendACC(){
        if(hz6d_get_guest_id_over==0 && hz6d_get_guest_id_num>0){
          hz6d_get_guest_id_num--;
          setTimeout("hz6d_sendACC()",500);
          return;
        }
				
				if(!hz6d_block_trace_over){
					setTimeout("hz6d_sendACC()",10);
					return;
				}

				if(hz6d_block_trace_guest) return;

        var kh_status = 0;
        if(onliner_zdfq==3) { kh_status = 3; }
        if(hz6d_guest_id==0) { hz6d_guest_id = ""; }

				var ip = "221.0.91.117";
				if("" != ip){
					var com_id = "70824690";
					var guest_ip_info = "";
					var from_page = "";
					var talk_page = "http%3A%2F%2Fwww.tgjy.cn%2F";
					var kf_time = "1352616696";
					var time = new Date().getTime();
					var curSecond = Math.floor(time/1000);
				
					//var url = "http://www3.53kf.com/sendacc.jsp?cmd=ACC&did=0&sid=12&company_id="+com_id+"&guest_id="+hz6d_guest_id+"&status="+kh_status+"&guest_name=&guest_ip="+ip+"&guest_ip_info="+guest_ip_info+"&from_page="+from_page+"&talk_page="+talk_page+"&kf_time="+kf_time+"&bto_id6d=-99&time="+time+"&title="+decodeURIComponent(document.title);
					var url = "http://www3.53kf.com/sendacc.jsp?cmd=ACC&did=0&sid=12&company_id="+com_id+"&guest_id="+hz6d_guest_id+"&status="+kh_status+"&guest_name=&guest_ip="+ip+"&guest_ip_info="+guest_ip_info+"&from_page="+from_page+"&talk_page="+talk_page+"&kf_time="+kf_time+"&bto_id6d=-99&time="+time;
					
					if(hz6d_filter_time!=""){
						if(hz6d_filter_time > 0){
							if(curSecond%hz6d_filter_time==0){
								hz6d_createScript("hz6d_send_acc", url);
							}
						}
					}else{
						hz6d_createScript("hz6d_send_acc", url);
					}
				}
        setTimeout("hz6d_sendACC()",20000);
      }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

      // 邀请框处理 
      var acc_pop_page     = "1";
      var acc_pop_pagenum  = 1;
      var acc_pop_total    = "1";
      var acc_pop_totalnum = 5;
      var nowpage          = "www_tgjy_cn_";
      var acc_lr           = "";
      var acc_tb           = "";
      var acc_middle       = "1";
      var how_float       = "0";
      var acc_left         = 280;
      var acc_top          = 230;
      var acc_autotype     = "0"; // 点击接受或拒绝不再弹出 

      var zdyivt            = "1";
      var ivtstr            = "<div id=\'acc_title\' style=\'position:relative;overflow:hidden;background-image: url(http://www3.53kf.com/img/ivt/new2011_04/dialog_18.png);background-repeat: no-repeat;font-size: 12px;width: 400px;height: 165px;z-index: 0;border-style: none;\'><div style=\'overflow: hidden;position:absolute;background-image: url(http://www3.53kf.com/img/upload/tgjy/zdyivt/zdyivt_53kf_1344674634.png);background-repeat: no-repeat;font-size: 12px;color: #000000;text-align:left;width: 22px;height: 20px;left: 12px;top: 8px;z-index: 1;font-family:&#23435;&#20307;;\' id=\'ivtzdy_53kf_1\'></div><div style=\'overflow: hidden;position:absolute;background-image: url(http://www3.53kf.com/img/ivt/new2011_04/dialog_14.png);background-repeat: no-repeat;font-size: 12px;color: #000000;width: 18px;height: 18px;left: 375px;top: 5px;z-index: 2;font-family:&#23435;&#20307;;cursor:pointer;\' onclick=\';onliner_zdfq=3;hidden_ivt();\' id=\'hz6d_53kf_invite_hid\'></div><div style=\'overflow: hidden;position:absolute;background-repeat: no-repeat;line-height:120%;font-size: 12px;color: #FFFFFF;text-align:left;width: 325px;height: 14px;left: 40px;top: 8px;z-index: 3;font-family:&#23435;&#20307;;\' id=\'ivtzdy_53kf_3\'>&#27743;&#35199;&#25945;&#32946;&#32771;&#35797;&#36741;&#23548;&#20013;&#24515;</div><div style=\'overflow: hidden;position:absolute;background-repeat: no-repeat;line-height:120%;font-size: 12px;text-align:left;width: 245px;height: 14px;left: 140px;top: 40px;z-index: 4;font-family:&#23435;&#20307;;\' id=\'ivtzdy_53kf_4\'>&#27426;&#36814;&#24744;&#65281;</div><div style=\'overflow: hidden;position:absolute;background-repeat: no-repeat;line-height:120%;font-size: 12px;color: #000000;text-align:left;width: 245px;height: 45px;left: 140px;top: 60px;z-index: 5;font-family:&#23435;&#20307;;\' id=\'ivtzdy_53kf_5\'>&#36731;&#26494;&#36807;&#20851;&#65292;&#39034;&#21033;&#27605;&#19994;&#65281;&#20320;&#36824;&#22312;&#29369;&#35947;&#20160;&#20040;&#65311;&#32771;&#21069;&#32771;&#21518;&#20840;&#38754;&#21327;&#21161;&#65292;&#36890;&#20851;&#25252;&#33322;&#26377;&#20445;&#38556;&#65281;</div><a href=\"http://www.tgjy.cn/53.htm\" target=\"_blank\" style=\"cursor:pointer; text-decoration:none;\"><div style=\'overflow: hidden;position:absolute;background-image: url(http://www3.53kf.com/img/ivt/new2011_04/dialog_11.png);background-repeat: no-repeat;font-size: 12px;color: #000000;text-align:left;width: 101px;height: 35px;left: 140px;top: 111px;z-index: 6;font-family:&#23435;&#20307;;\' id=\'ivtzdy_53kf_6\'></div></a><div style=\'overflow: hidden;position:absolute;background-image: url(http://www3.53kf.com/img/ivt/new2011_04/dialog_12.png);background-repeat: no-repeat;font-size: 12px;color: #000000;text-align:left;width: 103px;height: 35px;left: 255px;top: 111px;z-index: 7;font-family:&#23435;&#20307;;cursor:pointer;\' onclick=\';onliner_zdfq=3;hidden_ivt();\' id=\'hz6d_53kf_invite_hid\'></div><div style=\'overflow: hidden;position:absolute;background-repeat: no-repeat;line-height:120%;font-size: 15px;color: #FFFFFF;text-align:center;font-weight: bold;width: 100px;height: 20px;left: 140px;top: 121px;z-index: 8;font-family:&#23435;&#20307;;cursor:pointer;\' onclick=\';onliner_zdfq=2;window.open(\"talk_openurl\",\"_blank\",\"height=473,width=703,top=200,left=200,status=yes,toolbar=no,menubar=no,resizable=yes,scrollbars=no,location=no,titlebar=no\");hidden_ivt();\' id=\'hz6d_53kf_invite_acc\'>&#22312;&#32447;&#21672;&#35810;</div><a href=\"http://www.tgjy.cn/qq.htm\" target=\"_blank\" style=\"cursor:pointer; text-decoration:none;\"><div style=\'overflow: hidden;position:absolute;background-repeat: no-repeat;line-height:120%;font-size: 15px;color: #666666;text-align:center;font-weight: bold;width: 100px;height: 20px;left: 255px;top: 121px;z-index: 9;font-family:&#23435;&#20307;;\' id=\'ivtzdy_53kf_9\'>QQ&#21672;&#35810;</div></a></div>";
      var zdyivt_width      = "400px";
      var zdyivt_height     = "165px";
      var acc_reinvite      = "1";
      var acc_reauto        = "1";
      var acc_reauto_time   = 30000;
      var acc_poptime       = 8000;
      var acc_poptype       = 1;
      var acc_freeze        = "off";
      var acc_chattype      = 2;
      var acc_from_kf       = false;
      var hz6d_ivt_effect   = "0";
			var hz6d_cname				= "&#27743;&#35199;&#25104;&#32771;&#25253;&#21517;&#20013;&#24515; ";
			hz6d_cname = hz6d_cname.replace(/\"/g, '&quot;').replace(/\'/g, '&#039;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
			var hz6d_ivt_tpl			= "../templates/ivt/green/kf.tpl";

      var acc_content = "&#26377;&#20160;&#20040;&#21487;&#20197;&#24110;&#21161;&#24744;&#30340;&#21527;?";
      if(0==0)
      {
        acc_content = "&#23458;&#26381;&#19981;&#22312;&#32447;&#65292;&#28857;&#20987;&#30041;&#35328;&#65281;";
      }

      var ivt_timer = 0;
      var force_kf = "";
      var man_content = "";

      document.write("<iframe id=\"kfiframe\" style=\"display:none;overflow:hidden;\" frameborder=\"0\" ></iframe>");
      document.write("<div id=\"kfivteffect\" style=\"display:none;position:absolute;width:0px;height:0px;overflow:hidden;border:1px solid #1B88D0;background:#D6EEFD;z-index:10087;\"></div>");
      document.write("<div id=\"kfivtwin\" style=\"display:none;overflow:hidden;\">"+ivtstr+"</div>");
			document.write("<div id=\"div_company_mini\" style=\"display:none;position:fixed;_position:absolute;right:0;bottom:0;width:403px;height:378px;overflow:hidden;z-index:10089;cursor:move;\"><div id=\"hz6d_cname_mini_div\" style=\"overflow:hidden;position:absolute;top:7px;left:10px;width:330px;height:20px;color:#fff;text-indent:30px;background:url('http://www3.53kf.com/style/chat/minichat2/img/minchat_ns.gif') -79px 0 no-repeat;\">"+hz6d_cname+"</div><div title=\"&#32553;&#23567;\" mini_narrow=\"&#32553;&#23567;\" mini_recover=\"&#36824;&#21407;\" max_min=\"max\" style=\"position:absolute;top:10px;right:46px;width:12px;height:12px;background:url('http://www3.53kf.com/style/chat/minichat2/img/min.gif') no-repeat; cursor:pointer;\" onclick=\"max_min_company_mini(this);\"></div><div title=\"&#20999;&#25442;&#21040;&#27491;&#24120;&#31383;&#21475;\" style=\"position:absolute;top:10px;right:28px;width:12px;height:12px;background:url('http://www3.53kf.com/style/chat/minichat2/img/maxto.gif') no-repeat; cursor:pointer;\" onclick=\"max_from_company_mini(this);\"></div><div title=\"&#20851;&#38381;\" style=\"position:absolute;top:10px;right:10px;width:12px;height:12px;background:url('http://www3.53kf.com/style/chat/minichat2/img/minchat_ns.gif') -18px 0 no-repeat;cursor:pointer;\" onclick=\"close_company_mini();\"></div><div id=\"mini_header_bg_div\" style=\"width:403px;height:35px;background:url('http://www3.53kf.com/style/chat/minichat2/img/header_bg.gif') no-repeat;\"></div><div id=\"iframe_company_mini_div\" style=\"width:100%;height:100%;\"><iframe id=\"iframe_company_mini\" frameborder=\"0\" width=\"100%\" height=\"100%\" ></iframe></div></div>");

      //  mini悬浮对话窗口 转到正常聊天窗口 
      function max_from_company_mini(t)
      {
        var openurl = "http://www.tgjy.cn/53.htm?arg=tgjy&style=1&kf=&kflist=off&kf=&zdkf_type=1&language=cn&charset=gbk&username=&userinfo=&introurl=&lyurl=&lytype=0&copartner=&referer=http%3A%2F%2Fwww.tgjy.cn%2F&keyword=&brief=&logo=&question=&tfrom=2"+force_kf;
        try{
          var chatWindow = window.open(openurl,"_blank","height=473,width=703,top=200,left=200,status=yes,toolbar=no,menubar=no,resizable=yes,scrollbars=no,location=no,titlebar=no");
          if(chatWindow==null){
            location.href = openurl;
          }else{
            chatWindow.focus();
            chatWindow.opener = window;
          }
        }catch(e){
          location.href = openurl;  // 傲游 
				}
        close_company_mini();
        t.parentNode.parentNode.removeChild(t.parentNode);
      }
      //  mini悬浮对话窗口 缩小、放大 
      function max_min_company_mini(t)
      {
        if (t.getAttribute('max_min') == 'max')
        {
          hz6d$("div_company_mini").style.height = "36px";
          hz6d$("hz6d_cname_mini_div").style.width = "130px";
          hz6d$("div_company_mini").style.width = "203px";
          hz6d$("iframe_company_mini_div").style.display = "none";
          t.style.backgroundImage = "url('http://www3.53kf.com/style/chat/minichat2/img/max.gif')";
          hz6d$("mini_header_bg_div").style.backgroundImage = "url('http://www3.53kf.com/style/chat/minichat2/img/header_bg2.gif')";
          t.setAttribute('max_min','min');
          t.title = t.getAttribute('mini_recover');
        }
        else
        {
          hz6d$("iframe_company_mini_div").style.display = "";
          hz6d$("div_company_mini").style.height = "378px";
          hz6d$("div_company_mini").style.width = "403px";
          hz6d$("hz6d_cname_mini_div").style.width = "330px";
          t.style.backgroundImage = "url('http://www3.53kf.com/style/chat/minichat2/img/min.gif')";
          hz6d$("mini_header_bg_div").style.backgroundImage = "url('http://www3.53kf.com/style/chat/minichat2/img/header_bg.gif')";
          t.setAttribute('max_min','max');
          t.title = t.getAttribute('mini_narrow');
        }
        hz6d$("div_company_mini").style.right = "0px";
        hz6d$("div_company_mini").style.bottom = "0px";
      }
      // 定时调用判断是否显示邀请框 
      function hz6d_checkIvt() { hz6d_showIvt(); }

      // 显示冻结层 
      function hz6d_showFreeze(){
        if(acc_freeze=="on"){
          var div = hz6d$("hz6d_freeze_div");
          if(div==null){
						hz6d_createFreezeDiv();
					}else{
						div.style.display = "block";
					}
        }
      }

      // 创建冻结层 
      function hz6d_createFreezeDiv(){
        var div = document.createElement('DIV');
        div.id = 'hz6d_freeze_div';
        with(div.style){
          zIndex=6998;
          top='0px';
          left='0px';
          width='100%';
          height='100%';
          border='none';
          margin=padding=0;
          position='absolute';
          backgroundColor='#000';
          opacity='0.2';
          filter='alpha(opacity=20)';
          duration=1000;
        }
        document.body.insertBefore(div,document.body.firstChild);
				setInterval("hz6d_checkFreezeStyle()", 1);
      }
			
			var hz6d_maxPageWidth = 0;
			var hz6d_maxPageHeight = 0;
      // 定时调整冻结层大小 
      function hz6d_checkFreezeStyle(){
				try{
					var freeze = hz6d$("hz6d_freeze_div");
					if(freeze!=null){
						var scroll = hz6d_getScrollPosition();
						var client = hz6d_getClientWindow();
						var w = client.width+scroll.sLeft;
						var h = client.height+scroll.sTop;
						if(w > hz6d_maxPageWidth){
							hz6d_maxPageWidth = w;
							freeze.style.width = hz6d_maxPageWidth+"px";
						}
						if(h > hz6d_maxPageHeight){
							hz6d_maxPageHeight = h;
							freeze.style.height = hz6d_maxPageHeight+"px";
						}
					}
				}catch(e){}
      }

      // 删除冻结层 
      function hz6d_destroyFreezeDiv(){
        try{
          var div = hz6d$("hz6d_freeze_div");
					if(div!=null) { div.style.display = "none"; }
        }catch(e){}
      }

      // 显示邀请框 
      function hz6d_showIvt(){
        if(hz6d_isShowIvt()){
          if(hz6d$("kfivtwin").style.display=="none" && onliner_zdfq!=2 || acc_from_kf==true){
            acc_from_kf = false;
            get_ACCWindow();
            hz6d_setTotalNum();
            hz6d_setPageNum();
          }
        }
      }

      // 判断是否显示邀请框 
      function hz6d_isShowIvt(){
        if(acc_reinvite==1 && acc_from_kf==true) { return true; }
        if(acc_autotype==3){
          //点击接受或拒绝后不再弹出 
          if(onliner_zdfq!=0){
            return false;
          }
        }
        if(!hz6d_overTotalNum()){
          if(hz6d_overPageNum()){
            return false;
          }
        }else{
          return false;
        }
        return true;
      }

      // 判断是否超过所有页面次数 
      function hz6d_overTotalNum(){
        if(hz6d$("kfivtwin").style.display!="none") return;
        if(acc_pop_total==1){
          var total_invite = hz6d_getCookie("invite_53kf_totalnum_1");
          if(total_invite=="") { total_invite = 0; }
          if(total_invite>=acc_pop_totalnum) { return true; }
        }
        return false;
      }

      // 判断是否超过每个页面次数 
      function hz6d_overPageNum(){
        if(hz6d$("kfivtwin").style.display!="none") return;
        if(acc_pop_page==1){
          var page_invite = hz6d_getCookie(nowpage);
          if(page_invite=="") { page_invite = 0; }
          if(page_invite>=acc_pop_pagenum) { return true; }
        }
        return false;
      }

      // 设置所有页面弹出次数 
      function hz6d_setTotalNum()
      {
        var total_invite = hz6d_getCookie("invite_53kf_totalnum_1");
        if(total_invite=="") { total_invite = 0; }
        total_invite++;
        document.cookie = "invite_53kf_totalnum_1="+total_invite;
      }
      
      // 设置每个页面弹出次数 
      function hz6d_setPageNum()
      {
        var page_invite = hz6d_getCookie(nowpage);
        if(page_invite=="") { page_invite = 0; }
        page_invite++;
        document.cookie = nowpage+"="+page_invite;
      }
      
      // 隐藏邀请框 
      function hidden_ivt()
      {
        if(acc_autotype==3) { document.cookie = "onliner_zdfq70824690="+onliner_zdfq; }
        try{ hz6d$("kfiframe").style.display = "none"; }catch(e){}
        try{ hidden_ACCWindow(); }catch(e){}
        hz6d_destroyFreezeDiv();
        try{ force_kf = ""; }catch(e){}
      }
			
			// 加载后是否显示邀请框 
			function hz6d_LoadToShowIvt()
			{
				if(acc_poptype==1)
				{
					setTimeout("hz6d_checkIvt()", acc_poptime);
				}
				else if(acc_poptype==2 && onliner_zdfq!=2)
				{
					setTimeout("get_location(acc_chattype)", acc_poptime);
				}
			}
            
      //查询link表，判断是否已建立对话 
      if(0==1){
				hz6d_sendACC();
				hz6d_LoadToShowIvt();
			}
			
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
      
			var hz6d_company_mini = null;
      // 强制对话 
      function get_location(type){
        // type:1 覆盖本窗口 2 如果被拦截，则本窗口刷新 3 悬浮对话窗口 
				try{
					var openurl = "http://www.tgjy.cn/53.htm?arg=tgjy&style=1&kf=&kflist=off&kf=&zdkf_type=1&language=cn&charset=gbk&username=&userinfo=&introurl=&lyurl=&lytype=0&copartner=&referer=http%3A%2F%2Fwww.tgjy.cn%2F&keyword=&brief=&logo=&question=&tfrom=2"+force_kf;
					if(type==1){
						location.href = openurl;
					}else if(type==2){
						try{
							var chatWindow = window.open(openurl,"_blank","height=473,width=703,top=200,left=200,status=yes,toolbar=no,menubar=no,resizable=yes,scrollbars=no,location=no,titlebar=no");
							if(chatWindow==null){
								location.href = openurl;
							}else{
								chatWindow.focus();
								chatWindow.opener = window;
							}
						}catch(e){
							location.href = openurl;  // 傲游 
						}
					}else{
						var openurl_mini = openurl;
						var tpl = "";
						if(openurl_mini.match(/&tpl=[^&]*/gim)!=null){
							openurl_mini = openurl_mini.replace(/&tpl=[^&]*/gim, "&tpl=minichat2");
						}else{
							tpl = "&tpl=minichat2";
						}
						hz6d$("iframe_company_mini").src = openurl_mini+tpl;
						var div = hz6d$("div_company_mini");
						hz6d_company_mini = new hz6d_div_scroll(div);
						hz6d_company_mini.start();
						div.style.display = "";
					}
					force_kf = "";
					onliner_zdfq = 2;
					hidden_ivt();
				}catch(e){}
      }
			// 悬浮邀请框滚动 
			function hz6d_div_scroll(d){
				var self = this;
				this.div = d;
				this.right = 0;
				this.bottom = 0;
				this.timer = 0;
				this.posX=this.posY=this.posR=this.posB=0;
				this.scrollX=this.scrollY=false;

				this.start = function(){
					this.goPosition();
					this.timer = setInterval(this.scroll, 10);
					this.move();
				}
				this.stop = function(){
					if(this.timer!=0){ clearInterval(this.timer); }
				}
				this.goPosition = function(){
					//var scroll = hz6d_getScrollPosition();
					//this.right = -scroll.sLeft;
					//this.bottom = -scroll.sTop;
					this.right = 0;
					this.bottom = 0;
					this.div.style.right = this.right + "px";
					this.div.style.bottom = this.bottom + "px";
				}
				this.scroll = function(){
					var scroll = hz6d_getScrollPosition();
					var cur_right = -scroll.sLeft;
					var cur_bottom = -scroll.sTop;
					if(cur_right != self.right){
						self.right = smoothMove(self.right, cur_right);
						self.div.style.right = self.right + "px";
						self.scrollX = true;
					}
					if(self.scrollX){
						self.div.style.right = "0px";
						self.scrollX = false;
					}
					if(cur_bottom != self.bottom){
						self.bottom = smoothMove(self.bottom, cur_bottom);
						self.div.style.bottom = self.bottom + "px";
						self.scrollY = true;
					}
					if(self.scrollY){
						self.div.style.bottom = "0px";
						self.scrollY = false;
					}
				}
				this.move = function(){
					this.div.onmousedown = function(e){
						if(!e) e = window.event; //如果是IE 
						self.posX = e.clientX;
						self.posY = e.clientY;
						self.posR = parseInt(self.div.style.right);
						self.posB = parseInt(self.div.style.bottom);
						if(self.div.setCapture){
							self.div.setCapture();
						}else if(window.captureEvents){
							window.captureEvents(Event.MOUSEMOVE|Event.MOUSEUP);
						}
						var d = document;
						d.onmousemove = function(ev){
							if(!ev) ev = window.event; //如果是IE 
							self.div.style.right = (self.posR - (ev.clientX - self.posX)) + "px";
							self.div.style.bottom = (self.posB - (ev.clientY - self.posY)) + "px";
						}
						d.onmouseup = function(){
							if(self.div.releaseCapture){
								self.div.releaseCapture();
							}else if(window.captureEvents){
								window.captureEvents(Event.MOUSEMOVE|Event.MOUSEUP);
							}
							d.onmousemove = null;
							d.onmouseup = null;
						}
					}
				}
			}
			// 关闭悬浮框 
			function close_company_mini(){
				hz6d$("div_company_mini").style.display = "none";
				hz6d$("iframe_company_mini").src = "";
				hz6d_company_mini.stop();
			}

      var ivt_top = 0;
      var ivt_left = 0;

      var ivt_width="400";
      var ivt_height="140";

      var hz6d_effect_time = 200;
      var hz6d_effect_timer = 10;

      // 显示邀请框 
      function get_ACCWindow(){
        var ivtPosition = hz6d_getIvtPosition();

        if(zdyivt==1){
          ivt_height_init = zdyivt_height;
          ivt_width_init = zdyivt_width;
        }else{
          ivt_height_init = "140px";
          ivt_width_init = "400px";
        }
        hz6d$("kfivtwin").style.height = ivt_height_init;
        hz6d$("kfivtwin").style.width = ivt_width_init;

        try{
          hz6d$("kfivtwin").style.zIndex = "10088";
          hz6d$("kfivtwin").style.fontSize = "12px";
          hz6d$("kfivtwin").style.position = "absolute";
					if(how_float==1 && hasdoctype) hz6d$("kfivtwin").style.position = "fixed";

          hz6d$("kfiframe").style.width = hz6d$("kfivtwin").clientWidth + 0 + "px";
          hz6d$("kfiframe").style.height = hz6d$("kfivtwin").clientHeight + 0 + "px";
          hz6d$("kfiframe").style.position = "absolute";
					if(how_float==1 && hasdoctype) hz6d$("kfiframe").style.position = "fixed";
          hz6d$("kfiframe").style.filter = "alpha(opacity=1)";
          hz6d$("kfiframe").style.display = "";
        }catch(e){}

        var openurl = "http://www.tgjy.cn/53.htm?arg=tgjy&style=1&kf=&kflist=off&kf=&zdkf_type=1&language=cn&charset=gbk&username=&userinfo=&introurl=&lyurl=&lytype=0&copartner=&referer=http%3A%2F%2Fwww.tgjy.cn%2F&keyword=&brief=&logo=&question=&tfrom=2" + force_kf;
        if(man_content!=""){
          try{hz6d$("hz6d_acc_content").innerHTML = man_content.replace(/\"/g, '&quot;').replace(/\'/g, '&#039;').replace(/</g, '&lt;').replace(/>/g, '&gt;');}catch(e){}
          man_content = "";
        }else{
          try{hz6d$("hz6d_acc_content").innerHTML = acc_content;}catch(e){}
        }
        try{
					var isNew = hz6d_ivt_tpl.indexOf("new2011");
					if(zdyivt==1 || isNew>0){
            var zdyIds = document.getElementsByTagName("div");
            for(var i=0; i<zdyIds.length; i++){
              if(zdyIds[i].id=="hz6d_53kf_invite_acc"){
                zdyIds[i].onclick = function(){onliner_zdfq=2;window.open(openurl,"_blank","height=473,width=703,top=200,left=200,status=yes,toolbar=no,menubar=no,resizable=yes,scrollbars=no,location=no,titlebar=no");hidden_ivt();}
              }
            }
          }else{
            hz6d$("hz6d_53kf_invite_acc").onclick = function(){onliner_zdfq=2;window.open(openurl,"_blank","height=473,width=703,top=200,left=200,status=yes,toolbar=no,menubar=no,resizable=yes,scrollbars=no,location=no,titlebar=no");hidden_ivt();}
          }
        }catch(e){}
        
        function hz6d_open_move(iconDivMain){
          var obj = hz6d$("kfivtwin");
          obj.style.display = "block";
          var obj_height = obj.offsetHeight;
          var obj_width = obj.offsetWidth;
          obj.style.display = "none";

          var tb_top = parseInt(iconDivMain.style.top.replace("px",""));
          var tb_left = parseInt(iconDivMain.style.left.replace("px",""));
          var tb_width = parseInt(iconDivMain.style.width.replace("px",""));
          var tb_height = parseInt(iconDivMain.style.height.replace("px",""));

          obj = hz6d$("kfivteffect");
          obj.style.top = tb_top + "px";
          obj.style.left = tb_left + "px";
          obj.style.height = tb_height + "px";
          obj.style.width = tb_width + "px";
          obj.style.display = "block";

          var moveHeight = tb_height;
          var moveWidth  = tb_width;
          var moveTop    = tb_top;
          var moveLeft   = tb_left;

          var offTop     = Math.abs(tb_top-ivtPosition.top);
          var offLeft    = Math.abs(tb_left-ivtPosition.left);

          var topStep    = offTop/(hz6d_effect_time/hz6d_effect_timer);
          var leftStep   = offLeft/(hz6d_effect_time/hz6d_effect_timer);

          var heightStep = (obj_height-tb_height)/(hz6d_effect_time/hz6d_effect_timer);
          var widthStep  = (obj_width-tb_width)/(hz6d_effect_time/hz6d_effect_timer);

          var topD = 1;
          if(tb_top-ivtPosition.top>0) { topD=-1; }
          var leftD = 1;
          if(tb_left-ivtPosition.left>0) { leftD=-1; }

          function dmove(){
            moveHeight += heightStep;
            moveWidth  += widthStep;
            moveTop    += topD*topStep;
            moveLeft   += leftD*leftStep;

            if(moveWidth>obj_width){
              obj.style.display = "none";
              clearInterval(iIntervalId);
              hz6d_showIvtWindow();
            }else{
              var ivtPosition_t = hz6d_getIvtPosition();
              obj.style.height = moveHeight + 'px';
              obj.style.width = moveWidth + 'px';
              obj.style.top = moveTop + (ivtPosition_t.top-ivtPosition.top) + 'px';
              obj.style.left = moveLeft + (ivtPosition_t.left-ivtPosition.left) + 'px';
            }
          }
          var iIntervalId = setInterval(dmove, hz6d_effect_timer);
          try{iconDivMain.style.display = "none";}catch(e){}
        }
        
        if(hz6d_ivt_effect==1 && hz6d_kf_type==2 && hz6d_pos_model==1 && hz6d_hidden==0){
          hz6d_checkIconDivMain();
        }else{
          hz6d_showIvtWindow();
        }

        function hz6d_showIvtWindow(){
          var ivtPosition_t = hz6d_getIvtPosition();
					if(how_float==1) var ivtPosition_t = hz6d_getIvtFixedPosition();
          hz6d_setIvtTop(ivtPosition_t.top);
          hz6d_setIvtLeft(ivtPosition_t.left);
          hz6d$("kfivtwin").style.display = "block";
          hz6d_initScrollPosition();
          hz6d_showFreeze();
          hz6d_startScrollTimer();
        }
        function hz6d_setIvtTop(top){
          hz6d$("kfivtwin").style.top = top + "px";
          hz6d$("kfiframe").style.top = top + "px";
        }
        function hz6d_setIvtLeft(left){
          hz6d$("kfivtwin").style.left = left + "px";
          hz6d$("kfiframe").style.left = left + "px";
        }
        function hz6d_initScrollPosition(){
          var scrollPosition = hz6d_getScrollPosition();
          ivt_top = scrollPosition.sTop;
          ivt_left = scrollPosition.sLeft;
        }
        function hz6d_checkIconDivMain(){
          var iconDivMain = hz6d$("iconDivMain"+kf_icon_id);
          if(iconDivMain!=null){
						if(hz6d_close_icon==0){
							hz6d_open_move(iconDivMain);
						}else{
							hz6d_showIvtWindow();
						}
          }else{
            setTimeout(hz6d_checkIconDivMain, 100);
          }
        }
        function hz6d_startScrollTimer(){
          if(ivt_timer==0 && how_float!=1){
            if(browser=="360" || browser=="TheWorld"){
              ivt_timer = window.setInterval("ivt_autoScroll()", 500);
            }else{
              ivt_timer = window.setInterval("ivt_autoScroll()", 10);
            }
          }
        }

				var posX;
				var posY;
				fdiv = hz6d$("kfivtwin");
				hz6d$("acc_title").onmousedown=function(e){
					if(!e) e = window.event;   //如果是IE 
					posX = e.clientX - parseInt(fdiv.style.left);
					posY = e.clientY - parseInt(fdiv.style.top);
					document.onmousemove = mousemove;          
				}
				document.onmouseup = function(){
					document.onmousemove = null;
				}
				function mousemove(ev){
					if(ev==null) ev = window.event;//如果是IE 
					fdiv.style.left = (ev.clientX - posX) + "px";
					fdiv.style.top = (ev.clientY - posY) + "px";
					ivt_top = Math.max(document.body.scrollTop,document.documentElement.scrollTop);
					ivt_left = Math.max(document.body.scrollLeft,document.documentElement.scrollLeft);
					
					// if(ivt_top==0) { ivt_top = document.documentElement.scrollTop; }
					// if(ivt_left==0) { ivt_left = document.documentElement.scrollLeft; }
				}
      }

      function hidden_ACCWindow(){
        function hz6d_close_move(iconDivMain){
          var obj = hz6d$("kfivtwin");
          var obj_height = obj.offsetHeight;
          var obj_width = obj.offsetWidth;
          var ivtPosition = {top:obj.offsetTop,left:obj.offsetLeft};
					if(how_float==1) var ivtPosition = hz6d_getIvtPosition();
          obj.style.display = "none";

          var tb_top = parseInt(iconDivMain.style.top.replace("px",""));
          var tb_left = parseInt(iconDivMain.style.left.replace("px",""));
          var tb_width = parseInt(iconDivMain.style.width.replace("px",""));
          var tb_height = parseInt(iconDivMain.style.height.replace("px",""));

          obj = hz6d$("kfivteffect");
          obj.style.top = ivtPosition.top + "px";
          obj.style.left = ivtPosition.left + "px";
          obj.style.height = obj_height + "px";
          obj.style.width = obj_width + "px";
          obj.style.display = "block";

          var moveHeight = obj_height;
          var moveWidth  = obj_width;
          var moveTop    = ivtPosition.top;
          var moveLeft   = ivtPosition.left;

          var offTop     = Math.abs(tb_top-ivtPosition.top);
          var offLeft    = Math.abs(tb_left-ivtPosition.left);

          var topStep    = offTop/(hz6d_effect_time/hz6d_effect_timer);
          var leftStep   = offLeft/(hz6d_effect_time/hz6d_effect_timer);

          var heightStep = (obj_height-tb_height)/(hz6d_effect_time/hz6d_effect_timer);
          var widthStep  = (obj_width-tb_width)/(hz6d_effect_time/hz6d_effect_timer);

          var topD = 1;
          if(tb_top-ivtPosition.top>0) { topD=-1; }
          var leftD = 1;
          if(tb_left-ivtPosition.left>0) { leftD=-1; }

          ivtPosition = hz6d_getIvtPosition();
          function dmove()
          {
            moveHeight -= heightStep;
            moveWidth  -= widthStep;
            moveTop    -= topD*topStep;
            moveLeft   -= leftD*leftStep;

            if(moveWidth<tb_width){
              obj.style.display = "none";
              try{iconDivMain.style.display = "block";}catch(e){}
              clearInterval(iIntervalId);
              hz6d_startReautoTimer();
            }else{
              var ivtPosition_t = hz6d_getIvtPosition();
              obj.style.height = moveHeight + 'px';
              obj.style.width = moveWidth + 'px';
              obj.style.top = moveTop + (ivtPosition_t.top-ivtPosition.top) + 'px';
              obj.style.left = moveLeft + (ivtPosition_t.left-ivtPosition.left) + 'px';
            }
          }
          var iIntervalId = setInterval(dmove, hz6d_effect_timer);
        }
        if(hz6d_ivt_effect==1 && hz6d_kf_type==2 && hz6d_pos_model==1 && hz6d_hidden==0){
          var iconDivMain = hz6d$("iconDivMain"+kf_icon_id);
					if(hz6d_close_icon==0){
						hz6d_close_move(iconDivMain);
					}else{
						hz6d$("kfivtwin").style.display = "none";
						hz6d_startReautoTimer();
					}
        }else{
          hz6d$("kfivtwin").style.display = "none";
          hz6d_startReautoTimer();
        }
      }

      function hz6d_startReautoTimer(){
        if(acc_reauto==1) { setTimeout("hz6d_checkIvt()", acc_reauto_time); }
      }

			// get ivt fixed position 
      function hz6d_getIvtFixedPosition(){
        var clientRect = hz6d_getClientWindow();

        if(ivt_height=="auto") { ivt_height="200"; }
        if(zdyivt==1){
          ivt_width = zdyivt_width.replace("px","");
          ivt_height = zdyivt_height.replace("px","");
        }
        if(acc_middle==1){
          acc_lr = 1;
          acc_tb = 1;
          acc_left = (clientRect.width-ivt_width)/2;
          acc_top = (clientRect.height-ivt_height)/2;
        }

        if(acc_lr==2){
          var ivt_left_init = clientRect.width - acc_left - ivt_width;
        }else{
          var ivt_left_init = acc_left;
        }
        if(acc_tb==2){
          var ivt_top_init = clientRect.height - acc_top - ivt_height;
        }else{
          var ivt_top_init = acc_top;
        }
        return {top:ivt_top_init, left:ivt_left_init};
      }

      // get ivt position 
      function hz6d_getIvtPosition(){
        var clientRect = hz6d_getClientWindow();

        if(ivt_height=="auto") { ivt_height="200"; }
        if(zdyivt==1){
          ivt_width = zdyivt_width.replace("px","");
          ivt_height = zdyivt_height.replace("px","");
        }
        if(acc_middle==1){
          acc_lr = 1;
          acc_tb = 1;
          acc_left = (clientRect.width-ivt_width)/2;
          acc_top = (clientRect.height-ivt_height)/2;
        }

        var scrollPosition = hz6d_getScrollPosition();
        if(acc_lr==2){
          var ivt_left_init = scrollPosition.sLeft + clientRect.width - acc_left - ivt_width;
        }else{
          var ivt_left_init = acc_left + scrollPosition.sLeft;
        }
        if(acc_tb==2){
          var ivt_top_init = clientRect.height + scrollPosition.sTop - acc_top - ivt_height;
        }else{
          var ivt_top_init = acc_top + scrollPosition.sTop;
        }
        return {top:ivt_top_init, left:ivt_left_init};
      }
      
      // get scroll position 
      function hz6d_getScrollPosition(){
        var s_top = document.body.scrollTop;
        var s_left = document.body.scrollLeft;
        if(s_left==0) { s_left=document.documentElement.scrollLeft; }
        if(s_top==0) { s_top=document.documentElement.scrollTop; }
        return {sTop:s_top, sLeft:s_left};
      }

      // get client width height 
      function hz6d_getClientWindow(){
        var clientWidth = 0;
        var clientHeight = 0;
        if(document.documentElement && document.documentElement.scrollTop){ 
          clientWidth = document.documentElement.clientWidth; 
          clientHeight = document.documentElement.clientHeight; 
        }else if(document.body){
          clientWidth = document.body.clientWidth;
          clientHeight = document.body.clientHeight;
        }
        if(hasdoctype){
          clientHeight = document.documentElement.clientHeight;
          clientWidth = document.documentElement.clientWidth;
        }
        return {width:clientWidth, height:clientHeight};
      }
      
      // old client height width 
      var hz6d_oldClient = hz6d_getClientWindow();
      function ivt_autoScroll(){
        var scrollPosition = hz6d_getScrollPosition();
        // new client height width 
        var hz6d_newClient = hz6d_getClientWindow();

        var hz6d_kfivtwin = hz6d$("kfivtwin");
        var hz6d_kfiframe = hz6d$("kfiframe");
        
        // top change 
        if(scrollPosition.sTop!=ivt_top || hz6d_oldClient.height!=hz6d_newClient.height){
          if(scrollPosition.sTop!=ivt_top){
            if(browser=="360" || browser=="TheWorld"){
						  ivt_top = scrollPosition.sTop;
            }else{
              ivt_top = smoothMove(ivt_top, scrollPosition.sTop);
            }
					}
					if(hz6d_oldClient.height!=hz6d_newClient.height){
            if(browser=="360" || browser=="TheWorld"){
						  hz6d_oldClient.height = hz6d_newClient.height;
            }else{
              hz6d_oldClient.height = smoothMove(hz6d_oldClient.height, hz6d_newClient.height);
            }
					}
          var hz6d_ivt_top = 0;
          if(acc_tb==2){
            hz6d_ivt_top = hz6d_oldClient.height - acc_top - ivt_height + ivt_top;
          }else{
            hz6d_ivt_top = acc_top + ivt_top;
          }

          if(browser=="360" || browser=="TheWorld"){
            if(hz6d_kfivtwin.style.display=="none"){
              hz6d_recover = false;
            }else{
              hz6d_recover = true;
              hz6d_kfivtwin.style.display = "none";
              try{
                hz6d_kfiframe.style.display = "none";
              }catch(e){}
            }
            hz6d_kfivtwin.style.top = hz6d_ivt_top+"px";
            try{
              hz6d_kfiframe.style.top = hz6d_ivt_top+"px";
            }catch(e){}
            if(hz6d_recover==true){
              hz6d_kfivtwin.style.display = "block";
              try{
                hz6d_kfiframe.style.display = "block";
              }catch(e){}
            }
          }else{
            hz6d_kfivtwin.style.top = hz6d_ivt_top+"px";
            try{
              hz6d_kfiframe.style.top = hz6d_ivt_top+"px";
            }catch(e){}
          }
        }
        
        // left change 
        if(scrollPosition.sLeft!=ivt_left || hz6d_oldClient.width!=hz6d_newClient.width){
          if(scrollPosition.sLeft!=ivt_left){
            if(browser=="360" || browser=="TheWorld"){
						  ivt_left = scrollPosition.sLeft;
            }else{
              ivt_left = smoothMove(ivt_left, scrollPosition.sLeft);
            }
					}
					if(hz6d_oldClient.width!=hz6d_newClient.width){
            if(browser=="360" || browser=="TheWorld"){
						  hz6d_oldClient.width = hz6d_newClient.width;
            }else{
              hz6d_oldClient.width = smoothMove(hz6d_oldClient.width, hz6d_newClient.width);
            }
					}
          var hz6d_ivt_left = 0;
          if(acc_lr==2){
            hz6d_ivt_left = ivt_left + hz6d_oldClient.width - acc_left - ivt_width;
          }else{
            hz6d_ivt_left = acc_left + ivt_left;
          }
          
          if(browser=="360" || browser=="TheWorld"){
            if(hz6d_kfivtwin.style.display=="none"){
              hz6d_recover = false;
            }else{
              hz6d_recover = true;
              hz6d_kfivtwin.style.display = "none";
              try{
                hz6d_kfiframe.style.display = "none";
              }catch(e){}
            }
            hz6d_kfivtwin.style.left = hz6d_ivt_left+"px";
            try{
              hz6d_kfiframe.style.left = hz6d_ivt_left+"px";
            }catch(e){}
            if(hz6d_recover==true){
              hz6d_kfivtwin.style.display = "block";
              try{
                hz6d_kfiframe.style.display = "block";
              }catch(e){}
            }
          }else{
            hz6d_kfivtwin.style.left = hz6d_ivt_left+"px";
            try{
              hz6d_kfiframe.style.left = hz6d_ivt_left+"px";
            }catch(e){}
          }
        }
      }

      if(0==0 && "off"=="on"){
				setTimeout("hz6d_checkIvt()", 500);
      }