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

Statement fai=connection.createStatement();
Statement faid=connection.createStatement();
Statement ccd=connection.createStatement();
Statement nn=connection.createStatement();
Statement mm=connection.createStatement();




ResultSet rs=stmt.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"'),TO_CHAR( round(decode(SUM(BLS),0,0,(SUM(BLS)/(sum(JCPS)))*100),2),'fm990.00')AS 制一累计FAI不良率,TO_CHAR( round(decode(SUM(BHGPS),0,0,(SUM(ZYBLSS)/(sum(zyjcs)))*100),2),'fm990.00')AS 制一FAI不良率 from WIQWMS.MQA where DATATIME1 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"')");
ResultSet faib=fai.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"'), round(decode(SUM(BLJS),0,0,(SUM(BLJS)/(sum(GDS)))*100),2)AS 制一累计异常比例,round(decode(SUM(BLJS),0,0,(SUM(ZYBLSS)/(sum(zygdss)))*100),2)AS 制一异常比例 from WIQWMS.MQA where DATATIME1 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"')");
ResultSet faidd=faid.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"'),round(decode(SUM(BLS),0,0,(SUM(BLS)/SUM(TRS)*1000000)),2)AS 制一累计HiPOTDPPM,round(decode(SUM(ZYBLSS),0,0,(SUM(ZYBLSS)/SUM(ZYTRS)*1000000)),2)AS 制一HiPOTDPPM from WIQWMS.MQA where DATATIME1 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"')");
ResultSet qcc=ccd.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"'),TO_CHAR( round(decode(SUM(nonBLS),0,0,(SUM(nonBLS)/(sum(nonJCPS)))*100),2),'fm990.00')AS 制二累计FAI不良率,TO_CHAR( round(decode(SUM(ZRBLS),0,0,(SUM(ZRBLS)/(sum(ZRJCS)))*100),2),'fm990.00')AS 制二FAI不良率 from WIQWMS.MQA where DATATIME1 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"')");
ResultSet nnn=nn.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"'), round(decode(SUM(nonBLJS),0,0,(SUM(nonBLJS)/(sum(nonGDS)))*100),2)AS 制二累计异常比例,round(decode(SUM(ZRBLS),0,0,(SUM(ZRBLS)/(sum(ZRGDS)))*100),2)AS 制二异常比例 from WIQWMS.MQA where DATATIME1 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"')");
ResultSet mmm=mm.executeQuery("SELECT TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"'),round(decode(SUM(NONBLS),0,0,(SUM(NONBLS)/SUM(NONTRS)*1000000)),2)AS 制二累计HiPOTDPPM,round(decode(SUM(ZRBLS),0,0,(SUM(ZRBLS)/SUM(ZRTRS)*1000000)),2)AS 制二HiPOTDPPM from WIQWMS.MQA where DATATIME1 BETWEEN to_CHAR('"+startime+"')AND to_char('"+endtime+"') GROUP BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"') ORDER BY TO_CHAR(TO_DATE(DATATIME1,'YYYY/MM/DD'),'"+day+"')");

%>
	
	
	
		<div class="header">
			<h1 class="header-title">MQA数据可视化看板</h1>
		</div>
		<div class="wrapper">
			<div class="content">
				<div class="col col-l">
					
							
					
					
				<div class="xpanel-wrapper xpanel-wrapper-4001">		
			
					
					
					
						<div style="height:100%;" id="zyfaii"></div>
							<p></p>
                        <div style="height:100%;" id="container"></div>
							
		                            <p></p>
                        <div style="height:100%;" id="aa"></div>
						<p></p>
						<div style="height:100%;" id="bb"></div>
							<p></p>
                        <div style="height:100%;" id="nnmm"></div>
							
		                            <p></p>
                        <div style="height:100%;" id="xxd"></div>
		                             
		<table id="zyfai"    style="position:absolute;width: 96.3%; font-family: Verdana, sans-serif;border-collapse: collapse;text-align: center;font-size:14px;height: 20%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一累计FAI不良率</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一FAI不良率</td>
         
       
    </tr>
      <tbody style="height:80%;" >
    <% while(rs.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=rs.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=rs.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=rs.getString(3)%></td>
      
    </tr>
    

    <% } %>
    </tbody>
</table>

							
	<table   id="datatable" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一累计异常比例</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一异常比例</td>
        
       
       
    </tr>
    <% while(faib.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=faib.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=faib.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=faib.getString(3)%></td>
       
      
    </tr>
    

    <% } %>
</table>
<table   id="faidd" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一累计HiPOTDPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制一HiPOTDPPM</td>
        
       
       
    </tr>
    <% while(faidd.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=faidd.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=faidd.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=faidd.getString(3)%></td>
       
      
    </tr>
    

    <% } %>
</table>
				<table   id="DPPM" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二累计FAI不良率</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二FAI不良率</td>
        
       
       
    </tr>
    <% while(qcc.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=qcc.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=qcc.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=qcc.getString(3)%></td>
       
      
    </tr>
    

    <% } %>
</table>	
	<table   id="nnm" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二累计异常比例</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二异常比例</td>
        
       
       
    </tr>
    <% while(nnn.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=nnn.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=nnn.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=nnn.getString(3)%></td>
       
      
    </tr>
    

    <% } %>
</table>	
	<table   id="sccv" style="position:absolute;width: 2%; font-family: Verdana, sans-serif;border-collapse: collapse;border: 1px solid #ebebeb;text-align: center;font-size:14px;height: 2%;display: none">
    <tr>
        <td style="background: #94c9ff;border: 1px solid #ebebeb;">时间</td>
       <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二累计HiPOTDPPM</td>
         <td style="background: #94c9ff;border: 1px solid #ebebeb;">制二HiPOTDPPM</td>
        
       
       
    </tr>
    <% while(mmm.next()){ %>
   
    <tr  >
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;"><%=mmm.getString(1)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=mmm.getString(2)%></td>
        <td style=" border: 1px solid #ebebeb;background: #94c9ff;" ><%=mmm.getString(3)%></td>
       
      
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
 

 
Highcharts.chart('zyfaii', {
	
	
	
    data: {
    	 
    	
        table: 'zyfai'
        	
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
    	 
		text: '制一 FAI不良率'
		// 该功能依赖 data.js 模块，详见https://www.hcharts.cn/docs/data-modules
	},
	
	yAxis: {
		gridLineDashStyle: 'ShortDash',//网格线样式
		allowDecimals: false,
		title: {
			text: '%',
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
			pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
			valueDecimals: 2,
			shared: true,
            crosshairs: [true, false]
		},

});



		</script>
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
    	 
		text: '制一异常比例'
		// 该功能依赖 data.js 模块，详见https://www.hcharts.cn/docs/data-modules
	},
	
	yAxis: {
		gridLineDashStyle: 'ShortDash',//网格线样式
		allowDecimals: false,
		title: {
			text: '%',
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
			pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
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
    	 
		text: '制一HI-POT DPPM'
		// 该功能依赖 data.js 模块，详见https://www.hcharts.cn/docs/data-modules
	},
	
	yAxis: {
		gridLineDashStyle: 'ShortDash',//网格线样式
		allowDecimals: false,
		title: {
			text: '%',
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
			pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
			valueDecimals: 2,
			shared: true,
            crosshairs: [true, false]
		},

});



		</script>
		 <script type="text/javascript">
 

 
Highcharts.chart('bb', {
	
	
	
    data: {
    	 
    	
        table: 'DPPM'
        	
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
    	 
		text: '制二FAI不良率'
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
 

 
Highcharts.chart('nnmm', {
	
	
	
    data: {
    	 
    	
        table: 'nnm'
        	
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
    	 
		text: '制二异常比例'
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
 

 
Highcharts.chart('xxd', {
	
	
	
    data: {
    	 
    	
        table: 'sccv'
        	
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
    	 
		text: '制二HI-POT DPPM'
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