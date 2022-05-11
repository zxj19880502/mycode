<!DOCTYPE html>
<%@ page contentType="text/html;charset=utf-8" language="java" errorPage="" %>
 <%@ page import="java.text.*"%>
<%@ page import="java.sql.*" %>
 <%@page import="java.util.*"%>
<html>
<html lang="en" class="no-js">

    <head>
<meta name="viewport" content="width=device-width,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
       
        <title>数据提交</title>
     

        <!-- CSS -->
        <link rel="stylesheet" href="assets/css/reset.css">
        <link rel="stylesheet" href="assets/css/supersized.css">
        <link rel="stylesheet" href="assets/css/stylee.css">

	<script type="text/javascript">
		function mqa(){
			var datatime1=window.document.getElementById("datatime1").value;
			
			
		
			if (datatime1 == ""){
				window.alert("请选择日期");
				return false;
			}
	
			
			return true;
		} 
	</script>	
<script type="text/javascript">
		function ooba(){
			var datatime2=window.document.getElementById("datatime2").value;
			
			
		
			if (datatime2 == ""){
				window.alert("请选择日期");
				return false;
			}
	
			
			return true;
		} 
	</script>
	<script type="text/javascript">
		function qhold(){
			var datatime=window.document.getElementById("datatime").value;
			
			
		
			if (datatime == ""){
				window.alert("请选择日期");
				return false;
			}
	
			
			return true;
		} 
	</script>
	
	
	
    </head>

    <body>

 

    
    
	<div  style="padding-top:10px;">
	 
    <table    style="position:absolute;width: 100%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;font-size:0.8em;height: 33%; ">
	<form style="padding-bottom:10px;padding-top:10px;" method="post"action="datadb.jsp"onsubmit="return mqa()"autocomplete="off">
	<tr><td style="width:20%;padding-right: 12%;">制一基础数据</td></tr>
      <tr>
	  <td style="width:9%;" >FAI：累计检查批数：</td>
        <td><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="jcps" id="jcps" class="username" value="0" onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		<td  style="width:9%;">累计不合格批数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="bhgps" id="bhgps" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
		<td style="width:12%;">异常比例：累计工单数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="gds" id="gds" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		<td style="width:9%;">累计不良件数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="bljs" id="bljs" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
      </tr>
      <tr>
	  
		<td style="width:9%;">HI-POT：累计投入数：</td>
        <td><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="trs" id="trs" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		<td style="width:9%;">累计不良数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="bls" id="bls" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
		
      </tr>
    <tr><td style="width:20%;padding-right: 12%;">制二基础数据</td></tr>
      <tr>
	  <td style="width:9%;">FAI：累计检查批数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="nonjcps" id="nonjcps" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		<td style="width:9%;">累计不合格批数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="nonbhgps" id="nonbhgps" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
		<td style="width:12%;">异常比例：累计工单数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="nongds" id="nongds" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		<td style="width:9%;">累计不良件数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="nonbljs" id="nonbljs" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>

      </tr>
      <tr>
	  
		<td style="width:9%;">HI-POT：累计投入数：</td>
        <td><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="nontrs" id="nontrs" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		<td style="width:9%;">累计不良数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="nonbls" id="nonbls" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
		<td style="width:9%;">日期：</td>
        <td ><input readonly="readonly" readonly="value"  onkeyup="value=value.replace(/[^\d{1,}\/\d{1,}|\d{1,}]/g,'')"  style="width:55%;" type="text" name="datatime1" id="datatime1" class="username"  onClick="WdatePicker({dateFmt:'yyyy/MM/dd'})" value="" ></td>
      </tr>
	<tr><td colspan="20"> <input  type="submit"  value="提交" /></td></tr>
	</form>
    </table>
  
	 <table   style="position:absolute;width: 100%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:0.8em;height: 22%;margin-top:17.5%; ">
	 <form style="padding-bottom:10px;padding-top:10px;" method="post"action="ooba.jsp"onsubmit="return ooba()"autocomplete="off">
	<tr><td style="width:20%;padding-right: 10%;">OOBA 制一 基础数据</td></tr>
      <tr>
	  
		<td style="width:10%;">累计送验数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:65%;" type="text" name="ljsys" id="ljsys" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
		<td style="width:10%;">累计抽样数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width: 55%;" type="text" name="ljcys" id="ljcys" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
		
		<td style="width:10%;">当日待检数量：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:65%;" type="text" name="drdjsl" id="drdjsl" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
		
		<td style="width:10%;">累计外观不良数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width: 55%;" type="text" name="wgbls" id="wgbls" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		<td style="width:10%;">累计电性不良数：</td>
        <td><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width: 55%;" type="text" name="dxbls" id="dxbls" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
        
		
		
      </tr>
	  <tr><td style="width:23%;padding-right: 10%;">OOBA 制二 基础数据</td></tr>
      <tr>
	  <td style="width:10%;">累计送验数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:65%;" type="text" name="nonljsys" id="nonljsys" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
		<td style="width:10%;">累计抽样数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width: 55%;" type="text" name="nonljcys" id="nonljcys" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
		
		<td style="width:10%;">当日待检数量：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:65%;" type="text" name="nondrdjsl" id="nondrdjsl" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		
		<td style="width:10%;">累计外观不良数：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width: 55%;" type="text" name="nonwgbls" id="nonwgbls" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		<td style="width:10%;">累计电性不良数：</td>
        <td><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width: 55%;" type="text" name="nondxbls" id="nondxbls" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
        
		</tr>
		<tr>
		<td style="width:7%;">日期：</td>
        <td ><input readonly="readonly" readonly="value"  onkeyup="value=value.replace(/[^\d{1,}\/\d{1,}|\d{1,}]/g,'')" style="width: 100%;" type="text" name="datatime2" id="datatime2" class="username" onClick="WdatePicker({dateFmt:'yyyy/MM/dd'})" value=""></td>
      </tr>
  <tr><td colspan="12"> <input  type="submit"  value="提交" /></td></tr>
   </form>
    </table>
	
	
	<table   style="position:absolute;width: 100%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:0.8em;height: 22%;margin-top:29.7%; ">
	<form style="padding-bottom:10px;padding-top:10px;" method="post"action="qhold.jsp"onsubmit="return qhold()"autocomplete="off">
	<tr><td style="width:20%;padding-right: 12%;">Q HOLD</td></tr>
      <tr>
	  <td style="width:10%;">机种：</td>
        <td ><input style="width:65%;" type="text" name="jz" id="jz" class="username" value=""></td>
		<td style="width:10%;">数量：</td>
        <td ><input onkeyup="value=value.replace(/[^\d{1,}\.\d{1,}|\d{1,}]/g,'')"  style="width:65%;" type="text" name="sl" id="sl" class="username" value="0"onfocus="if(this.value=='0'){this.value='';}" onblur="if(this.value==''){this.value='0';}"></td>
		<td style="width:10%;">HOLD原因：</td>
        <td><input style="width:65%;" type="text" name="holdyy" id="holdyy" class="username" value=""></td>
		<td style="width:10%;">分类：</td>
        <td ><input style="width:65%;" type="text" name="fl" id="fl" class="username" value=""></td>
        <td style="width:10%;">处理状态：</td>
        <td ><input style="width:65%;" type="text" name="clzt" id="clzt" class="username" value=""></td>
	  </tr>
		<tr>
		
		<td style="width:10%;">日期：</td>
        <td ><input readonly="readonly" readonly="value"  style="width:65%;" type="text" name="datatime" id="datatime" class="username" onClick="WdatePicker({dateFmt:'yyyy/MM/dd'})" value=""></td>
      </tr>
   <tr><td colspan="10"> <input  type="submit"  value="提交" /></td></tr>
    </form>
    </table>
	
   </div>
<script src="assets/js/jquery-1.8.2.min.js" ></script>
        <script src="assets/js/supersized.3.2.7.min.js" ></script>
        <script src="assets/js/supersized-init.js" ></script>
        <script src="assets/js/scripts.js" ></script>
<script language="javascript" type="text/javascript" src="My97DatePicker/WdatePicker.js"></script>
    </body>
<div style="text-align:center;margin-top:42%;margin-left:15%;border: 1px solid #ebebeb;width: 70%;padding-bottom:12px;padding-top:10px;">
<table>
<form   action="fai.jsp"method="post"autocomplete="off" >
  
  <label>FAI数据看板 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;开始日期</label>
   <label>
   

    <input  readonly="readonly" readonly="value"  style="width:16%;" type="text" id="time" name="time" onclick="WdatePicker({minDate:'%y/{%M-1}/01',maxDate:'%y/%M/%ld'})"  value="">
    </label>
    
    <label>截止日期</label>
   <label>
    
    <input readonly="readonly" readonly="value"  style="width:16%;" type="text" id="endtime" name="endtime" onclick="WdatePicker({minDate:'%y/{%M-1}/01',maxDate:'%y/%M/%ld'})" value="">
    </label>
        
    <label>
    &nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" id="button" value="FAI数据看板" />
    </label>
    
    </form>
    </table>
</div>
<div style="text-align:center;margin-top:3%;margin-left:15%;border: 1px solid #ebebeb;width: 70%;padding-bottom:12px;padding-top:10px;">
<table>
<form   action="oobak.jsp"method="post"autocomplete="off" >
  
  <label>OOBA数据看板 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;开始日期</label>
   <label>
   

    <input  readonly="readonly" readonly="value"  style="width:16%;" type="text" id="time" name="time" onclick="WdatePicker({minDate:'%y/{%M-1}/01',maxDate:'%y/%M/%ld'})"  value="">
    </label>
    
    <label>截止日期</label>
   <label>
    
    <input readonly="readonly" readonly="value"  style="width:16%;" type="text" id="endtime" name="endtime" onclick="WdatePicker({minDate:'%y/{%M-1}/01',maxDate:'%y/%M/%ld'})" value="">
    </label>
        
    <label>
    &nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" id="button" value="OOBA数据看板" />
    </label>
    
    </form>
    </table>
</div>
<div style="text-align:center;margin-top:3%;margin-left:15%;border: 1px solid #ebebeb;width: 70%;padding-bottom:12px;padding-top:10px;">
<table>
<form   action="qholdd.jsp"method="post"autocomplete="off" >
  
  <label>待验 Q HOLD &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;开始日期</label>
   <label>
   

    <input  readonly="readonly" readonly="value"  style="width:16%;" type="text" id="time" name="time" onclick="WdatePicker({minDate:'%y/{%M-1}/01',maxDate:'%y/%M/%ld'})"  value="">
    </label>
    
    <label>截止日期</label>
   <label>
    
    <input readonly="readonly" readonly="value"  style="width:16%;" type="text" id="endtime" name="endtime" onclick="WdatePicker({minDate:'%y/{%M-1}/01',maxDate:'%y/%M/%ld'})" value="">
    </label>
        
    <label>
    &nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" id="button" value="待验 Q HOLD" />
    </label>
    
    </form>
    </table>
</div>
</html>

