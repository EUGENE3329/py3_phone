import  arrow

import  datetime
import ntplib

# setting variable
smp1="2013-05-11T21:23:58.970460+07:00"
row_utcNow= datetime.datetime.utcnow()
arr_utcNow= arrow.utcnow()

print( arrow.get(smp1) , "sample_date" )
print( row_utcNow, " utc_datetime" )
print( arr_utcNow , " utc_arrow")

# arrow  api
print()
print( arr_utcNow.shift(hours= +9), "+9 shifting")
print( arr_utcNow.to('Asia/Seoul'), "Asia/Seoul" )
arrow_usa= arr_utcNow.to('US/Pacific')
arrow_seoul=arr_utcNow.to('Asia/Seoul')
print( arrow_usa  , "미국/태평양")

print()
print( arrow_usa.shift(hours=-3).humanize(), "미국시간")
print(arrow_seoul.humanize(),  "한국시간" )

print()
print( arrow_usa.timestamp() , '태평양timestamp')
print( arrow_seoul.timestamp(), '서울timestamp' )


