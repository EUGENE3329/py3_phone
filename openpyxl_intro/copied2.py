from openpyxl import Workbook
#from openpyxl.utils import get_column_letter
import  datetime

wb=Workbook()
ws1=wb.active


ws1['A1']=datetime.datetime(2010, 7, 19)

print(ws1['A1'].number_format)

