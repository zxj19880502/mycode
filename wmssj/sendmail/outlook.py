import win32com.client as win32
import pythoncom
import schedule 
import time
pythoncom.CoInitialize()
curr_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
def send_mail():
    outlook = win32.Dispatch('Outlook.Application')
    reciList = ['Xiaolong_Zhu@sz.chiconypower.com.cn'] #收件人
    for i in range(len(reciList)):
        mail_item = outlook.CreateItem(0) # 0: olMailItem
        mail_item.Recipients.Add(reciList[i])
        mail_item.Subject = '来自系统自动发送的邮件'
        mail_item.CC = 'Xiaolong_Zhu@sz.chiconypower.com.cn'  # 抄送人
        mail_item.Importance = 2  #设置重要性为高 
        mail_item.BodyFormat = 2          # 2: Html format
        mail_item.HTMLBody  = '''<H2>hi</H2><BR>
    	<FONT SIZE=4>请注意<BR>
    	这是一封<Font Face=Times Roman Size=4.5 Color=blue>有附件</font>并且<Font Face=Times Roman Size=4.5 Color=red>邮件</font>。<BR>'''
        mail_item.Attachments.Add('f:ssssc.xlsx') 
        mail_item.Send()
        print(curr_time+"发送邮件成功")
schedule.every(1).minutes.do(send_mail)
 
while True:
    schedule.run_pending()
    time.sleep(1)