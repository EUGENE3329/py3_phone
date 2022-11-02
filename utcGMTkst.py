#!/usr/bin/python3

'''
utc는 전세계 공통 시간이므로,
구글에서, 타임서버에서, 나의 시스템에서 각 각 호출해 보기.
타임서버에서 utc를 가져올 수 있나???
'''

from datetime import datetime, timezone

#from  time server, 
import ntplib, ctime, time

winTime= "time.windows.com"
gleTime="time.google.com"
pleTime="time.apple.com"

client = ntplib.NTPClient()
responseW=client.request(winTime, version=3)
responseG=client.request(gleTime, version=3)
responseA=client.request(pleTime, version=3)

print("NTP :  ")
print( "win: (KST)", time.ctime(responseW.tx_time) )
print( "gle: (KST)", time.ctime(responseG.tx_time) )
print( "ple: (KST)", time.ctime(responseA.tx_time) )

print("####"*6)

#unix time stamp
utcT= datetime.now(timezone.utc)
print( "py utc aware: ", utcT )
# converting to unix timestamp
unixT=utcT.timestamp()
print( "utc aware, unix Tstamp: ", unixT )
#back to datetime from unixT
backT=datetime.fromtimestamp(unixT,tz=timezone.utc)
print("back to py from unix: ", backT)


"""
#failed below, stupied coding

#getting UTC from google.com
import urllib3

http=urllib3.PoolManager()
with http.request('GET', "http://google.co.kr/") as response:
    date = response.data
    print(date)
    
"""
