<!DOCTYPE html>

<html>
<html lang="en" class="no-js">

    <head>
<meta name="viewport" content="width=device-width,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
       
        <title>数据提交</title>
     

        <!-- CSS -->
        <link rel="stylesheet" href="assets/css/reset.css">
        <link rel="stylesheet" href="assets/css/supersized.css">
        <link rel="stylesheet" href="assets/css/stylee.css">

	
	
	
    </head>

    <body>

 

  
<script src="assets/js/jquery-1.8.2.min.js" ></script>
        <script src="assets/js/supersized.3.2.7.min.js" ></script>
        <script src="assets/js/supersized-init.js" ></script>
        <script src="assets/js/scripts.js" ></script>
<script language="javascript" type="text/javascript" src="My97DatePicker/WdatePicker.js"></script>
    
<div style="text-align:center;margin:15% auto;border: 1px solid #ebebeb;width: 80%;padding-bottom:12px;padding-top:15px;">
<table style="text-align:center;margin:1% auto;width: 80%;padding-bottom:15px;padding-top:12px;">
<form   action="fai.jsp"method="post"autocomplete="off" >
  
  <label>制程数据看板 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;开始日期</label>
   <label>
   

    <input  readonly="readonly" readonly="value"  style="width:16%;" type="text" id="time" name="time" onclick="WdatePicker({minDate:'%y/{%M-1}/01',maxDate:'%y/%M/%ld'})"  value="">
    </label>
    
    <label>截止日期</label>
   <label>
    
    <input readonly="readonly" readonly="value"  style="width:16%;" type="text" id="endtime" name="endtime" onclick="WdatePicker({minDate:'%y/{%M-1}/01',maxDate:'%y/%M/%ld'})" value="">
    </label>
        
    <label>
    <SELECT NAME="day" id="day" style=" width:80px;background: #fff;opacity:0.5;">
      <option value="yyyy/mm/dd" >天</option>
      <option value="iw" >周</option>
      <option value="yyyy/mm" >月</option>
      <option value="q" >季度</option>
      <option value="yyyy" >年</option>
    </select>
    &nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" id="button" value="制程数据看板" />
    </label>
    
    </form>
    </table>

<table style="text-align:center;margin:1% auto;width: 80%;padding-bottom:15px;padding-top:14px;">
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
    <SELECT NAME="day" id="day" style=" width:80px;background: #fff;opacity:0.5;">
      <option value="yyyy/mm/dd" >天</option>
      <option value="iw" >周</option>
      <option value="yyyy/mm" >月</option>
      <option value="q" >季度</option>
      <option value="yyyy" >年</option>
    </select>
    <tr>
   
    &nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" id="button" value="OOBA数据看板" />
    </label>
    
    </form>
    </table>

<table style="text-align:center;margin:1% auto;width: 80%;padding-bottom:15px;padding-top:14px;">
<form   action="qholdd.jsp"method="post"autocomplete="off" >
  
  <label>Q HOLD看板 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;开始日期</label>
   <label>
   

    <input  readonly="readonly" readonly="value"  style="width:16%;" type="text" id="time" name="time" onclick="WdatePicker({minDate:'%y/{%M-1}/01',maxDate:'%y/%M/%ld'})"  value="">
    </label>
    
    <label>截止日期</label>
   <label>
    
    <input readonly="readonly" readonly="value"  style="width:16%;" type="text" id="endtime" name="endtime" onclick="WdatePicker({minDate:'%y/{%M-1}/01',maxDate:'%y/%M/%ld'})" value="">
    </label>
        
    <label>
    
 统计方式：<SELECT NAME="day" id="day" style=" width:80px;background: #fff;opacity:0.5;">
      <option value="yyyy/mm/dd" >天</option>
      <option value="iw" >周</option>
      <option value="yyyy/mm" >月</option>
      <option value="q" >季度</option>
      <option value="yyyy" >年</option>
    </select>
     <br>机种：
        <input style="width:15%;" type="text" name="zjmc" id="zjmc" class="username" value="">
       
        处理状态：<SELECT NAME="ztzt" id="ztzt"  style=" width:80px;background: #fff;opacity:0.5;">
        
      <option value="待重工" >待重工</option>
      <option value="重工中" >重工中</option>
      <option value="待处理" >待处理</option>
      <option value="特采" >特采</option>
      <option value="Waive" >Waive</option>
    </select>
    
    &nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" id="button" value="Q HOLD查询" style="margin-top:1%"/>
    </label>
    
    </form>
    </table>
</div>
</body>
</html>

