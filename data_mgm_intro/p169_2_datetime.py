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
print('just now: ', time_now.strftime("%d/%m/%Y")  )
print('######'*6)

#반드시 일,월,년 순으로 입력시켜야...
#에러발생, 찬형식
#tmp_form="%y,%m,%d"
#tmp_tic="2022,06,15"
#time_tmp=datetime.strptime(tmp_tic, tmp_form)
#print( time_tmp.strftime("%d,%m,%Y") )

##에러발생, 찬형식 시간 추가
#tmp_form="%y,%m,%d %H:%M"
#tmp_tic="2022,06,15 16:50"
#time_tmp=datetime.strptime(tmp_tic, tmp_form)
#print( time_tmp.strftime("%d,%m,%Y") )

#정상
std1="21/11/06 16:30"
form1= "%d/%m/%y %H:%M"
time_tmp1=datetime.strptime(std1, form1)
print( "std1: ", time_tmp1.strftime("%d,%m,%Y") )

#정상, 시간삭제
std2="22/10/22"
form2= "%d/%m/%y"
time_tmp2=datetime.strptime(std2, form2)
print( "std2; ", time_tmp2.strftime("%d,%m,%Y") )

#정상, 식별자 변경, 시간삭제
std3="27,02,22"
form3= "%d,%m,%y"
time_tmp3=datetime.strptime(std3, form3)
print("std3; ",  time_tmp3.strftime("%d/%m/%y") )

###############
#에러발생,  22(%y)년과 2022년(%Y) 은  형식form이 다르다
std4="11,06,2022 16:50"
form4="%d,%m,%Y %H:%M"
time_tmp=datetime.strptime(std4, form4)
print( "std4: ", time_tmp.strftime("%d,%m,%Y") )

form5="%d/%m/%y %H:%M"
std5="28/06/20 16:50"
time_tmp4=datetime.strptime(std5, form5)
print( "std5: ", time_tmp.strftime("%d,%m,%Y") )


time_tmp7=datetime.now(timezone.utc)
print('\nstd7 utc, timezone: ', time_tmp7.strftime("%d,%m,%Y") )

#timezone, 설정, 설정값추출
print('    time obj whole: ', str(time_tmp7))

# KST로 설정
import pytz
#tmp_tz= pytz.timezone('Asia/Seoul')
tmp_tz= pytz.timezone('Zulu')
#tmp_tz.localize( time_tmp7 )    # error occur
                # tz obj may nt be changed, 
                
print('    after changing, time obj whole: ',   \
               str(time_tmp7))

######## all fail about  tz changing

print('###### \n'*3)

#utc 어웨어 객체 생성
time_tmp11=datetime.utcnow()    # naive
print('std11 utc: ', str(time_tmp11), end= ' ')
print('\ttzinfo is ', time_tmp11.tzinfo)

# copied py doc official 
time_tmp12=datetime.now(timezone.utc)    #aware
print('std12 utc: ', str(time_tmp12), end= ' ')
print('\ttzinfo is ', time_tmp12.tzinfo)


#utc, iso, gmt 형식 