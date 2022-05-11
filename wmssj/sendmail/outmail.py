# -*- coding: utf-8 -*-
 
"""
Module 根据定义的Task，发送邮件提醒，避免遗漏处理
"""
 
from asyncio import exceptions
import os
import xlrd
import schedule
import time
import win32com.client as win32
from datetime import datetime,date
 
 
dictWeek={0:"Monday",1:"TuesDay",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
 
def job():
    sPath = os.getcwd()
    sFile = "Task.xls"
    sExcelFile = sPath +"\\" + sFile
    print("执行完成")
    wb = xlrd.open_workbook(filename=sExcelFile)
       
    sheet1 = wb.sheet_by_index(0)   
    nrows1 = sheet1.nrows
     
    #注意weekday() 返回的是0-6是星期一到星期日
    sWeekday = dictWeek.get(datetime.now().weekday())
    sNow = datetime.now() 
 
    iDay = sNow.day
    sToday= formatDay(sNow,"yyyy-mm-dd")
 
    for iRow in range(1,nrows1):
        sCheck = sheet1.cell(iRow,3).value
        if sCheck != "Y":
            sFrequency = sheet1.cell(iRow,0).value
            s1 = sheet1.cell(iRow,1).value
            if sFrequency == "Week":
                if s1 == sWeekday:
                    s2 = sheet1.cell(iRow,2).value
                    sendEmail(s2)
            elif sFrequency == "Day":
                if formatDay(s1) == sToday:
                    s2 = sheet1.cell(iRow,2).value
                    sendEmail(s2)
            elif sFrequency == "Month":
                if int(s1) == int(iDay):
                    s2 = sheet1.cell(iRow,2).value
                    sendEmail(s2)
                        
def formatDay(sDay,sFormat):
    sYear = str(sDay.year)
    sMonth = str(sDay.month)
    sDay = str(sDay.day)
 
    if sFormat == "yyyy-mm-dd":
        sFormatDay = sYear +"-" +sMonth.zfill(2)+"-" +sDay.zfill(2)
    else:
        sFormatDay = sYear+"-" + sMonth + "-" + sDay
         
    return sFormatDay
 
     
def sendEmail(sTask):
    try:
    #读取config.txt，获得发送的目标邮箱账号
        sConfigFile="config.txt"
             
        f=open(sConfigFile,'r')
        try:
            file_Context=f.read()
        except:
            return False
        finally:
            if f:
                f.close()
         
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
 
        receivers = [file_Context]
        mail.To = receivers[0]
        mail.Subject ='来自系统自动发送的邮件'
        mail.CC = 'Xiaolong_Zhu@sz.chiconypower.com.cn'  # 抄送人
        mail.Importance = 2  #设置重要性为高
        mail.Body="邮件提醒：  \r\n    请注意处理任务作业，如已处理可忽略此封邮件。\r\n   任务内容：" + sTask + " \r\n     (此邮件由系统自动发送)"
        #mail.Attachments.Add('C:\\Users\enegc\\OneDrive - Bayer\\Personal Data\\'+sFileName+'.xlsx')
        mail.Attachments.Add(r'F:\wmssj\Task.xls') 
        mail.Send()
        return True
    except exceptions as e:
        return False
 
schedule.every().day.at("10:40").do(job)
 
while True:
    schedule.run_pending()
    time.sleep(1)