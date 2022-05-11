<html>
<!DOCTYPE html>
<html lang="en" class="no-js">
<%@ page contentType="text/html;charset=utf-8" language="java" errorPage="" %>
    <head>

      
        <title>登录(Login)</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

       
        <link rel="stylesheet" href="assets/css/reset.css">
        <link rel="stylesheet" href="assets/css/supersized.css">
        <link rel="stylesheet" href="assets/css/style.css">

    
		<script type="text/javascript">
		function val(){
			var name=window.document.getElementById("username").value;
			var password=window.document.getElementById("password").value;
			
		
			if (name == ""){
				window.alert("用户名不能为空!");
				return false;
			}
			if (password ==""){
				window.alert("密码不能为空!");
				return false;
			}
		
			 if(name!="zhuxiaolong" && name!="AAA"){ 
				window.alert("用户名错误!");
				return false;
			}
			 
		     if(password!="123456" && password!="1234"){ 
				window.alert("密码错误!");
				return false;
			}
			
			
			return true;
		} 
	</script>
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
            <h1>登录(Login)</h1>
            <form action="tijiao.jsp" method="post" onsubmit="return val()"autocomplete="off">
                <input type="text" name="username" id="username" class="username" placeholder="请输入您的用户名！">
                <input type="password" name="password" id="password" class="password" placeholder="请输入您的用户密码！">
              
                <button type="submit" class="submit_button">登录</button>
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

