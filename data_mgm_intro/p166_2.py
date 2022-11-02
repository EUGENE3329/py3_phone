import os
from datetime import date

from openpyxl import Workbook
import openpyxl

os.system('clear')

input_xl_f='sales_2013.xlsx'
output_xl_f='tmp3.xlsx'

if os.path.exists(input_xl_f) and  os.path.isfile(input_xl_f):
    input_wb=openpyxl.load_workbook(input_xl_f)
    input_ws1=input_wb['january_2013']
else:
    print('open error, input file !!!')
    
if os.path.exists(output_xl_f) and os.path.isfile(output_xl_f):
    output_wb=openpyxl.load_workbook(output_xl_f)
    output_ws1=output_wb['filtering_cost']
else:
    print('open error, output file !!!')


#finding the amount of sales is over 14,000.
COLUMN_AXIS=None
filtered_rows_list=[]

for ele in input_ws1['1']:
    if ele.value == 'Sale Amount':
        COLUMN_AXIS = ele.column_letter
        
for ele in input_ws1.columns:
    print(ele)
    
    