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
          正在执行录入<br />
 <%
 
       Class.forName("oracle.jdbc.driver.OracleDriver");
    java.sql.DriverManager.registerDriver(new oracle.jdbc.driver.OracleDriver());
  
    Connection con=DriverManager.getConnection("jdbc:oracle:thin:@172.22.8.234/MES","sajet","tech");
    request.setCharacterEncoding("UTF-8");
    response.setContentType("text/html; charset=utf-8");
        String jcps = request.getParameter("jcps");
        String bhgps = request.getParameter("bhgps");
       
        String gds = request.getParameter("gds");
        String bljs = request.getParameter("bljs");
        
        String trs = request.getParameter("trs");
        String bls = request.getParameter("bls");
       
        String datatime1 = request.getParameter("datatime1");
        String nonjcps = request.getParameter("nonjcps");
        String nonbhgps = request.getParameter("nonbhgps");
        String nongds = request.getParameter("nongds");
        String nonbljs = request.getParameter("nonbljs");
       
        String nontrs = request.getParameter("nontrs");
        String nonbls = request.getParameter("nonbls");
        
        
       
        
       String sql="insert into WIQWMS.mqa values( '"+jcps+"','"+bhgps+"','"+gds+"','"+bljs+"','"+trs+"','"+bls+"','"+datatime1+"','"+nonjcps+"','"+nonbhgps+"','"+nongds+"','"+nonbljs+"','"+nontrs+"','"+nonbls+"')";
       
                Statement smt=con.createStatement();
            int  n=  smt.executeUpdate(sql);
        		if(n==1){%> 数据插入成功！<br><input type="button" name="Submit" value="返回上一页" onclick="window.location.href='tijiao.jsp';"> <%}
        		else{%> 数据插入失败！<br> <%}
        		if(smt!=null) {smt.close();}
        		if(con!=null) {con.close();}
 
          		
          		
          		
        		%>  
  
  
  </body>
</html>


