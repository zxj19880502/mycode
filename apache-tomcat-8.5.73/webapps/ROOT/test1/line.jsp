<%@ page contentType="text/html;charset=utf-8" language="java" errorPage="" %>
 <%@ page import="java.text.*"%>
<%@ page import="java.sql.*" %>
 <%@page import="java.util.*"%>
 
 <meta http-equiv="refresh" content="300">

<html>

<head>
 
  <title>线别查询</title>

 
 <style type="text/css">
#container {
    height: 70%;
}

.highcharts-figure,
.highcharts-data-table table {
    min-width: 100%;
    max-width: 100%;
    margin: 1em auto;
}



#datatable caption {
    padding: 1em 0;
    font-size: 1.2em;
    color: #555;
}

#datatable th {
    font-weight: 600;
    padding: 0.5em;
}

#datatable td,
#datatable th,
#datatable caption {
    padding: 0.5em;
}


		</style>
 
 
 
</head>
<body>


<%

Class.forName("oracle.jdbc.driver.OracleDriver");
Connection connection=DriverManager.getConnection("jdbc:oracle:thin:@172.22.24.119:1521:ledmes","sajet","tech");
Statement stmt=connection.createStatement();
String path = request.getContextPath(); 
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/"; 
String name = request.getParameter("line");//用request得到 
String starday = request.getParameter("day");//用request得到 
String startime = request.getParameter("time");//用request得到 
String endday = request.getParameter("endday");//用request得到 
String endtime = request.getParameter("endtime");//用request得到
String datetime = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(Calendar.getInstance().getTime());//系统时间

ResultSet rs=stmt.executeQuery("SELECT PROCESS_NAME,SUM(PASS_QTY)as good,sum(FAIL_QTY) as Fail,sum(PASS_QTY+FAIL_QTY)as input,round(decode(SUM(PASS_QTY),0,0,(SUM(PASS_QTY)/(sum(PASS_QTY+FAIL_QTY)))*100),2)as Yield from input_qtyc where PDLINE_NAME='"+name+"'AND WORK_DATE||WORK_TIME between to_CHAR('"+startime+""+starday+"')and to_char('"+endtime+""+endday+"') GROUP BY PROCESS_NAME ORDER BY Fail DESC   ");

%>

<figure class="highcharts-figure">
<tr><td><h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;数据更新时间：<%=datetime %></h1></td></tr>
    <div id="container"></div>
    
<table  id="datatable" style="position:absolute;width: 100%;font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">Process</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">Output</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">Fail</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">Input</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">Yield(%)</td>
    </tr>
    <% while(rs.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;"><%=rs.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=rs.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;" ><%=rs.getString(3)%></td>
        <td style=" border: 1px solid #ebebeb;"><%=rs.getString(4)%></td>
        <td style=" border: 1px solid #ebebeb;"><%=rs.getString(5)%></td>
    </tr>
    
 
    <% } %>

</table>

<script type="text/javascript">
window.onload = function() {
    // 第3列
    var column_num = 3;
                                      
    // 获取元素
    var table = document.getElementById("datatable"),
        rows = table.getElementsByTagName("tr");
                                      
    // 循环表格
    for(var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        for(var c = 0; c < cells.length; c++) {
            // 对应列
            if(c + 1 === column_num
                // 判断是否大于 0
                && parseFloat(cells[c].innerHTML) > 0 && parseFloat(cells[c].innerHTML)<= 10) {
                // 两者均成立，改变颜色
                rows[i].style.background = "#f7c017";
                
                // 检查下一行
                break;
            }
            if(c + 1 === column_num
                    // 判断是否大于 0
                    && parseFloat(cells[c].innerHTML) > 10 ) {
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
};
</script> 
 
 </figure>
   


 
 
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
		text: '<%=name %>看板'
		// 该功能依赖 data.js 模块，详见https://www.hcharts.cn/docs/data-modules
	},
	yAxis: {
		allowDecimals: false,
		title: {
			text: '个',
			rotation: 0
		}
	},
	credits:{
	     enabled: false // 禁用版权信息
	},
	
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' +
                this.point.y + ' ' + this.point.name.toLowerCase();
        }
    }

});
		</script>
 
</body>
</html>
