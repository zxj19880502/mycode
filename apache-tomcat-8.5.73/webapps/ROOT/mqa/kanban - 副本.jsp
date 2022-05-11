<!DOCTYPE html>
<%@ page contentType="text/html;charset=utf-8" language="java" errorPage="" %>
<%@ page import="java.text.*"%>
<%@ page import="java.sql.*" %>
<%@page import="java.util.*"%>
<html>
	<head>
	
<meta name="viewport" content="width=device-width,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>	
	    
		<title>MQA数据可视化看板</title>
	<link rel="stylesheet" href="css/app.css" />	
		
		
	
<style>
table tbody {
    display: block;
  
   
}
 
table thead, tbody tr {
    display:table;
    width:100%;
    table-layout:fixed;
}
 
table thead {
    width: calc( 100% - 1em )
    display: none;
}

</style>


	</head>
	
	<body>
	
	
	<%

Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection connection=DriverManager.getConnection("jdbc:oracle:thin:@172.22.8.234/MES","sajet","tech");
Statement stmt=connection.createStatement();
String path = request.getContextPath(); 
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/"; 
String startime = request.getParameter("time");//用request得到 
String endtime = request.getParameter("endtime");//用request得到


Statement cv=connection.createStatement();
Statement ccd=connection.createStatement();
Statement ccdd=connection.createStatement();
Statement cb=connection.createStatement();
Statement cbbc=connection.createStatement();
Statement jzz=connection.createStatement();

Statement hzsj1=connection.createStatement();

Statement hzsj3=connection.createStatement();

ResultSet rs=stmt.executeQuery("SELECT DATATIME1, round(sum(BHGPS/(JCPS*5)*100),2)AS PCFAI不良率,round(sum(nonBHGPS/(nonJCPS*5)*100),2)AS NonPCFAI不良率,round(sum(BLJS/GDS),2)AS PC异常比例,round(sum(nonBLJS/nonGDS),2)AS NonPC异常比例 from WIQWMS.MQA where DATATIME1 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY DATATIME1 ORDER BY DATATIME1");
ResultSet qcc=ccd.executeQuery("SELECT DATATIME1, round(sum(BLS /TRS*1000000),2)AS PCHiPOTDPPM,round(sum(nonBLS /nonTRS*1000000),2)AS NonPCHiPOTDPPM from WIQWMS.MQA where DATATIME1 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY DATATIME1 ORDER BY DATATIME1");
ResultSet qd=ccdd.executeQuery("SELECT DATATIME2, round(sum(WGBLS /LJCYS *1000000),2)AS PC外观DPPM,round(sum(NONWGBLS  /NONLJCYS *1000000),2)AS NonPC外观DPPM,round(sum((WGBLS+NONWGBLS) /(LJCYS+NONLJCYS) *1000000),2)AS total外观DPPM from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY DATATIME2 ORDER BY DATATIME2");
ResultSet cbb=cb.executeQuery("SELECT DATATIME2, round(sum(DXBLS  /LJCYS  *1000000),2)AS PC电性DPPM,round(sum(NONDXBLS  /NONLJCYS  *1000000),2)AS NonPC电性DPPM,round(sum((DXBLS +NONDXBLS)  /(LJCYS +NONLJCYS) *1000000),2)AS total电性DPPM from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY DATATIME2 ORDER BY DATATIME2");
ResultSet hold=cbbc.executeQuery("SELECT DATATIME, sum(LJSYS) ,sum(DRDJSL) FROM wiqwms.q_hold where DATATIME BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY DATATIME ORDER BY DATATIME");

ResultSet jzsl=jzz.executeQuery("SELECT DATATIME , JZ ,SL  ,HOLDYY ,FL ,CLZT  FROM WIQWMS.q_hold WHERE DATATIME  BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"')  ORDER BY DATATIME");


ResultSet hz1=hzsj1.executeQuery("SELECT DATATIME2,sum(LJCYS),sum(WGBLS),sum(DXBLS),sum(NONLJCYS),sum(NONWGBLS),sum(NONDXBLS),round(sum(WGBLS /LJCYS *1000000),2)AS PC外观DPPM,round(sum(NONWGBLS  /NONLJCYS *1000000),2)AS NonPC外观DPPM,round(sum((WGBLS+NONWGBLS)  /(LJCYS+NONLJCYS) *1000000),2)AS total外观DPPM, round(sum(DXBLS  /LJCYS  *1000000),2)AS PC电性DPPM,round(sum(NONDXBLS  /NONLJCYS  *1000000),2)AS NonPC电性DPPM,round(sum((DXBLS +NONDXBLS)  /(LJCYS +NONLJCYS) *1000000),2)AS total电性DPPM FROM WIQWMS.OOBA  WHERE DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY DATATIME2 ORDER BY DATATIME2");

ResultSet hz3=hzsj3.executeQuery("SELECT DATATIME1,sum(JCPS),sum(BHGPS),sum(NONJCPS),sum(NONBHGPS), round(sum(BHGPS/(JCPS*5)*100),2)AS PCFAI不良率,round(sum(nonBHGPS/(nonJCPS*5)*100),2)AS NonPCFAI不良率,round(sum(BLJS/GDS),2)AS PC异常比例,round(sum(nonBLJS/nonGDS),2)AS NonPC异常比例,round(sum(BLS /TRS*1000000),2)AS PCHiPOTDPPM,round(sum(nonBLS /nonTRS*1000000),2)AS NonPCHiPOTDPPM FROM WIQWMS.MQA WHERE DATATIME1 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY DATATIME1 ORDER BY DATATIME1");
%>
	
	
	
		<div class="header">
			<h1 class="header-title">MQA数据可视化看板</h1>
		</div>
		<div class="wrapper">
			<div class="content">
				<div class="col col-l">
					<div class="xpanel-wrapper xpanel-wrapper-40">
						<div class="xpanel xpanel-l-t">
							<div class="title">FAI不良率/异常比例</div>
							
							 
							<div style="height:80%;" id="container"></div>
							
							
						</div>
					</div>
					
					<div class="xpanel-wrapper xpanel-wrapper-40"style="margin-top: 1%;">
						<div class="xpanel xpanel-l-b">
							<div class="title">HI-POT DPPM</div>
							
							<div style="height:80%;" id="ycll"></div>
							
						</div>
					</div>
					<div class="xpanel-wrapper xpanel-wrapper-400"style="margin-top: 1%;">
						<div class="xpanel xpanel-l-b">
						<div class="title">Q HOLD</div>
		<div style="overflow-x:scroll; width: 100%;">			
	<table id="jzsl" style="border-collapse: collapse;text-align: center;font-size:0.8em;width:300%;">
    <thead>
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">机种</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">数量</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">HOLD原因</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">分类</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">处理状态</td>
    </tr>
    </thead>
    <tbody style="height:120px;">
    <% while(jzsl.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;"><%=jzsl.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=jzsl.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=jzsl.getString(3)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=jzsl.getString(4)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=jzsl.getString(5)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=jzsl.getString(6)%></td>
    </tr>
    
 
    <% } %>
</tbody>
</table>
				
			</div>
                   </div>
					</div>
				</div>
				<div class="col col-c">
					<div class="xpanel-wrapper xpanel-wrapper-75">
						<div class="xpanel xpanel-c-b"style="margin-top: 3%;">
						<div class="title">汇总数据表</div>
						
		
			
		<div style="overflow-x:scroll; width: 100%;">		
	
	<table  id="hz1"   style="border-collapse: collapse;text-align: center;font-size:0.8em;width:300%;">
    <thead >
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">累计抽样数</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">累计外观不良数</td>       
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">累计电性不良数</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">NON累计抽样数</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">NON外观不良数</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">NON电性不良数</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">PC外观DPPM</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">NONPC外观DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">TOTAL外观DPPM</td>
          <td style="background: #94c9ff;border: 1px solid #ebebeb;">PC电性DPPM</td>
           <td style="background: #94c9ff;border: 1px solid #ebebeb;">NONPC电性DPPM</td>
            <td style="background: #94c9ff;border: 1px solid #ebebeb;">TOTAL电性DPPM</td>
    </tr>
    </thead>
    <tbody style="height:230px;" >
    <% while(hz1.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;"><%=hz1.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(3)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(4)%></td>
       <td style=" border: 1px solid #ebebeb;"><%=hz1.getString(5)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(6)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(7)%></td>
      <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(8)%></td>
      <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(9)%></td>
      <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(10)%></td>
      <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(11)%></td>
      <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(12)%></td>
      <td style=" border: 1px solid #ebebeb;" ><%=hz1.getString(13)%></td>
      
    </tr>
    
 
    <% } %>
</tbody>
</table>	
			
					</div>
					
			</div>
					
					
					</div>
					
					
					
				<div class="xpanel-wrapper xpanel-wrapper-4001">		
			<div class="xpanel xpanel-c-b" style="margin-top: 3%;">
						<div class="title">汇总数据表</div>
						
		
			
				
	<div style="overflow-x:scroll; width: 100%;">	
	<table  id="hz3"   style="border-collapse: collapse;text-align: center;font-size:0.8em;width:300%;">
    <thead >
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
        
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">累计检查批数</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">累计不合格批数</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">Non累计检查批数</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">Non累计不合格批数</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">PCFAI不良率</td> 
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">NonPCFAI不良率</td>
             <td style="background: #94c9ff;border: 1px solid #ebebeb;">PC异常比例</td>
              <td style="background: #94c9ff;border: 1px solid #ebebeb;">NonPC异常比例</td>
            <td style="background: #94c9ff;border: 1px solid #ebebeb;">PCHIPOTDPPM</td>
              <td style="background: #94c9ff;border: 1px solid #ebebeb;">NONPCHIPOTDPPM</td>
    </tr>
    </thead>
    <tbody style="height:230px;" >
    <% while(hz3.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;"><%=hz3.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=hz3.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=hz3.getString(3)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=hz3.getString(4)%></td>
       <td style=" border: 1px solid #ebebeb;"><%=hz3.getString(5)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=hz3.getString(6)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=hz3.getString(7)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=hz3.getString(8)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=hz3.getString(9)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=hz3.getString(10)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=hz3.getString(11)%></td>
       
      
    </tr>
    
 
    <% } %>
</tbody>
</table>	
			</div>
					</div>		
					</div>	
					
					
					
					
					<div class="xpanel-wrapper xpanel-wrapper-25">
						
		
				<table   id="datatable" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">PCFAI不良率</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">NonPCFAI不良率</td>
        
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">PC异常比例</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">NonPC异常比例</td>
       
    </tr>
    <% while(rs.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;"><%=rs.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=rs.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=rs.getString(3)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=rs.getString(4)%></td>
       <td style=" border: 1px solid #ebebeb;" ><%=rs.getString(5)%></td>
      
    </tr>
    

    <% } %>
</table>

							<table  id="ccd" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">PCHiPOTDPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">NonPCHiPOTDPPM</td>
       
       
    </tr>
    <% while(qcc.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;"><%=qcc.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=qcc.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=qcc.getString(3)%></td>
        
        
    </tr>
    
 
    <% } %>

</table>		
					<table  id="qd" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">PC外观DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">NonPC外观DPPM</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">total外观DPPM</td>
        
    </tr>
    <% while(qd.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;"><%=qd.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=qd.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=qd.getString(3)%></td>
        <td style=" border: 1px solid #ebebeb;"><%=qd.getString(4)%></td>
       
    </tr>
    
 
    <% } %>

</table>		
		<table  id="cbb" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">PC电性DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">NONPC电性DPPM</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">total电性DPPM</td>
        
    </tr>
    <% while(cbb.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;"><%=cbb.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=cbb.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=cbb.getString(3)%></td>
        <td style=" border: 1px solid #ebebeb;"><%=cbb.getString(4)%></td>
       
    </tr>
    
 
    <% } %>

</table>	

					
					</div>
					
							
							
				</div>
				<div class="col col-r">
					<div class="xpanel-wrapper xpanel-wrapper-30"style="margin-top: 3%;">
						<div class="xpanel xpanel-r-t">
							<div class="title">OOBA外观</div>
							
							 
							<div style="height:80%;" id="qdd"></div>
							
							
						</div>
					</div>
					<div class="xpanel-wrapper xpanel-wrapper-30"style="margin-top: 3%;">
						<div class="xpanel xpanel-r-m">
							<div class="title">电性DPPM</div>
							<div style="height:80%;" id="cbbc"></div>
						</div>
					</div>
					
					<div class="xpanel-wrapper xpanel-wrapper-45" >
					<div class="xpanel xpanel-r-m">
			
				<div style="overflow-x:scroll; width: 100%;">	
			<table  id="cbbcd" style="border-collapse: collapse;text-align: center;font-size:0.8em;width:120%;">
    <thead>
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">累计送验数</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">当日待检数量</td>
        
    </tr>
    </thead>
    <tbody style="height:130px;">
  
    <% while(hold.next()){ %>
     
    <tr  >
        <td style=" border: 1px solid #ebebeb;"><%=hold.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=hold.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=hold.getString(3)%></td>
       
    </tr>
    
 
    <% } %>
</tbody>
</table>
</div>
					
					</div>
				</div>
			</div>
			
		</div>
 		

<script type="text/javascript">

    // 第5列
    var column_num = 3;
                                      
    // 获取元素
    var table = document.getElementById("cbbcd"),
        rows = table.getElementsByTagName("tr");
                                      
    // 循环表格
    for(var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        for(var c = 0; c < cells.length; c++) {
            // 对应列
            if(c + 1 === column_num
                // 判断是否大于 0
                && parseFloat(cells[c].innerHTML) > 0 && parseFloat(cells[c].innerHTML)<= 47000) {
                // 两者均成立，改变颜色
                rows[i].style.background = "#f7c017";
               
                // 检查下一行
                break;
            }
            if(c + 1 === column_num
                    // 判断是否大于 0
                    && parseFloat(cells[c].innerHTML) > 47000 ) {
                    // 两者均成立，改变颜色
                    rows[i].style.background = "#f73c17";
                   
                    // 检查下一行
                    break;
                }
            if(c + 1 === column_num
                    // 判断是否大于 0
                    && parseFloat(cells[c].innerHTML) === 0) {
                    // 两者均成立，改变颜色
                    rows[i].style.background = "#37f717";
                   
                    // 检查下一行
                    break;
                }
        }
}
</script>
<script type="text/javascript">

    // 第5列
    var column_num = 3;
                                      
    // 获取元素
    var table = document.getElementById("jzsl"),
        rows = table.getElementsByTagName("tr");
                                      
    // 循环表格
    for(var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        for(var c = 0; c < cells.length; c++) {
            // 对应列
            if(c + 1 === column_num
                // 判断是否大于 0
                && parseFloat(cells[c].innerHTML) > 0 ) {
                // 两者均成立，改变颜色
                rows[i].style.background = "#37f717";
               
                // 检查下一行
                break;
            }
          
            if(c + 1 === column_num
                    // 判断是否大于 0
                    && parseFloat(cells[c].innerHTML) === 1) {
                    // 两者均成立，改变颜色
                    rows[i].style.background = "#37f717";
                    
                    // 检查下一行
                    break;
                }
        }
}
</script>
<script type="text/javascript">

    // 第5列
    var column_num = 3;
                                      
    // 获取元素
    var table = document.getElementById("hz1"),
        rows = table.getElementsByTagName("tr");
                                      
    // 循环表格
    for(var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        for(var c = 0; c < cells.length; c++) {
            // 对应列
          
          
            if(c + 1 === column_num
                    // 判断是否大于 0
                    && parseFloat(cells[c].innerHTML) >= 0) {
                    // 两者均成立，改变颜色
                    rows[i].style.background = "#37f717";
                   
                    // 检查下一行
                    break;
                }
        }
}
</script>
<script type="text/javascript">

    // 第5列
    var column_num = 3;
                                      
    // 获取元素
    var table = document.getElementById("hz3"),
        rows = table.getElementsByTagName("tr");
                                      
    // 循环表格
    for(var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        for(var c = 0; c < cells.length; c++) {
            // 对应列
          
          
            if(c + 1 === column_num
                    // 判断是否大于 0
                    && parseFloat(cells[c].innerHTML) >= 0) {
                    // 两者均成立，改变颜色
                    rows[i].style.background = "#37f717";
                   
                    // 检查下一行
                    break;
                }
        }
}
</script>

 <script src="highcharts.js"></script>
<script src="data.js"></script>
<script src="exporting.js"></script>
<script src="accessibility.js"></script>
 
 <script type="text/javascript">
 

 
Highcharts.chart('container', {
	
	
	
    data: {
    	 
    	
        table: 'datatable'
        	
    },

    chart: {
    	zoomType:'xy',
    	  backgroundColor: {
              linearGradient: [0, 0, 500, 500],
              stops: [
            	  [0, 'rgb(207, 143, 223)'],
                  [1, 'rgb(241, 252, 177)']
              ]
          },
        type: 'line' //柱状图
        
        
        	
    },
    
    yAxis: {
        allowDecimals: false,
        
        title: {
            text: 'Units'
        }
        
    
    },
    title: {
    	 
		text: '视图'
		// 该功能依赖 data.js 模块，详见https://www.hcharts.cn/docs/data-modules
	},
	
	yAxis: {
		gridLineDashStyle: 'ShortDash',//网格线样式
		allowDecimals: false,
		title: {
			text: '%',
			rotation: 0
		}
	
	},
	credits:{
	     enabled: false // 禁用版权信息
	},
	 plotOptions: {
	        
	line: {
        borderWidth: 0,
        dataLabels:{
            enabled:true,
            color: "#000",
           
        }
        // colorByPoint: true
    }

	    },
	
	    tooltip: {
			pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
			valueDecimals: 2,
			shared: true,
            crosshairs: [true, false]
		},

});



		</script>
		
  <script type="text/javascript">
Highcharts.chart('ycll', {
    data: {
    	
        table: 'ccd'
        	
    },
    chart: {
    	zoomType:'xy',
    	  backgroundColor: {
              linearGradient: [0, 0, 500, 500],
              stops: [
                  [0, 'rgb(236, 183, 249)'],
                  [1, 'rgb(241, 252, 177)']
              ]
          },
        type: 'line' //柱状图
        	// type: 'line' 曲线
    },
   
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Units'
        }
    },
    title: {
		text: '视图'
		// 该功能依赖 data.js 模块，详见https://www.hcharts.cn/docs/data-modules
	},
	yAxis: {
		gridLineDashStyle: 'ShortDash',//网格线样式
		allowDecimals: false,
		title: {
			text: '',
			rotation: 0
		}
	},
	credits:{
	     enabled: false // 禁用版权信息
	},
	plotOptions: {
        line: {
            dataLabels: {
                enabled: true
            }
        }
    },
	
    tooltip: {
		pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> <br/>',
		valueDecimals: 2,
		shared: true,
        crosshairs: [true, false]
	},

});
		</script>
		<script type="text/javascript">
Highcharts.chart('qdd', {
    data: {
    	
        table: 'qd'
        	
    },
    chart: {
    	zoomType:'xy',
    	  backgroundColor: {
              linearGradient: [0, 0, 500, 500],
              stops: [
                  [0, 'rgb(207, 143, 223)'],
                  [1, 'rgb(241, 252, 177)']
              ]
          },
        type: 'line' //柱状图
        	// type: 'line' 曲线
    },
   
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Units'
        }
    },
    title: {
		text: '视图'
		// 该功能依赖 data.js 模块，详见https://www.hcharts.cn/docs/data-modules
	},
	yAxis: {
		gridLineDashStyle: 'ShortDash',//网格线样式
		allowDecimals: false,
		title: {
			text: '',
			rotation: 0
		}
	},
	credits:{
	     enabled: false // 禁用版权信息
	},
	plotOptions: {
        line: {
            dataLabels: {
                enabled: true
            }
        }
    },
	
    tooltip: {
		pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>',
		valueDecimals: 2,
		shared: true,
        crosshairs: [true, false]
	},

});
		</script>
		<script type="text/javascript">
Highcharts.chart('cbbc', {
    data: {
    	
        table: 'cbb'
        	
    },
    chart: {
    	zoomType:'xy',
    	  backgroundColor: {
              linearGradient: [0, 0, 500, 500],
              stops: [
            	  [0, 'rgb(207, 143, 223)'],
                  [1, 'rgb(241, 252, 177)']
              ]
          },
        type: 'line' //柱状图
        	// type: 'line' 曲线
    },
   
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Units'
        }
      
    },
    title: {
		text: '视图'
		// 该功能依赖 data.js 模块，详见https://www.hcharts.cn/docs/data-modules
	},
	yAxis: {
		gridLineDashStyle: 'ShortDash',//网格线样式
		allowDecimals: false,
		title: {
			text: '',
			rotation: 0
		}
	
	},
	credits:{
	     enabled: false // 禁用版权信息
	},
	plotOptions: {
        line: {
            dataLabels: {
                enabled: true
            }
        }
    },
	
    tooltip: {
		pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> <br/>',
		valueDecimals: 2,
		shared: true,
        crosshairs: [true, false]
	},

});
		</script>
	</body>
</html>