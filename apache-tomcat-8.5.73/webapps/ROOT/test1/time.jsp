<%@ page contentType="text/html;charset=utf-8" language="java" errorPage="" %>
 <%@ page import="java.text.*"%>
<%@ page import="java.sql.*" %>
 <%@page import="java.util.*"%>



<meta http-equiv="refresh" content="300">

<html>
 

 
<head>
 
  <title>时间查询</title>
 <script type="text/javascript">  
      function exportExcel(){  
          window.open('time.jsp?exportToExcel=YES');  
      }  
 </script> 

 
<style type="text/css">
#container {
    height: 70%;
}

.highcharts-figure,
.highcharts-data-table table {
  
    margin: 1em auto;
}

#datatable {
    font-family: Verdana, sans-serif;
    border-collapse: collapse;
    border: 1px solid #ebebeb;
   
    text-align: center;
    font-size:11px;
    
}



#datatable td,
#datatable th,
#datatable caption {
    padding: 0.1em;
}

#datatable thead tr,
#datatable tr:nth-child(even) {
    background: #f8f8f8;
}

#datatable tr:hover {
    background: #fe99d1;
}

		</style>
</head>
 <body >
 
 




<%

Class.forName("oracle.jdbc.driver.OracleDriver");
 
Connection connection=DriverManager.getConnection("jdbc:oracle:thin:@172.22.24.221:1521:ledmes1","sajet","tech");

Statement stmt=connection.createStatement();

Statement stmtc=connection.createStatement();
Statement cc=connection.createStatement();
Statement dd=connection.createStatement();

Statement hja=connection.createStatement();
Statement wip=connection.createStatement();

Statement nqc=connection.createStatement();
Statement dqc=connection.createStatement();

String path = request.getContextPath(); 
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/"; 
String starday = request.getParameter("day");//用request得到 
String startime = request.getParameter("time");//用request得到 
String endday = request.getParameter("endday");//用request得到 
String endtime = request.getParameter("endtime");//用request得到
String datetime = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(Calendar.getInstance().getTime());//系统时间变量
ResultSet rs =stmt.executeQuery("SELECT PROCESS_NAME ,sum(nvl(LED_TP1,'0')) LED_TP1,sum(nvl(LED_TP2,'0')) LED_TP2,sum(nvl(LED_TP3,'0')) LED_TP3,sum(nvl(LED_S01,'0')) LED_S01,sum(nvl(LED_S02,'0')) LED_S02,sum(nvl(LED_S03,'0')) LED_S03,sum(nvl(LED_S04,'0')) LED_S04,sum(nvl(LED_S05,'0')) LED_S05,sum(nvl(LED_S06,'0')) LED_S06,sum(nvl(LED_L01,'0')) LED_L01,sum(nvl(LED_L02,'0')) LED_L02,sum(nvl(LED_L03,'0')) LED_L03,sum(nvl(LED_L04,'0')) LED_L04,sum(nvl(LED_L05,'0')) LED_L05,sum(nvl(LED_L06,'0')) LED_L06,sum(nvl(LED_L07,'0')) LED_L07,sum(nvl(LED_L08,'0')) LED_L08,sum(nvl(LED_L09,'0')) LED_L09,sum(nvl(LED_W01,'0')) LED_W01,sum(nvl(LED_W02,'0')) LED_W02,sum(nvl(LED_W03,'0')) LED_W03,sum(nvl(LED_W04,'0')) LED_W04,sum(nvl(LED_W05,'0')) LED_W05,sum(nvl(LED_W06,'0')) LED_W06,sum(nvl(LED_W07,'0')) LED_W07,sum(nvl(LED_W08,'0')) LED_W08,sum(nvl(LED_W09,'0')) LED_W09,sum(nvl(LED_W10,'0')) LED_W10,sum(nvl(LED_W11,'0')) LED_W11,sum(nvl(LED_W12,'0')) LED_W12,sum(nvl(LED_W13,'0')) LED_W13,sum(nvl(LED_W14,'0')) LED_W14,sum(nvl(LED_W15,'0')) LED_W15,sum(nvl(LED_W16,'0')) LED_W16,sum(nvl(LED_S99,'0')) LED_S99,sum(nvl(LED_L99,'0')) LED_L99,sum(nvl(LED_W99,'0')) LED_W99,sum(nvl(LED_T99,'0')) LED_T99 from(SELECT PDLINE_NAME,PROCESS_NAME, decode(PDLINE_NAME,'LED_TP1',input)LED_TP1,decode(PDLINE_NAME,'LED_W10',input) LED_W10,decode(PDLINE_NAME,'LED_W16',input) LED_W16 ,decode(PDLINE_NAME,'LED_W01',input) LED_W01 ,decode(PDLINE_NAME,'LED_L05',input) LED_L05,decode(PDLINE_NAME,'LED_S01',input) LED_S01,decode(PDLINE_NAME,'LED_S02',input) LED_S02 ,decode(PDLINE_NAME,'LED_L02',input) LED_L02 ,decode(PDLINE_NAME,'LED_L08',input) LED_L08 ,decode(PDLINE_NAME,'LED_L04',input) LED_L04 ,decode(PDLINE_NAME,'LED_L09',input) LED_L09,decode(PDLINE_NAME,'LED_TP2',input) LED_TP2,decode(PDLINE_NAME,'LED_W03',input) LED_W03 ,decode(PDLINE_NAME,'LED_L03',input) LED_L03 ,decode(PDLINE_NAME,'LED_W07',input) LED_W07,decode(PDLINE_NAME,'LED_W08',input) LED_W08,decode(PDLINE_NAME,'LED_S05',input) LED_S05 ,decode(PDLINE_NAME,'LED_W05',input) LED_W05 ,decode(PDLINE_NAME,'LED_W04',input) LED_W04 ,decode(PDLINE_NAME,'LED_TP3',input) LED_TP3 ,decode(PDLINE_NAME,'LED_S99',input) LED_S99,decode(PDLINE_NAME,'LED_W02',input) LED_W02,decode(PDLINE_NAME,'LED_S04',input) LED_S04 ,decode(PDLINE_NAME,'LED_S03',input) LED_S03 ,decode(PDLINE_NAME,'LED_W09',input) LED_W09,decode(PDLINE_NAME,'LED_L01',input) LED_L01,decode(PDLINE_NAME,'LED_L07',input) LED_L07 ,decode(PDLINE_NAME,'LED_W11',input) LED_W11 ,decode(PDLINE_NAME,'LED_L99',input) LED_L99 ,decode(PDLINE_NAME,'LED_W12',input) LED_W12 ,decode(PDLINE_NAME,'LED_S06',input) LED_S06 ,decode(PDLINE_NAME,'LED_W06',input) LED_W06 ,decode(PDLINE_NAME,'LED_L06',input) LED_L06 ,decode(PDLINE_NAME,'LED_W13',input) LED_W13 ,decode(PDLINE_NAME,'LED_W14',input) LED_W14 ,decode(PDLINE_NAME,'LED_W15',input) LED_W15 ,decode(PDLINE_NAME,'LED_W99',input) LED_W99 ,decode(PDLINE_NAME,'LED_T99',input) LED_T99 from INPUT_QTYC  WHERE WORK_DATE||WORK_TIME between to_CHAR('"+startime+""+starday+"')and to_char('"+endtime+""+endday+"'))GROUP BY PROCESS_NAME ");
ResultSet hjb =hja.executeQuery("SELECT PROCESS_NAME ,sum(INPUT)AS INPUT,sum(PASS_QTY)AS PASS_QTY,sum(FAIL_QTY)AS fail, SUM(REPASS_QTY)AS REPASS,CONCAT(round(decode(SUM(PASS_QTY),0,0,(SUM(PASS_QTY)/(sum(input)))*100),2),'%')AS yeald FROM input_qtyc  WHERE WORK_DATE||WORK_TIME between to_CHAR('"+startime+""+starday+"')and to_char('"+endtime+""+endday+"')  GROUP BY PROCESS_NAME ");
ResultSet wips =wip.executeQuery("SELECT '合计'AS heji, sum(PASS_QTY+FAIL_QTY)AS INPUT,sum(PASS_QTY)AS PASS_QTY,sum(FAIL_QTY)AS fail, SUM(REPASS_QTY)AS REPASS,CONCAT(round(decode(SUM(PASS_QTY),0,0,(SUM(PASS_QTY)/(sum(PASS_QTY+FAIL_QTY)))*100),2),'%')AS yeald FROM G_SN_COUNT a LEFT join sajet.SYS_PROCESS b  on a.process_id = b.process_id LEFT join sajet.SYS_PDLINE c  on a.PDLINE_ID = c.PDLINE_ID WHERE WORK_DATE||WORK_TIME between to_CHAR('"+startime+""+starday+"')and to_char('"+endtime+""+endday+"')");

ResultSet rc =stmtc.executeQuery("SELECT * FROM (SELECT PDLINE_NAME,sum(PASS_QTY+FAIL_QTY)as input,sum(PASS_QTY)as good,SUM(FAIL_QTY)AS FAIL_QTY,CONCAT(round(decode(SUM(PASS_QTY),0,0,(SUM(PASS_QTY)/(sum(PASS_QTY+FAIL_QTY)))*100),2),'%')as Yield from(select * from sajet.G_SN_COUNT a  LEFT join sajet.SYS_PROCESS b  on a.process_id = b.process_id LEFT join sajet.SYS_PDLINE c  on a.PDLINE_ID = c.PDLINE_ID LEFT join sajet.G_WO_BASE d  on a.WORK_ORDER = d.WORK_ORDER WHERE A.WORK_DATE||A.WORK_TIME between to_CHAR('"+startime+""+starday+"')and to_char('"+endtime+""+endday+"') )GROUP BY PDLINE_NAME ORDER BY FAIL_QTY DESC ) ");
ResultSet rb =cc.executeQuery("SELECT distinct Defect_Code 不良代码,Defect_Desc 不良描述, SUMCOUNT 数量 FROM (SELECT F.Defect_Code , F.Defect_Desc ,SUM (A.DEFECT_QTY) SUMCOUNT FROM SAJET.G_SN_DEFECT A, SAJET.SYS_DEFECT F WHERE 1=1 and  A.REC_TIME >= (SYSDATE - 225)AND A.REC_TIME <  (SYSDATE) AND A.DEFECT_ID = F.DEFECT_ID AND  A.REC_TIME between TRUNC(SYSDATE) + 08/24 and TRUNC(SYSDATE) + 20/24 GROUP BY F.Defect_Code, F.Defect_Desc ORDER BY 3 DESC)WHERE ROWNUM <= 20");
ResultSet rf=dd.executeQuery("SELECT distinct Defect_Code 不良代码,Defect_Desc 不良描述, SUMCOUNT 数量 FROM (SELECT F.Defect_Code , F.Defect_Desc ,SUM (A.DEFECT_QTY) SUMCOUNT FROM SAJET.G_SN_DEFECT A, SAJET.SYS_DEFECT F WHERE 1=1 and  A.REC_TIME >= (SYSDATE - 225)AND A.REC_TIME <  (SYSDATE) AND A.DEFECT_ID = F.DEFECT_ID AND  A.REC_TIME between TRUNC(SYSDATE-1) + 20/24 and TRUNC(SYSDATE) + 08/24 GROUP BY F.Defect_Code, F.Defect_Desc ORDER BY 3 DESC)WHERE ROWNUM <= 20");

ResultSet nq=nqc.executeQuery("SELECT PDLINE_NAME 线别,MODEL_ID model,defect_desc 不良描述,SAMPLING_SIZE SAMPLING,FAIL_QTY 不良,PASS_QTY PASS,dppm FROM (SELECT D.PDLINE_NAME,A.MODEL_ID ,C.DEFECT_DESC,A.SAMPLING_SIZE ,A.FAIL_QTY,A.PASS_QTY,sum(FAIL_QTY/SAMPLING_SIZE*1000000)DPPM FROM G_QC_LOT A LEFT JOIN G_QC_SN_DEFECT B ON A.QC_LOTNO =B.QC_LOTNO LEFT JOIN SYS_DEFECT C ON B.DEFECT_ID =C.DEFECT_ID LEFT JOIN SYS_PDLINE D ON A.PDLINE_ID =D.PDLINE_ID WHERE END_TIME between TRUNC(SYSDATE-1) + 20/24 and TRUNC(SYSDATE) + 08/24 GROUP BY D.PDLINE_NAME,A.MODEL_ID ,C.DEFECT_DESC,A.SAMPLING_SIZE ,A.FAIL_QTY,A.PASS_QTY ORDER BY A.FAIL_QTY DESC )WHERE ROWNUM <= 20");
ResultSet dq=dqc.executeQuery("SELECT PDLINE_NAME 线别,MODEL_ID model,defect_desc 不良描述,SAMPLING_SIZE SAMPLING,FAIL_QTY 不良,PASS_QTY PASS ,dppm FROM (SELECT D.PDLINE_NAME,A.MODEL_ID ,C.DEFECT_DESC,A.SAMPLING_SIZE ,A.FAIL_QTY,A.PASS_QTY ,sum(FAIL_QTY/SAMPLING_SIZE*1000000) dppm FROM G_QC_LOT A LEFT JOIN G_QC_SN_DEFECT B ON A.QC_LOTNO =B.QC_LOTNO LEFT JOIN SYS_DEFECT C ON B.DEFECT_ID =C.DEFECT_ID LEFT JOIN SYS_PDLINE D ON A.PDLINE_ID =D.PDLINE_ID WHERE END_TIME between TRUNC(SYSDATE) + 08/24 and TRUNC(SYSDATE) + 20/24 GROUP BY D.PDLINE_NAME,A.MODEL_ID ,C.DEFECT_DESC,A.SAMPLING_SIZE ,A.FAIL_QTY,A.PASS_QTY ORDER BY A.FAIL_QTY DESC )WHERE ROWNUM <= 20");
%>
<tr><td><h3>数据更新时间：<%=datetime %>&nbsp;&nbsp;&nbsp;&nbsp;<button type="button" onclick="tableToExcel('datatable','Operation线<%=datetime %>')">Operation线导出</button>
  <button type="button" onclick="tableToExcel('cd','Operation站<%=datetime %>')">Operation站导出</button>
  <button type="button" onclick="tableToExcel('he','Operation合<%=datetime %>')">Operation合导出</button>
  <button type="button" onclick="tableToExcel('er','PDLINE<%=datetime %>')">PDLINE导出</button>
  <button type="button" onclick="tableToExcel('blb','不良白<%=datetime %>')">不良白导出</button>
  <button type="button" onclick="tableToExcel('two','不良夜<%=datetime %>')">不良夜导出</button>
  <button type="button" onclick="tableToExcel('qc','QC夜<%=datetime %>')">QC夜导出</button>
  <button type="button" onclick="tableToExcel('qcb','QC白<%=datetime %>')">QC白导出</button>
  

  
  </h3> 

  </td></tr>
    
    
    
<table id="datatable" border="1">

    <tr> 
    
    
  <td style="background: #027806;color: #fff">Operation</td>
       
         <td style="background: #027806;color: #fff">LED_TP1</td>
         <td style="background: #027806;color: #fff">LED_TP2</td>
         <td style="background: #027806;color: #fff">LED_TP3</td>
         <td style="background: #027806;color: #fff">LED_S01</td>
         <td style="background: #027806;color: #fff">LED_S02</td>
         <td style="background: #027806;color: #fff">LED_S03</td>
         <td style="background: #027806;color: #fff">LED_S04</td>
         <td style="background: #027806;color: #fff">LED_S05</td>
         <td style="background: #027806;color: #fff">LED_S06</td>
         <td style="background: #027806;color: #fff">LED_L01</td>
         <td style="background: #027806;color: #fff">LED_L02</td>
         <td style="background: #027806;color: #fff">LED_L03</td>
         <td style="background: #027806;color: #fff">LED_L04</td>
         <td style="background: #027806;color: #fff">LED_L05</td>
         <td style="background: #027806;color: #fff">LED_L06</td>
         <td style="background: #027806;color: #fff">LED_L07</td>
         <td style="background: #027806;color: #fff">LED_L08</td>
         <td style="background: #027806;color: #fff">LED_L09</td>
         <td style="background: #027806;color: #fff">LED_W01</td>
         <td style="background: #027806;color: #fff">LED_W02</td>
         <td style="background: #027806;color: #fff">LED_W03</td>
         <td style="background: #027806;color: #fff">LED_W04</td>
         <td style="background: #027806;color: #fff">LED_W05</td>
         <td style="background: #027806;color: #fff">LED_W06</td>
         <td style="background: #027806;color: #fff">LED_W07</td>
         <td style="background: #027806;color: #fff">LED_W08</td >
         <td style="background: #027806;color: #fff">LED_W09</td>
         <td style="background: #027806;color: #fff">LED_W10</td>
         <td style="background: #027806;color: #fff">LED_W11</td>
         <td style="background: #027806;color: #fff">LED_W12</td>
         <td style="background: #027806;color: #fff">LED_W13</td>
         <td style="background: #027806;color: #fff">LED_W14</td>
         <td style="background: #027806;color: #fff">LED_W15</td>
         <td style="background: #027806;color: #fff">LED_W16</td>
         <td style="background: #027806;color: #fff">LED_S99</td>
         <td style="background: #027806;color: #fff">LED_L99</td>
         <td style="background: #027806;color: #fff">LED_W99</td>
         <td style="background: #027806;color: #fff">LED_T99</td>

       </tr>
      
       
          <% while(rs.next()){ %>
        
        <tr >
       
           <td style=" background: #cb99fa"> <%=rs.getString(1)%></td>
            <td> <%=rs.getString(2)%></td>
             <td> <%=rs.getString(3)%></td>
              <td> <%=rs.getString(4)%></td>
               <td> <%=rs.getString(5)%></td>
                <td> <%=rs.getString(6)%></td>
                 <td> <%=rs.getString(7)%></td>
                  <td> <%=rs.getString(8)%></td>
                   <td> <%=rs.getString(9)%></td>
                    <td> <%=rs.getString(10)%></td>
                     <td> <%=rs.getString(11)%></td>
                      <td> <%=rs.getString(12)%></td>
                       <td> <%=rs.getString(13)%></td>
                        <td> <%=rs.getString(14)%></td>
                         <td> <%=rs.getString(15)%></td>
                          <td> <%=rs.getString(16)%></td>
                           <td> <%=rs.getString(17)%></td>
                            <td> <%=rs.getString(18)%></td>
                             <td> <%=rs.getString(19)%></td>
                              <td> <%=rs.getString(20)%></td>
                               <td> <%=rs.getString(21)%></td>
                                <td> <%=rs.getString(22)%></td>
                                 <td> <%=rs.getString(23)%></td>
                                  <td> <%=rs.getString(24)%></td>
                                   <td> <%=rs.getString(25)%></td>
                                    <td> <%=rs.getString(26)%></td>
                                     <td> <%=rs.getString(27)%></td>
                                      <td> <%=rs.getString(28)%></td>
                                      <td> <%=rs.getString(29)%></td>
                                       <td> <%=rs.getString(30)%></td>
                                        <td> <%=rs.getString(31)%></td>
                                         <td> <%=rs.getString(32)%></td>
                                          <td> <%=rs.getString(33)%></td>
                                           <td> <%=rs.getString(34)%></td> 
                                            <td> <%=rs.getString(35)%></td> 
                                             <td> <%=rs.getString(36)%></td> 
                                              <td> <%=rs.getString(37)%></td> 
                                               <td> <%=rs.getString(38)%></td>
                                               <td> <%=rs.getString(39)%></td> 
                                          
    
  
     <% } %>
    

  </tr>    
  

   

  
 <table  name="er" id="er" style="position:absolute;top:430px;left:9px;width: 350px;font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:10px">
  <tr>
      <td style="background: #94c9ff;border: 1px solid #ebebeb;">PDLINE_NAME  </td>
       <td style="background: #fe99d1;border: 1px solid #ebebeb;">INPUT</td>
          <td style="background: #94c9ff;border: 1px solid #ebebeb;">GOOD</td>
          <td style="background: #94c9ff;border: 1px solid #ebebeb;">Fail_QTY</td>
           <td  style="background: #fed09e;border: 1px solid #ebebeb;">YIELD</td>
  </tr>
 
  <% while(rc.next()){   %>
 
    <tr >
       
           <td style="background: #94c9ff; border: 1px solid #ebebeb;"> <%=rc.getString(1)%></td>
           <td style="background: #fe99d1; border: 1px solid #ebebeb;"> <%=rc.getString(2)%></td>
           <td style="background: #94c9ff; border: 1px solid #ebebeb;"> <%=rc.getString(3)%></td>
           <td style="background: #94c9ff; border: 1px solid #ebebeb;"> <%=rc.getString(4)%></td>
           <td style="background: #fed09e; border: 1px solid #ebebeb;"> <%=rc.getString(5)%></td>
</tr>
           
  <% } %>



  </table>
  

  
  
 <table id="blb" style="position:absolute;top:430px;left:749px;width: 19.4%;font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:10px">
  <tr>
	
        <td style="background: #008205;border: 1px solid #ebebeb;color: #fff;">不良代码(白班)</td>
         <td style="background: #008205;border: 1px solid #ebebeb;color: #fff;">不良描述(白班)</td>
          <td style="background: #008205;border: 1px solid #ebebeb;color: #fff;">不良(白班)</td>
          </tr>
       
  
 
  <% while(rb.next()){ %>
    <tr>
       
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=rb.getString(1)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=rb.getString(2)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=rb.getString(3)%></td>
          </tr>
  
  <% } %>
 <table id="two" style="position:absolute;top:430px;left:370px;;width: 19.4%;font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:10px">
  <tr>
	
        <td style="background: #008205;border: 1px solid #ebebeb;color: #fff;">不良代码(夜班)</td>
         <td style="background: #008205;border: 1px solid #ebebeb;color: #fff;">不良描述(夜班)</td>
          <td style="background: #008205;border: 1px solid #ebebeb;color: #fff;">不良(夜班)</td>
          </tr>
       
  
 
  <% while(rf.next()){ %>
    <tr>
       
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=rf.getString(1)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=rf.getString(2)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=rf.getString(3)%></td>
          </tr>
  
  <% } %>
  
</table>



 <table name="qc" id="qc"  style="position:absolute;top:430px;left:1130px;;width: 600;font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:10px">
  <tr>
	
        <td style="background: #7c027b;border: 1px solid #ebebeb;color: #fff;">线别(夜班)</td>
         <td style="background: #7c027b;border: 1px solid #ebebeb;color: #fff;">MODEL(夜班)</td>
          <td style="background: #7c027b;border: 1px solid #ebebeb;color: #fff;">不良描述(夜班)</td>
          <td style="background: #7c027b;border: 1px solid #ebebeb;color: #fff;">SAMPLING(夜班)</td>
          <td style="background: #7c027b;border: 1px solid #ebebeb;color: #fff;">不良(夜班)</td>
          <td style="background: #7c027b;border: 1px solid #ebebeb;color: #fff;">PASS(夜班)</td>
          <td style="background: #7c027b;border: 1px solid #ebebeb;color: #fff;">DPPM(夜班)</td>
          </tr>
       
  
 
  <% while(nq.next()){ %>
    <tr>
       
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=nq.getString(1)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=nq.getString(2)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=nq.getString(3)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=nq.getString(4)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=nq.getString(5)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=nq.getString(6)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=nq.getString(7)%></td>
          </tr>
  
  <% } %>
  
  

  
  
</table>

<table name="qcb" id="qcb" style="position:absolute;top:430px;left:1740px;;width: 600;font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:10px">
  <tr>
	
        <td style="background: #3564fc;border: 1px solid #ebebeb;color: #fff;">线别(白班)</td>
         <td style="background: #3564fc;border: 1px solid #ebebeb;color: #fff;">MODEL(白班)</td>
          <td style="background: #3564fc;border: 1px solid #ebebeb;color: #fff;">不良描述(白班)</td>
          <td style="background: #3564fc;border: 1px solid #ebebeb;color: #fff;">SAMPLING(白班)</td>
          <td style="background: #3564fc;border: 1px solid #ebebeb;color: #fff;">不良(白班)</td>
          <td style="background: #3564fc;border: 1px solid #ebebeb;color: #fff;">PASS(白班)</td>
          <td style="background: #3564fc;border: 1px solid #ebebeb;color: #fff;">DPPM(白班)</td>
          </tr>
       
  
 
  <% while(dq.next()){ %>
    <tr>
       
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=dq.getString(1)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=dq.getString(2)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=dq.getString(3)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=dq.getString(4)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=dq.getString(5)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=dq.getString(6)%></td>
           <td style=" background: #fcfe9d;border: 1px solid #ebebeb;"> <%=dq.getString(7)%></td>
          </tr>
  
  <% } %>
  
</table>



	
	
	 <table name="cd" id="cd"  style="position:absolute;top:51px;left:2350px;width: 500px; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:10px">
  <tr>
	
        <td style="background: #027806;color: #fff;border: 1px solid #ebebeb;">Operation</td>
         <td style="background: #027806;color: #fff;border: 1px solid #ebebeb;">INPUT</td>
         <td style="background: #027806;color: #fff;border: 1px solid #ebebeb;">良品数量</td>
         <td style="background: #027806;color: #fff;border: 1px solid #ebebeb;">不良数量</td>
         <td style="background: #027806;color: #fff;border: 1px solid #ebebeb;">维修数量</td>
          <td style="background: #027806;color: #fff;border: 1px solid #ebebeb;">YEALD</td>
          </tr>
       
  
 
  <% while(hjb.next()){ %>
    <tr>
       
           <td style=" background: #cb99fa;border: 1px solid #ebebeb;"> <%=hjb.getString(1)%></td>
           <td style=" background: #ffffd3;border: 1px solid #ebebeb;"> <%=hjb.getString(2)%></td>
           <td style=" background: #cfffff;border: 1px solid #ebebeb;"> <%=hjb.getString(3)%></td>
           <td style=" background: #cfffff;border: 1px solid #ebebeb;"> <%=hjb.getString(4)%></td>
           <td style=" background: #cfffff;border: 1px solid #ebebeb;"> <%=hjb.getString(5)%></td>
           <td style=" background: #cfffff;border: 1px solid #ebebeb;"> <%=hjb.getString(6)%></td>
          </tr>
  
  <% } %>
  
</table>	
	

	
	
	
		 <table id="he"  style="position:absolute;top:430px;left:2350px;width: 500px;font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:10px">
  <tr>
	
        <td style=" width:140px; background: #f89ace;color: #fff;border: 1px solid #ebebeb;">Operation</td>
        <td style="background: #f89ace;color: #fff;border: 1px solid #ebebeb;">INPUT</td>
         <td style="background: #f89ace;color: #fff;border: 1px solid #ebebeb;">良品数量</td>
          <td style="background: #f89ace;color: #fff;border: 1px solid #ebebeb;">不良数量</td>
         <td style="background: #f89ace;color: #fff;border: 1px solid #ebebeb;">维修数量</td>
         <td style="background: #f89ace;color: #fff;border: 1px solid #ebebeb;">YEALD</td>
          </tr>
       
  
 
  <% while(wips.next()){ %>
    <tr>
       
           <td  style="background: #cb99fa;border: 1px solid #ebebeb;"> <%=wips.getString(1)%></td>
           <td style=" background: #ffffd3;border: 1px solid #ebebeb;"> <%=wips.getString(2)%></td>
           <td style=" background: #cfffff;border: 1px solid #ebebeb;"> <%=wips.getString(3)%></td>
           <td style=" background: #cfffff;border: 1px solid #ebebeb;"> <%=wips.getString(4)%></td>
           <td style=" background: #cfffff;border: 1px solid #ebebeb;"> <%=wips.getString(5)%></td>
            <td style=" background: #cfffff;border: 1px solid #ebebeb;"> <%=wips.getString(6)%></td>
          </tr>
  
  <% } %>
  
</table>
	
	
	
	
	</table>
	

 
  </table>
  
<script type="text/javascript">
window.onload = function(er) {
    // 第4列
    var column_num = 4;
                                      
    // 获取元素
    var table = document.getElementById("er"),
        rows = table.getElementsByTagName("tr");
                                      
    // 循环表格
    for(var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        for(var c = 0; c < cells.length; c++) {
            // 对应列
            if(c + 1 === column_num
                // 判断是否小于 0
                && parseFloat(cells[c].innerHTML) > 0) {
                // 两者均成立，改变颜色
                rows[i].style.color = "#f00";
                // 检查下一行
                break;
            }
        }
    }
}
</script> 
<script type="text/javascript">

    // 第5列
    var column_num = 5;
                                      
    // 获取元素
    var table = document.getElementById("qc"),
        rows = table.getElementsByTagName("tr");
                                      
    // 循环表格
    for(var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        for(var c = 0; c < cells.length; c++) {
            // 对应列
            if(c + 1 === column_num
                // 判断是否小于 0
                && parseFloat(cells[c].innerHTML) > 0) {
                // 两者均成立，改变颜色
                rows[i].style.color = "#f00";
                // 检查下一行
                break;
            
        }
    }
}
</script>
<script type="text/javascript">

    // 第5列
    var column_num = 5;
                                      
    // 获取元素
    var table = document.getElementById("qcb"),
        rows = table.getElementsByTagName("tr");
                                      
    // 循环表格
    for(var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        for(var c = 0; c < cells.length; c++) {
            // 对应列
            if(c + 1 === column_num
                // 判断是否小于 0
                && parseFloat(cells[c].innerHTML) > 0) {
                // 两者均成立，改变颜色
                rows[i].style.color = "#f00";
                // 检查下一行
                break;
            
        }
    }
}
</script>
<script type="text/javascript">

    // 第4列
    var column_num = 4;
                                      
    // 获取元素
    var table = document.getElementById("cd"),
        rows = table.getElementsByTagName("tr");
                                      
    // 循环表格
    for(var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        for(var c = 0; c < cells.length; c++) {
            // 对应列
            if(c + 1 === column_num
                // 判断是否小于 0
                && parseFloat(cells[c].innerHTML) > 0 ) {
                // 两者均成立，改变颜色
                rows[i].style.color = "#f00";
                // 检查下一行
          
                break;
               
            }
        
    }
}
</script>

<script type="text/javascript">
    function base64 (content) {
       return window.btoa(unescape(encodeURIComponent(content)));         
    }
    /*
    *@tableId: table的Id
    *@fileName: 要生成excel文件的名字（不包括后缀，可随意填写）
    */
    function tableToExcel(tableID,fileName){
        var table = document.getElementById(tableID);
      var excelContent = table.innerHTML;
      var excelFile = "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:x='urn:schemas-microsoft-com:office:excel' xmlns='http://www.w3.org/TR/REC-html40'>";
      excelFile += "<head><!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>{worksheet}</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--></head>";
      excelFile += "<body><table>";
      excelFile += excelContent;
      excelFile += "</table></body>";
      excelFile += "</html>";
      var link = "data:application/vnd.ms-excel;base64," + base64(excelFile);
      var a = document.createElement("a");
      a.download = fileName+".xls";
      a.href = link;
      a.click();
    }
</script>














</body>

</html>
