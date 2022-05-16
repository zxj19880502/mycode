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
  overflow-x:scroll;
   
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
	request.setCharacterEncoding("UTF-8");
    response.setContentType("text/html; charset=utf-8");
String path = request.getContextPath(); 
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/"; 
String startime = request.getParameter("time");//用request得到 
String endtime = request.getParameter("endtime");//用request得到

String day = request.getParameter("day");
String jzmc = request.getParameter("zjmc");
String ztt = request.getParameter("ztzt");

Statement jzz=connection.createStatement();


ResultSet jzsl=jzz.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME,'YYYY/MM/DD'),'"+day+"') , JZ ,SL  ,HOLDYY ,FL ,CLZT  FROM WIQWMS.q_hold WHERE DATATIME  BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"')and JZ='"+jzmc+"'and CLZT='"+ztt+"'  ORDER BY TO_CHAR(TO_DATE(DATATIME,'YYYY/MM/DD'),'"+day+"')desc");

%>
	
	
	
		<div class="header">
			<h1 class="header-title">MQA数据可视化看板</h1>
		</div>
		<div class="wrapper">
			<div class="content">
				<div class="col col-l">
					
							
					
					
				<div class="xpanel-wrapper xpanel-wrapper-4001">		
			
				<p></p>					
      <div class="title"style="color:#fff">Q HOLD</div>
      <p></p>	
					<table  style="border-collapse: collapse;text-align: center;font-size:1.2em;width:100%;">
    
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">机种</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">数量</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">HOLD原因</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">分类</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">处理状态</td>
    </tr>
   
    <tbody style="height:500px;">
    <% while(jzsl.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=jzsl.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=jzsl.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=jzsl.getString(3)%></td>
       <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=jzsl.getString(4)%></td>
       <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=jzsl.getString(5)%></td>
       <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=jzsl.getString(6)%></td>
    </tr>
    
 
    <% } %>
</tbody>
</table>
					
	
			
					</div>
					
							
							
				</div>
				
			
		</div>
 		
</div>

	
	</body>
</html>