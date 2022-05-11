<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%> 
<%@ page import="java.sql.*" %> 
<% 
String username1 = request.getParameter("username");
String password1 = request.getParameter("password");
String workorder = request.getParameter("workorder");
String email = request.getParameter("email");

Connection conn =null;
PreparedStatement pstm = null;
ResultSet rs =  null;
String driverClass = "oracle.jdbc.driver.OracleDriver";
String url = "jdbc:oracle:thin:@172.22.8.234/MES";
String user = "sajet";
String password = "tech";
String sql="insert into WIQWMS.MQA_USER(username,password,workorder,email,qx) values(?,?,?,?,?)";
try{
	Class.forName(driverClass);
	conn = DriverManager.getConnection(url, user, password);
	pstm = conn.prepareStatement(sql);
	pstm.setString(1, username1);
	pstm.setString(2, password1);
	pstm.setString(3, workorder);
	pstm.setString(4, email);
	pstm.setString(5, "3");
	rs=pstm.executeQuery();
	if(rs.next()){
		out.print("用户注册成功！");
		response.sendRedirect("index.jsp");
	}else{
		out.print("用户注册失败！");
		response.sendRedirect("zhuce.jsp");
	}
}catch (ClassNotFoundException e) {
	// TODO Auto-generated catch block
	e.printStackTrace();
} catch (SQLException e) {
	// TODO Auto-generated catch block
	e.printStackTrace();
}finally {
	try {
		if(rs!=null) {	
			rs.close();		
			rs =null;
		}
		if(pstm!=null) {	
			pstm.close();
			pstm =null;
		}
		if(conn!=null) {	
			conn.close();
			conn =null;
		}
	} catch (SQLException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
}  

 %> 