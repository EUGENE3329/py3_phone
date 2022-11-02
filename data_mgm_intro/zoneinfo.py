import pytz

#cnt=0
#for tz in pytz.all_timezones:
    #cnt+=1
    #print( cnt, " : ", tz)
#or
tz_list      = pytz.all_timezones
tz_set      = pytz.all_timezones_set
tz_comm = pytz.common_timezones
tz_comm_set = pytz.common_timezones_set
tz_country_dic  = pytz.country_names
tz_country_tz_dic = pytz.country_timezones
'''
ref) above lines,,,
https://pynative.com/list-all-timezones-in-python/
'''

print( len(tz_list), 
            len(tz_set),
            len(tz_comm),
            len(tz_comm_set),
            len(tz_country_dic),
            len(tz_country_tz_dic)
)

print(tz_country_dic.keys(),          '\n\n', 
           tz_country_dic.values(), '\n')
print( tz_country_dic['NC'])

for v in tz_country_dic.keys():
    print(v, tz_country_dic[v] )
'''
#tz_input_str=input('Enter a timezone: ')
tz_input_str='Asia/Seoul'
idx=tz_list.index( tz_input_str)  
print(type(idx))
print(    idx, ' :  ' , tz_list[  idx ]  )
'''

from  backports.zoneinfo import ZoneInfo
from datetime import datetime, timezone, timedelta

from  tzdata import  *
dt = datetime(2020, 10, 31, tzinfo=ZoneInfo("Asia/Seoul"))

'''
설치 성공, 모듈 2개 설치하기
pip  install  "tzdata",   #1
                      "backports.zoneinfo" for ZoneInfo()    #2

is this a problem only in android?
'''
dt1 = datetime(2020, 10, 31, tzinfo=pytz.timezone("Asia/Tokyo"))
print( dt, ' : ' ,dt.tzinfo )
print( dt1, ' : ' ,dt1.tzinfo )
print('{}'.format(dt.tzname()))
print('{}'.format(dt1.tzname()))

print( type(ZoneInfo("Asia/Seoul") ))

'''
openpyxl에서 시간정보를 xlsx에 저장할  때, timezone정보는 제거한 후에 xlsx에 저장해야 한다.

테스트방법은 2개으 타임객체 나이브 어웨어를 생성 후, 각 각을 셀에 할당한 후에 파일로 저장한다. 그리고 다른 py스크립트에서 방금 저장한 xlsx를 불러온 후, 파이썬해석기에서 시간객체를 출력해 본다.
'''


