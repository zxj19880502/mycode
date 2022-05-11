<%@ page contentType="text/html;charset=utf-8" language="java" errorPage="" %>
<%@ page
    import="java.sql.Connection"
 import="java.sql.ResultSet"
 import="java.sql.SQLException"
 import="java.sql.Statement"
 %>
<%@ page import="java.text.*"%>
<%@ page import="java.sql.*" %>
<%@page import="java.util.*"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>      </head>
 
  <body>
 
       <center><H1>MQA数据录入系统</H1></center>
          正在执行Q-HOLD数据录入<br />
 <%
 
       Class.forName("oracle.jdbc.driver.OracleDriver");
    java.sql.DriverManager.registerDriver(new oracle.jdbc.driver.OracleDriver());
  
    Connection con=DriverManager.getConnection("jdbc:oracle:thin:@172.22.8.234/MES","sajet","tech");
    request.setCharacterEncoding("UTF-8");
    response.setContentType("text/html; charset=utf-8");
       
        
        String jz = request.getParameter("jz");
        String sl = request.getParameter("sl");
        String holdyy = request.getParameter("holdyy");
        String fl = request.getParameter("fl");
        String clzt = request.getParameter("clzt");
       
      
        String datatime = request.getParameter("datatime");
        
        
      
        		
       String qhold="insert into WIQWMS.q_hold values('"+jz+"','"+sl+"','"+holdyy+"','"+fl+"','"+clzt+"','"+datatime+"')";
   	       
              Statement smt2=con.createStatement();
          int  v=  smt2.executeUpdate(qhold);
      		if(v==1){%> 数据录入成功！<br><input type="button" name="Submit" value="返回上一页" onclick="window.location.href='tijiao.jsp';"> <%}
      		else{%> 数据录入失败！<br> <%}
      		if(smt2!=null) {smt2.close();}
      		if(con!=null) {con.close();}  	   		
          		
          		
        		%>  
  
  
  </body>
</html>

