#!/usr/bin/python3

from zoneinfo import ZoneInfo

from datetime import datetime, timedelta

print('utc direct. ::::     ')
dt_utc = datetime.utcnow()
print('now() utc, naive:              ', dt_utc)

dt_kst = datetime.utcnow()+ \
                timedelta(hours=9)
print('now() kst, naive:              ', dt_kst)

print('-----'*5)

'''
tmp_dt=datetime( dt_utc,     \
                                    tzinfo=    \
                                    ZoneInfo('Asia/Seoul') 
'''

'''
tmp_dt=datetime( 2022, 10, 20, 12,     \
                                    tzinfo=    \
                                    ZoneInfo('Asia/Seoul') )
'''                    
#print(tmp_dt)

import pytz
time_dt3=datetime.now(pytz.timezone('Asia/Seoul'))
print( "'asia/seoul' now(): ",  time_dt3 )
print("tz: ",  time_dt3.tzinfo  )

time_dt4=datetime.now()
print( "kr time        now(): ", time_dt4 )
print("tz: ",  time_dt4.tzinfo  )


# error occured, not fixed ...
#print(  zoneinfo.ZoneInfo('Asia/Seoul') )
#print(  ZoneInfo('Asia/Seoul') )
#print(  ZoneInfo( "America/Los_Angeles" ) )


#copied stacoverflow
#"https://stackoverflow.com/questions/67234984/python-get-current-utc-time-ignore-computer-clock-always"
# astimezone() 활용법.

now_berlin = datetime.now(ZoneInfo('Europe/Berlin'))
now_ny = now_berlin.astimezone(ZoneInfo('America/New_York'))

print('Time in Berlin:', now_berlin)
print('Time in New York', now_ny)

