'''
xl의 날짜셀을 추출한다.

# 아래  주석은 나중에 구현
#UI, 문자열로 입력 받기 때문에 년 월 일을 구분한다.
#making a criteria, datetime objs.
#Year =     input('year : ')
#Month=   input('month : ')
#Day=        input('day : ')
'''

import datetime

aDay = input('enter a day, day/month/year: ')
#aDay = '11/01/2013'    #for debugging
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

def ret_datetime():
    return (tmp_datetime1)

