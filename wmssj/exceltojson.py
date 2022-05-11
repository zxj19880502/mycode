import  xlrd
import json
import time
import configparser
cf=configparser.ConfigParser()
secs=cf.sections()
def readExcelData():
    data = []             
    
    keyData=['SerialNumber','StationName','STARTING_DATE','ENDING_DATE','GooglePartNumber','LINE','WORK_ORDER','WO_STATUS','RESULT']
    keyData1=['WORK_ORDER','SerialNumber','TESTING_DATE','GooglePartNumber','LINE','StationName','TEST_ITEM','LOWER_LIMIT','UPPER_LIMIT','TEST_VALUE','TEST_RESULT']
    workbook = xlrd.open_workbook(r'2.xlsx')
    
    sheet = workbook.sheet_by_index(0)
   
    rows = sheet.nrows
    cols = sheet.ncols
   
    p = []
    for i in range(1, rows):
        d={}
        for j in range(0,cols):
            q=keyData[j] 
            d[q] = sheet.cell(i, j).value 
        ap = []
        for k, v in d.items():
            if isinstance(v, float):  
                 
                 ap.append('"%s":"%s"' % (k, v)) 
            else:
                 ap.append('"%s":"%s"' % (k, str(v)))
            

        s = '{%s}' % (','.join(ap))  
        p.append(s)
        
    t = '[%s]' % (','.join(p))  
    t2='"payload":'+'{'+'"@type":'+'"type.googleapis.com/hardware.data.collection.Data",'+'"factoryData":'+'{'+'"batchAssemblage":'+'{'+'"assemblages":'+'"null",'+'"body":'+t+'}'+'}'+'}'
    data.append(t2)
    t3='{%s}' % (','.join(data))  

    fh = open(r'zd.json',"w")
    fh.write(t3)
    fh.close()

readExcelData()

class JsonFormat():
   
    def __init__(self,filepath,newpath):
        self.filepath=filepath
        self.newpath=newpath
    def format_turn(self):
        file=open(filepath,'rb')
      
        str=json.load(file)
      
        js_data=json.dumps(str,indent=4,separators=(',',':')).encode('utf-8').decode('raw_unicode_escape')
    
        with open(newpath,'w') as f:
            print(js_data)
            f.write(js_data)

if __name__=="__main__":
    now = time.strftime("%Y%m%d%H")
    filepath="zd.json"
    newpath=now+".json"
    obj=JsonFormat(filepath,newpath)
    obj.format_turn()
