<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%> 
<%@ page import="java.sql.*" %> 
<% 
String uName = new String(request.getParameter("username"));
String uPwd = request.getParameter("password");

Connection conn = null;
PreparedStatement pstm = null;
ResultSet rs = null;
String driverClass = "oracle.jdbc.driver.OracleDriver";
String url = "jdbc:oracle:thin:@172.22.8.234/MES";
String user = "sajet";
String password = "tech";
String sql = "select username,password,qx from wiqwms.mqa_user";
try {
	Class.forName(driverClass);
	conn = DriverManager.getConnection(url, user, password);
	pstm = conn.prepareStatement(sql);
	rs = pstm.executeQuery();
	while (rs.next()) {
		if (rs.getString("username").equals(uName) && rs.getString("password").equals(uPwd) && rs.getString("qx").equals("1")) {
			RequestDispatcher dis = request.getRequestDispatcher("tijiao.jsp");
			dis.forward(request, response);
			return;
		} 
		if (rs.getString("username").equals(uName) && rs.getString("password").equals(uPwd) && rs.getString("qx").equals("2")) {
			RequestDispatcher dis = request.getRequestDispatcher("tj.jsp");
			dis.forward(request, response);
			return;
		}
		if (rs.getString("username").equals(uName) && rs.getString("password").equals(uPwd) && rs.getString("qx").equals("3")) {
			RequestDispatcher dis = request.getRequestDispatcher("index.jsp");
			dis.forward(request, response);
			return;
		}
	}
	response.sendRedirect("index.jsp");
} catch (ClassNotFoundException e) {
	// TODO Auto-generated catch block
	e.printStackTrace();
} catch (SQLException e) {
	// TODO Auto-generated catch block
	e.printStackTrace();
} finally {
	try {
		if (rs != null) {
			rs.close();
			rs = null;
		}
		if (pstm != null) {
			pstm.close();
			pstm = null;
		}
		if (conn != null) {
			conn.close();
			conn = null;
		}
	} catch (SQLException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
}

%>

