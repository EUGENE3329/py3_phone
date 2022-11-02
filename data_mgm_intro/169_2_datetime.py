#!/usr/bin/python3

import os, sys

from datetime import date, datetime, timedelta, timezone

import openpyxl

os.system('clear')

#작업 디렉토리가 실행파일 장소와 일치하지 않아서 생기는 에러 수정
working_dir=os.getcwd()
print('work here: ', working_dir )

if working_dir != "/storage/emulated/0/Documents/py3_phone/data_mgm_intro/":
    os.chdir("/storage/emulated/0/Documents/py3_phone/data_mgm_intro/")
print("Now !!!: ", os.getcwd())

time_now = datetime.now()
print( time_now.strftime("%d/%m/%Y")  )
print('######'*6)

#에러발생, 
#tmp_form="%y,%m,%d"
#tmp_tic="2022,06,15"
#time_tmp=datetime.strptime(tmp_tic, tmp_form)
#print( time_tmp.strftime("%d,%m,%Y") )

tmp_form="%d,%m,%y %H:%M"
tmp_tic="8,06,20 16:50"
time_tmp=datetime.strptime(tmp_tic, tmp_form)
print( time_tmp.strftime("%d,%m,%y") )

tmp_form4="%d/%m/%Y %H:%M"
tmp_tic4="28/06/2022 16:50"
time_tmp4=datetime.strptime(tmp_tic4, tmp_form4)
print( time_tmp4.strftime("%d,%m,%Y") )

time_tmp6=datetime.utcnow()
print( time_tmp6.strftime("%d,%m,%Y") )

import pytz
cnt=0
#for tz in pytz.all_timezones:
    #cnt+=1
    #print( cnt, " : ", tz)
#or
tz_list = list(pytz.all_timezones)
print('last item: ',  tz_list[-1] , tz_list.index('Asia/Seoul'))

#how to setting for timezone
#time_tmp6 is the ret of utcnow()
print( "\n1st, tz is : ", time_tmp6.tzinfo, time_tmp6 )
pytz.utc.localize( time_tmp6 )
print( "2nd tz is : ", time_tmp6.tzinfo, time_tmp6 )

KST = pytz.timezone('Asia/Seoul')
KST.localize(time_tmp6)
print( "3rd tz is : ", time_tmp6.tzinfo , time_tmp6)