<html>
<!DOCTYPE html>
<html lang="en" class="no-js">
<%@ page contentType="text/html;charset=utf-8" language="java" errorPage="" %>
    <head>

      
        <title>注册(用户)</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

       
        <link rel="stylesheet" href="assets/css/reset.css">
        <link rel="stylesheet" href="assets/css/supersized.css">
        <link rel="stylesheet" href="assets/css/style.css">

    
	
<script language=JavaScript>
function click() {
	 } 
	function click1(){
	if (event. button==2) {
	alert('禁止右键喔!')} }
	function CtrlKeyDown(){
	if(event. ctrlKey){
	alert('不当的操作将损害您的系统!')}} 
	document. onkeydown=CtrlKeyDown; 
	document. onselectstart=click; 
	document. onmousedown=click1;
</script>
    </head>

    <body>

        <div class="page-container">
            <h1>注册(用户)</h1>
            <form action="zcdata.jsp" method="post" autocomplete="off">
                <input type="text" name="username" id="username" class="username" placeholder="请输入您的用户名！">
                <input type="password" name="password" id="password" class="password" placeholder="请输入您的用户密码！">
              <input type="text" name="email" id="email" class="username" placeholder="请输入您的邮箱！">
              <input type="text" name="workorder" id="workorder" class="username" placeholder="请输入您的工号！">
                <button type="submit" class="submit_button">注册</button>
                <div class="error"><span>+</span></div>
            </form>
           
        </div>
		
       
        <script src="assets/js/jquery-1.8.2.min.js" ></script>
        <script src="assets/js/supersized.3.2.7.min.js" ></script>
        <script src="assets/js/supersized-init.js" ></script>
        <script src="assets/js/scripts.js" ></script>

    </body>
<div style="text-align:center;">

</div>
</html>

