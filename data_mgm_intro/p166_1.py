import os
from datetime import date

from openpyxl import Workbook

os.system('clear')

input_xl_f='sales_2013.xlsx'
output_xl_f='tmp3.xlsx'

if os.path.exists(input_xl_f) and \
    os.path.isfile(input_xl_f):
        input_wb=openpyxl.load_workbook(input_xl_f)
        input_ws1=input_wb['january_2013']
else:
    print('open error, input file !!!')
    
if os.path.exists(output_xl_f) and \
    os.path.isfile(output_xl_f):
        output_wb=openpyxl.load_workbook(output_xl_f)
        output_ws1=input_wb[0]
        if output_ws1.title =='filyering_cost':
            print('good !!!')
        else:
            print('output worksheet error')
            exit(1)
else:
    print('open error, output file !!!')
