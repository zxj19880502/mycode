import csv
import cx_Oracle
import time
from datetime import datetime
import pandas as pd
import os
# 生成excel文件名
curr_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

csv_file_name = 'sj/'+ curr_time + ".csv "

conn = cx_Oracle.connect('test', '123321', '172.22.8.234/MES')
        
v_sql = " select REEL_ID,PART_NO,VENDOR_CODE,M_LOT,DATE_CODE,UPDATE_TIME,'' as option1,''as option2 ,'' as option3,QTY from WIQWMS.CUS_REEL_BASE " \
        "WHERE regexp_like (PART_NO,'^(15|26|31|4|5|6|822|9mg)')AND UPDATE_TIME between to_date(to_char(sysdate-1/24,'yyyymmddhh24:mi:ss') ,'yyyymmddhh24:mi:ss') " \
        "and  to_date(to_char(sysdate,'yyyymmddhh24:mi:ss'),'yyyymmddhh24:mi:ss')  ORDER BY UPDATE_TIME"


cursor = conn.cursor()

cursor.execute(v_sql)


with open(csv_file_name,'w',newline='',encoding = 'gb18030') as t:

    writer=csv.writer(t)

    writer.writerows(cursor)

cursor.close()

conn.close()

