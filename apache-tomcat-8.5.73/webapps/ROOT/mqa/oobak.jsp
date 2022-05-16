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
    display:none;
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
Statement hh=connection.createStatement();
Statement gg=connection.createStatement();
Statement uu=connection.createStatement();


ResultSet rs=stmt.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')AS 日期, TO_CHAR(round(decode(SUM(WGBLS),0,0,(SUM(WGBLS)/SUM(LJCYS)*1000000)),2),'999,999,9999')AS 制一累计外观DPPM,TO_CHAR(round(decode(SUM(ZYWGBLS),0,0,(SUM(ZYWGBLS)/SUM(DRDJSL)*1000000)),2),'999,999,9999')AS 制一外观DPPM from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"')  GROUP BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')");
ResultSet qd=ccdd.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')AS 日期, TO_CHAR(round(decode(SUM(DXBLS),0,0,(SUM(DXBLS)/SUM(LJCYS)*1000000)),2),'999,999,9999') AS 制一累计电性DPPM,TO_CHAR(round(decode(SUM(ZYDXBLS),0,0,(SUM(ZYDXBLS)/SUM(DRDJSL)*1000000)),2),'999,999,9999') AS 制一电性DPPM from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"')  GROUP BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')");
ResultSet cbb=cb.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')AS 日期, TO_CHAR(round(decode(SUM(NONWGBLS),0,0,(SUM(NONWGBLS)/SUM(NONLJCYS)*1000000)),2),'999,999,9999')AS 制二累计外观DPPM,TO_CHAR(round(decode(SUM(ZRWGBLS),0,0,(SUM(ZRWGBLS)/SUM(NONDRDJSL)*1000000)),2),'999,999,9999')AS 制二外观DPPM from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"')  GROUP BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')");
ResultSet hhh=hh.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')AS 日期, TO_CHAR(round(decode(SUM(NONDXBLS),0,0,(SUM(NONDXBLS)/SUM(NONLJCYS)*1000000)),2),'999,999,9999') AS 制二累计电性DPPM,TO_CHAR(round(decode(SUM(ZRDXBLS),0,0,(SUM(ZRDXBLS)/SUM(NONDRDJSL)*1000000)),2),'999,999,9999') AS 制二电性DPPM from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"')  GROUP BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')");
ResultSet ggg=gg.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')AS 日期, round(decode(SUM(WGBLS+NONWGBLS),0,0,(SUM(WGBLS+NONWGBLS)/SUM(LJCYS+NONLJCYS)*1000000)),2)AS total外观DPPM,round(decode(SUM(DXBLS +NONDXBLS),0,0,(SUM(DXBLS +NONDXBLS)/SUM(LJCYS +NONLJCYS)*1000000)),2)AS total电性DPPM from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"')  GROUP BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')");
ResultSet uuu=uu.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')AS 日期, TO_CHAR( round(decode(SUM(DRDJSL),0,0,(SUM(DRDJSL)/(sum(LJSYS)))*100),2),'fm990.00')AS 制一抽样率,TO_CHAR( round(decode(SUM(NONDRDJSL),0,0,(SUM(NONDRDJSL)/(sum(NONLJSYS)))*100),2),'fm990.00')AS 制二抽样率 from WIQWMS.OOBA where DATATIME2 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"')  GROUP BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME2,'YYYY/MM/DD'),'"+day+"')");
%>
	
	
	
		<div class="header">
			<h1 class="header-title">MQA数据可视化看板</h1>
		</div>
		<div class="wrapper">
			<div class="content">
				<div class="col col-l">
					
							
					
					
				<div class="xpanel-wrapper xpanel-wrapper-4001">		
			
					
					<div style="height:100%;" id="zydppmm"></div>
							<p></p>
					
						<div style="height:100%;" id="zydxdppmm"></div>
						
							<p></p>
                        <div style="height:100%;" id="aa"></div>
							
		                            <p></p>
		                            <div style="height:100%;" id="jjjj"></div>
							<p></p>
					
						<div style="height:100%;" id="kkkk"></div>
							<p></p>
                        <div style="height:100%;" id="llll"></div>
                       
		<table id="zydppm" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一累计外观DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一外观DPPM</td>
        
       
    </tr>
    
    <% while(rs.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=rs.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=rs.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=rs.getString(3)%></td>
      
    </tr>
    

    <% } %>
    
</table>

							
	<table   id="zydxdppm" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一累计电性DPPM</td>
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
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二累计外观DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二外观DPPM</td>
        
      
       
    </tr>
    <% while(cbb.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=cbb.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=cbb.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=cbb.getString(3)%></td>
      
      
    </tr>
    

    <% } %>
</table>
<table   id="vvcc" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二累计电性DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二电性DPPM</td>
        
      
       
    </tr>
    <% while(hhh.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=hhh.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=hhh.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=hhh.getString(3)%></td>
      
      
    </tr>
    

    <% } %>
</table>
<table   id="yyvv" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">total外观DPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">total电性DPPM</td>
        
      
       
    </tr>
    <% while(ggg.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=ggg.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=ggg.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=ggg.getString(3)%></td>
      
      
    </tr>
    

    <% } %>
</table>
			<table   id="qqyy" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一抽样率</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二抽样率</td>
        
      
       
    </tr>
    <% while(uuu.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=uuu.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=uuu.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=uuu.getString(3)%></td>
      
      
    </tr>
    

    <% } %>
</table>
					</div>
					
							
							
				</div>
				
			
		</div>
 		
</div>




 <script src="highcharts.js"></script>
<script src="data.js"></script>
<script src="exporting.js"></script>
<script src="accessibility.js"></script>



 <script type="text/javascript">
 
Highcharts.chart('zydppmm', {
	
	
    data: {
    	 
    	
        table: 'zydppm'
        	
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
    	 
		text: '制一OOBA检查外观DPPM'
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
 
Highcharts.chart('zydxdppmm', {
	
	
	
    data: {
    	 
    	
        table: 'zydxdppm'
        	
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
    	 
		text: '制一OOBA检查电性DPPM'
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
    	 
		text: '制二OOBA检查外观DPPM'
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
 

 
Highcharts.chart('jjjj', {
	
	
	
    data: {
    	 
    	
        table: 'vvcc'
        	
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
    	 
		text: '制二OOBA检查电性DPPM'
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
 

 
Highcharts.chart('kkkk', {
	
	
	
    data: {
    	 
    	
        table: 'yyvv'
        	
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
    	 
		text: 'OOBA检验结果（制一+制二）'
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
 

 
Highcharts.chart('llll', {
	
	
	
    data: {
    	 
    	
        table: 'qqyy'
        	
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
    	 
		text: 'OOBA抽样比例'
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