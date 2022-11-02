import sys

import openpyxl
from  openpyxl.utils.dataframe import dataframe_to_rows

import pandas as pd

#input_f=sys.argv[1]
input_f= openpyxl.load_workbook("sup1.xlsx",
                  data_only=True)

wb=openpyxl.Workbook()
ws=wb.active

for r in dataframe_to_rows( df, index=True, header=True):
    