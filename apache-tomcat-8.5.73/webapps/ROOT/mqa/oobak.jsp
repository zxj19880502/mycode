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
String day = request.getParameter("day");

Statement ccdd=connection.createStatement();
Statement cb=connection.createStatement();


ResultSet rs=stmt.executeQuery("select TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"'), round(decode(SUM(WGBLS),0,0,(SUM(WGBLS)/SUM(LJCYS)*1000000)),2)AS PC外观DPPM,round(decode(SUM(NONWGBLS),0,0,(SUM(NONWGBLS)/SUM(NONLJCYS)*1000000)),2)AS NonPC外观DPPM,round(decode(SUM(WGBLS+NONWGBLS),0,0,(SUM(WGBLS+NONWGBLS)/SUM(LJCYS+NONLJCYS)*1000000)),2)AS total外观DPPM , round(decode(SUM(DXBLS),0,0,(SUM(DXBLS)/SUM(LJCYS)*1000000)),2)AS PC电性DPPM,round(decode(SUM(NONDXBLS),0,0,(SUM(NONDXBLS)/SUM(NONLJCYS)*1000000)),2)AS NonPC电性DPPM,round(decode(SUM(DXBLS +NONDXBLS),0,0,(SUM(DXBLS +NONDXBLS)/SUM(LJCYS +NONLJCYS)*1000000)),2)AS total电性DPPM from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')");
ResultSet qd=ccdd.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"'), round(decode(SUM(WGBLS),0,0,(SUM(WGBLS)/SUM(LJCYS)*1000000)),2)AS PC外观DPPM,round(decode(SUM(DXBLS),0,0,(SUM(DXBLS)/SUM(LJCYS)*1000000)),2)AS PC电性DPPM from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')");
ResultSet cbb=cb.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"'),round(decode(SUM(NONWGBLS),0,0,(SUM(NONWGBLS)/SUM(NONLJCYS)*1000000)),2)AS 制二外观DPPM, round(decode(SUM(NONDXBLS),0,0,(SUM(NONDXBLS)/SUM(NONLJCYS)*1000000)),2)AS 制二电性DPPM from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')");

%>
	
	
	
		<div class="header">
			<h1 class="header-title">MQA数据可视化看板</h1>
		</div>
		<div class="wrapper">
			<div class="content">
				<div class="col col-l">
					
							
					
					
				<div class="xpanel-wrapper xpanel-wrapper-4001">		
			
					
					
					
						<div style="height:100%;" id="container"></div>
							<p></p>
                        <div style="height:100%;" id="aa"></div>
							
		                            <p></p>
                       
		<table    style="position:absolute;width: 96.3%; font-family: Verdana, sans-serif;border-collapse: collapse;text-align: center;font-size:14px;height: 20%;">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一外观DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二外观DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">total外观DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一电性DPPM</td>
        
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二电性DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">total电性DPPM</td>
       
    </tr>
      <tbody style="height:80%;" >
    <% while(rs.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=rs.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=rs.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=rs.getString(3)%></td>
       <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=rs.getString(4)%></td>
       <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=rs.getString(5)%></td>
      <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=rs.getString(6)%></td>
       <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=rs.getString(7)%></td>
    </tr>
    

    <% } %>
    </tbody>
</table>

							
	<table   id="datatable" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一外观DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一电性DPPM</td>
         
       
       
    </tr>
    <% while(qd.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=qd.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=qd.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=qd.getString(3)%></td>
      
      
    </tr>
    

    <% } %>
</table>
<table   id="faidd" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二外观DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二电性DPPM</td>
        
      
       
    </tr>
    <% while(cbb.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=cbb.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=cbb.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=cbb.getString(3)%></td>
      
      
    </tr>
    

    <% } %>
</table>
			
					</div>
					
							
							
				</div>
				
			
		</div>
 		





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
    	 
		text: 'OOBA检验状况FOR制一'
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
    	 
		text: 'OOBA检验状况FOR制二'
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