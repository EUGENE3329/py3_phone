from datetime  import datetime, timezone

#utc 어웨어 객체 생성
time_tmp11=datetime.utcnow()    # naive
print('std11 utc: ', str(time_tmp11), end= ' ')
print('\ttzinfo is ', time_tmp11.tzinfo)
# copied py doc official 
time_tmp12=datetime.now(timezone.utc)    #aware
print('std12 utc: ', str(time_tmp12), end= ' ')
print('\ttzinfo is ', time_tmp12.tzinfo)


#현지 시간대, 덴마크, 휴대폰
"""
uname_result(system='Linux', node='localhost', release='4.14.186-24084238', version='#1 SMP PREEMPT Mon Aug 1 17:47:17 KST 2022', machine='aarch64')

std13 utc naive:  2022-10-16 09:10:18.944612    tzinfo is  None
std14 utc aware:  2022-10-16 09:10:18.944635+00:00     tzinfo is  UTC
std15 utc aware:  2022-10-16 11:10:18.944660    tzinfo is  None

std13 utc naive:  2022-10-16 09:12:14.843627    tzinfo is  None
std14 utc aware:  2022-10-16 09:12:14.843658+00:00     tzinfo is  UTC
std15 utc aware:  2022-10-16 18:12:14.843697    tzinfo is  None
"""
time_tmp13=datetime.utcnow()    # naive
print('std13 utc naive: ', str(time_tmp13), end= ' ')
print('\ttzinfo is ', time_tmp13.tzinfo)
# copied py doc official 
time_tmp14=datetime.now(timezone.utc)    #aware
print('std14 utc aware: ', str(time_tmp14), end= ' ')
print('\ttzinfo is ', time_tmp14.tzinfo)
# local, 
time_tmp15=datetime.now()    #aware
print('std15 utc aware: ', str(time_tmp15), end= ' ')
print('\ttzinfo is ', time_tmp15.tzinfo)




#utc, iso, gmt 형식 