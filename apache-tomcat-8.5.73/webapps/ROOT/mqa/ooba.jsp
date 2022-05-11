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
          OOBA数据正在执行录入<br />
 <%
 
       Class.forName("oracle.jdbc.driver.OracleDriver");
    java.sql.DriverManager.registerDriver(new oracle.jdbc.driver.OracleDriver());
  
    Connection con=DriverManager.getConnection("jdbc:oracle:thin:@172.22.8.234/MES","sajet","tech");
    request.setCharacterEncoding("UTF-8");
    response.setContentType("text/html; charset=utf-8");
       
    String ljcys = request.getParameter("ljcys");
        String ljscys = request.getParameter("ljsys");
        String drdjsl = request.getParameter("drdjsl");
        String wgbls = request.getParameter("wgbls");
      
        String dxbls = request.getParameter("dxbls");
       
        String datatime2 = request.getParameter("datatime2");
        String nonljsys = request.getParameter("nonljsys");
        String nonljcys = request.getParameter("nonljcys");
        String nondrdjsl = request.getParameter("nondrdjsl");
        String nonwgbls = request.getParameter("nonwgbls");
       
        String nondxbls = request.getParameter("nondxbls");
        
        
        	
        		
       String ooba="insert into WIQWMS.ooba values('"+ljcys+"','"+wgbls+"','"+dxbls+"','"+datatime2+"','"+nonljcys+"','"+nonwgbls+"','"+nondxbls+"','"+ljscys+"','"+drdjsl+"','"+nonljsys+"','"+nondrdjsl+"')";
        	       
                  Statement smt1=con.createStatement();
              int  mm=  smt1.executeUpdate(ooba);
          		if(mm==1){%> 数据录入成功！<br><input type="button" name="Submit" value="返回上一页" onclick="window.location.href='tijiao.jsp';"> <%}
          		else{%> 数据录入失败！<br> <%}
          		if(smt1!=null) {smt1.close();}
          		if(con!=null) {con.close();}  		
        		
          		
        		%>  
  
  
  </body>
</html>
