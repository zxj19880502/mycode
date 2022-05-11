<%@ page contentType="text/html;charset=utf-8" language="java" errorPage="" %>
<script language="JavaScript" src="mydate.js"></script>
<form style=" border: 2px solid #dddd;width: 47%;padding-bottom:20px;padding-top:20px;" id="form1" name="form1" method="get" action="time.jsp">
  
  <label>开始日期</label>
   <label>
   

    <input type="text" id="time" name="time" onfocus="MyCalendar.SetDate(this)" value="">
    </label>
     <label>开始时间
   
     <SELECT NAME="day" style=" width:175px">
    
<option  value="00">00</option>
<option  value="01">01</option>
<option  value="02">02</option>
<option  value="03">03</option>
<option  value="04">04</option>
<option  value="05">05</option>
<option  value="06">06</option>
<option  value="07">07</option>
<option  value="08">08</option>
<option  value="09">09</option>
<option  value="10">10</option>
<option  value="11">11</option>
<option  value="12">12</option>
<option  value="13">13</option>
<option  value="14">14</option>
<option  value="15">15</option>
<option  value="16">16</option>
<option  value="17">17</option>
<option  value="18">18</option>
<option  value="19">19</option>
<option  value="20">20</option>
<option  value="21">21</option>
<option  value="22">22</option>
<option  value="23">23</option>
<option  value="24">24</option>

</SELECT>
    </label> 
    
    <br><br>
    <label>截止日期</label>
   <label>
    
    <input type="text" id="endtime" name="endtime" onfocus="MyCalendar.SetDate(this)" value="">
    </label>
     <label>截止时间
   
     <SELECT NAME="endday" style=" width:175px">
    
<option  value="00">00</option>
<option  value="01">01</option>
<option  value="02">02</option>
<option  value="03">03</option>
<option  value="04">04</option>
<option  value="05">05</option>
<option  value="06">06</option>
<option  value="07">07</option>
<option  value="08">08</option>
<option  value="09">09</option>
<option  value="10">10</option>
<option  value="11">11</option>
<option  value="12">12</option>
<option  value="13">13</option>
<option  value="14">14</option>
<option  value="15">15</option>
<option  value="16">16</option>
<option  value="17">17</option>
<option  value="18">18</option>
<option  value="19">19</option>
<option  value="20">20</option>
<option  value="21">21</option>
<option  value="22">22</option>
<option  value="23">23</option>
<option  value="24">24</option>


</SELECT>
    </label>
    
    
    <label>
    &nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" id="button" value="查询" />
    </label>
    
    </form>
    
    
  <br><br>
  
  
  <form style="border: 2px solid #dddd;width: 47%;padding-bottom:20px;padding-top:20px;" id="form2" name="form2" method="get" action="test.jsp">
  
  <label>工单查询</label>
   <label>
   
 
    <input type="text" id="workorder" name="workorder"  value="">
    </label>


    <label>
    &nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" id="button" value="查询" />
    </label>
  

    
</form>


  <br><br>


<form style="border: 2px solid #dddd;width: 47%;padding-bottom:20px;padding-top:20px;"  id="form3" name="form3" method="get" action="line.jsp">
  
  <label>开始日期</label>
   <label>
   
 
    <input type="text" id="time" name="time" onfocus="MyCalendar.SetDate(this)" value="">
    </label>
     <label>开始时间
   
     <SELECT NAME="day" style=" width:175px">
    
<option  value="00">00</option>
<option  value="01">01</option>
<option  value="02">02</option>
<option  value="03">03</option>
<option  value="04">04</option>
<option  value="05">05</option>
<option  value="06">06</option>
<option  value="07">07</option>
<option  value="08">08</option>
<option  value="09">09</option>
<option  value="10">10</option>
<option  value="11">11</option>
<option  value="12">12</option>
<option  value="13">13</option>
<option  value="14">14</option>
<option  value="15">15</option>
<option  value="16">16</option>
<option  value="17">17</option>
<option  value="18">18</option>
<option  value="19">19</option>
<option  value="20">20</option>
<option  value="21">21</option>
<option  value="22">22</option>
<option  value="23">23</option>
<option  value="24">24</option>

</SELECT>
    </label> 
    
    <br><br>
    <label>截止日期</label>
   <label>
    
    <input type="text" id="endtime" name="endtime" onfocus="MyCalendar.SetDate(this)" value="">
    </label>
     <label>截止时间
   
     <SELECT NAME="endday" style=" width:175px">
    
<option  value="00">00</option>
<option  value="01">01</option>
<option  value="02">02</option>
<option  value="03">03</option>
<option  value="04">04</option>
<option  value="05">05</option>
<option  value="06">06</option>
<option  value="07">07</option>
<option  value="08">08</option>
<option  value="09">09</option>
<option  value="10">10</option>
<option  value="11">11</option>
<option  value="12">12</option>
<option  value="13">13</option>
<option  value="14">14</option>
<option  value="15">15</option>
<option  value="16">16</option>
<option  value="17">17</option>
<option  value="18">18</option>
<option  value="19">19</option>
<option  value="20">20</option>
<option  value="21">21</option>
<option  value="22">22</option>
<option  value="23">23</option>
<option  value="24">24</option>


</SELECT>
    </label>
     <label>线别
   
     <SELECT NAME="line" style=" width:175px">
    
<option  value="LED_L01">LED_L01</option>
<option  value="LED_L02">LED_L02</option>
<option  value="LED_L03">LED_L03</option>
<option  value="LED_L04">LED_L04</option>
<option  value="LED_L05">LED_L05</option>
<option  value="LED_L06">LED_L06</option>
<option  value="LED_L07">LED_L07</option>
<option  value="LED_L08">LED_L08</option>
<option  value="LED_L09">LED_L09</option>
<option  value="LED_S01">LED_S01</option>
<option  value="LED_S02">LED_S02</option>
<option  value="LED_S03">LED_S03</option>
<option  value="LED_S04">LED_S04</option>
<option  value="LED_S05">LED_S05</option>
<option  value="LED_S06">LED_S06</option>
<option  value="LED_TP1">LED_TP1</option>
<option  value="LED_TP2">LED_TP2</option>
<option  value="LED_TP3">LED_TP3</option>
<option  value="LED_W01">LED_W01</option>
<option  value="LED_W02">LED_W02</option>
<option  value="LED_W03">LED_W03</option>
<option  value="LED_W04">LED_W04</option>
<option  value="LED_W05">LED_W05</option>
<option  value="LED_W06">LED_W06</option>
<option  value="LED_W07">LED_W07</option>
<option  value="LED_W08">LED_W08</option>
<option  value="LED_W09">LED_W09</option>
<option  value="LED_W10">LED_W10</option>
<option  value="LED_W11">LED_W11</option>
<option  value="LED_W12">LED_W12</option>
<option  value="LED_W13">LED_W13</option>
<option  value="LED_W14">LED_W14</option>
<option  value="LED_W15">LED_W15</option>
<option  value="LED_W16">LED_W16</option>
<option  value="LED_S99">LED_S99</option>
<option  value="LED_L99">LED_L99</option>
<option  value="LED_W99">LED_W99</option>
<option  value="LED_T99">LED_T99</option>
</SELECT>
    </label> 
    
    
    <label>
    &nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" id="button" value="查询" />
    </label>
    
    </form>






