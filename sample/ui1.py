'''
xl파일의 날짜셀의 정체는 datime객체이다.
    문자열이 아닌 날짜속성 셀일 때...
질문) 2021 엑셀의 날짜속성의 셀도 datetime객체인가?
답) xlsx 파일이라면 호환성이 있을 듯.
'''
import datetime


#aDay = input('enter a day, day/month/year: ')
aDay = '11/01/2013'    #for debugging
#datetime객체로 변환
tmp_datetime1=datetime.datetime.strptime(
                                                    aDay,   "%d/%m/%Y"  )


##debug
print( 
            tmp_datetime1.strftime( '%B, %b, %Y' ),
                                ' is ',
            tmp_datetime1.strftime( ' %A  ' )
)
##

####testing
#날짜 값이  같으면, 2개의 객체는 서로 같은가?
#답) 동일하다.
tmp_datetime2=datetime.datetime.strptime(
                                                    aDay,   "%d/%m/%Y"  
)
print( tmp_datetime1 == tmp_datetime2 )
#엑셀에 저장된 날짜객체 하나를 꺼내서 비교해 본다.
#실제로 같은지를 판별해 보자.
import  openpyxl
xl_fname='sales_2013.xlsx'
wb=openpyxl.load_workbook( xl_fname )
ws=wb.active
cell_datetime=ws['e4']  # jan/11/2013

#아래는 비교 자체가 잘못됨. cell obj  vs datetime obj
print( cell_datetime == tmp_datetime1 )
print( type(cell_datetime), ' ; ' , cell_datetime.value )
#셀에서 날짜객체를 추출하라.
print( 'cmp with 2 objs : ', 
  type(cell_datetime.value) == type(tmp_datetime1)
)

print( tmp_datetime1, cell_datetime.value )
print( tmp_datetime1 == cell_datetime.value )

wb.close()
#### testing end.

