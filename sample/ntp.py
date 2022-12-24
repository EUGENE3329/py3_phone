import  ntplib
from  time  import ctime

c=ntplib.NTPClient()
ntp_win_url="time.windows.com"

response=c.request( ntp_win_url, version=3 )
print( ctime( response.tx_time ) , " : ntp time, timestamp" )
print( response.delay, " : delay" )
print( response.offset, " : offset" )
