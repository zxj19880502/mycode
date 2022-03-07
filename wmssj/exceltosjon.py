import datetime
import time
from tokenize import Double
import xlrd
import json
from datetime import datetime
from xlrd import xldate_as_datetime, xldate_as_tuple
def open_excel(file):
    """
    打开execl文件
    :param file: excel文件名字
    :return:
    """
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print("Error: " + str(e))


def parse_by_sheet_name(file, sheet_name):
    """
    获取Excel数据
    :param file: Excel文件名称
    :param sheet_name: sheet页名称
    :return: 该sheet页的数据(数组格式，每个成员是一个字典)
    """
    data = open_excel(file)
    table = data.sheet_by_name(sheet_name)
    nrows = table.nrows
    row_list = []
   
    for v in range(1, nrows):
        values = table.row_values(v)
       
        row_list.append(
           
            (
                
                {
                "WORK_ORDER":str(values[0]),
                "SerialNumber":str(values[1]), # 这里我只需要字符型数据，加了str(),根据实际自己取舍			
                #"TESTING_DATE":datetime(*xldate_as_tuple(values[2],0)).strftime('%Y-%m-%d %H:%M:%S'),
                "TESTING_DATE":str(values[2]),
                "GooglePartNumber":str(values[3]),
                "line":str(values[4]),
                "StationName":str(values[5]),
                "TEST_ITEM":str(values[6]),
                "LOWER_LIMIT":values[7],
                "UPPER_LIMIT":values[8],
                "TEST_VALUE":values[9],
                "TEST_RESULT":str(values[10]),
                }
                
            )
          
        )
        
    return row_list

def write_to_json_file(data, file_name):
    """
    写入json文件
    :param data: json数据
    :param file_name: json文件名称
    :return:
    """
    try:
        # 对中文编码处理，使得生成的json文件中中文能正常显示，而不是以Unicode码显示
        final_json = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
        with open(file_name, 'w') as fObj:
            fObj.write(final_json)

    except Exception as e:
        print("Error: " + str(e))

        
if __name__ == '__main__':
    excel_data = parse_by_sheet_name("4.xlsx", "Sheet1")
    print(excel_data)
    final_data = dict()
    
    final_data["body"] = excel_data
    write_to_json_file(final_data, "test.json")

 