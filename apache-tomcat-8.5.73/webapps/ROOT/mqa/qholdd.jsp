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
Statement stmt=connection.createStatement();
String path = request.getContextPath(); 
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/"; 
String startime = request.getParameter("time");//用request得到 
String endtime = request.getParameter("endtime");//用request得到


Statement cbbc=connection.createStatement();
Statement jzz=connection.createStatement();


ResultSet hold=cbbc.executeQuery("SELECT DATATIME2,SUM( LJSYS),SUM(LJCYS),CONCAT(round(decode(SUM(LJCYS),0,0,(SUM(LJCYS)/(sum(LJSYS)))*100),2),'%')AS 累计抽样比例,sum(DRDJSL),SUM(NONLJSYS),SUM(NONLJCYS),CONCAT(round(decode(SUM(NONLJCYS),0,0,(SUM(NONLJCYS)/(sum(NONLJSYS)))*100),2),'%')AS 累计抽样比例,sum(NONDRDJSL) FROM WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY DATATIME2 ORDER BY DATATIME2");

ResultSet jzsl=jzz.executeQuery("SELECT DATATIME , JZ ,SL  ,HOLDYY ,FL ,CLZT  FROM WIQWMS.q_hold WHERE DATATIME  BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"')  ORDER BY DATATIME");

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
					<table id="jzsl" style="border-collapse: collapse;text-align: center;font-size:1.2em;width:100%;">
    
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">机种</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">数量</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">HOLD原因</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">分类</td>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">处理状态</td>
    </tr>
   
    <tbody style="height:300px;">
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
					
	<p></p>					
      <div class="title"style="color:#fff">待验</div>
      <p></p>
	<table  id="cbbcd" style="border-collapse: collapse;text-align: center;font-size:1.2em;width:100%;">
  
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一累计送验数</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一累计抽样数</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一累计抽样比例</td>
      <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一当日待检数量</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二累计送验数</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二累计抽样数</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二累计抽样比例</td>
           <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二当日待检数量</td>
    </tr>
   
    <tbody style="height:300px;">
  
    <% while(hold.next()){ %>
     
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=hold.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=hold.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=hold.getString(3)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=hold.getString(4)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=hold.getString(5)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=hold.getString(6)%></td>
       <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=hold.getString(7)%></td>
       <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=hold.getString(8)%></td>
       <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=hold.getString(9)%></td>
    </tr>
    
 
    <% } %>
</tbody>
</table>
			
					</div>
					
							
							
				</div>
				
			
		</div>
 		



<script type="text/javascript">

    // 第5列
    var column_num = 5;
                                      
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
                cells[c].style.color = "#f7c017";
               
                // 检查下一行
                break;
            }
            if(c + 1 === column_num
                    // 判断是否大于 0
                    && parseFloat(cells[c].innerHTML) > 47000 ) {
                    // 两者均成立，改变颜色
                    cells[c].style.color = "#f73c17";
                   
                    // 检查下一行
                    break;
                }
            if(c + 1 === column_num
                    // 判断是否大于 0
                    && parseFloat(cells[c].innerHTML) === 0) {
                    // 两者均成立，改变颜色
                    cells[c].style.color = "#37f717";
                   
                    // 检查下一行
                    break;
                }
        }
}
</script>

<script type="text/javascript">

    // 第5列
    var column_num = 9;
                                      
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
                cells[c].style.color = "#f7c017";
               
                // 检查下一行
                break;
            }
            if(c + 1 === column_num
                    // 判断是否大于 0
                    && parseFloat(cells[c].innerHTML) > 47000 ) {
                    // 两者均成立，改变颜色
                   cells[c].style.color = "#f73c17";
                   
                    // 检查下一行
                    break;
                }
            if(c + 1 === column_num
                    // 判断是否大于 0
                    && parseFloat(cells[c].innerHTML) === 0) {
                    // 两者均成立，改变颜色
                    cells[c].style.color = "#37f717";
                   
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
    	 
		text: '外观DPPM'
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
        borderWidth: 0,
        dataLabels:{
            enabled:true,
            color: "#000",
           
        }
        // colorByPoint: true
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
 

 
Highcharts.chart('aa', {
	
	
	
    data: {
    	 
    	
        table: 'faidd'
        	
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
    	 
		text: '电性DPPM'
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
        borderWidth: 0,
        dataLabels:{
            enabled:true,
            color: "#000",
           
        }
        // colorByPoint: true
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