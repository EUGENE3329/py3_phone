#!/usr/bin/pyghon3
'''
time zone 디비에 수록된 예, 뉴욕 서울 도쿄.
국가코드                        US	
tz 디비이름                    America/New_York	
관할지역                        Eastern (most areas)	
type                              Canonical	
UTC_OFFSET    STD      −05:00	
UTC_OFFSET    DST      −04:00	
tz약어                 STD        EST	
tz약어                 DST        EDT	
소스파일                              northamerica

서울 일 때
KR  Asia/Seoul  Canonical  +09:00  +09:00  KST  asia
도쿄
JP  Asia/Tokyo  Canonical  +09:00  +09:00  JST  asia
'''
import time

# 시스템에 설정된 지역값을 리턴.
stampNow= time.time()
print( time.tzname, " : ")
# 예) 뉴욕 +18,000, 서울 -32,400 
print( time.timezone, " : ")
print()





# dst 설정
structNow=time.gmtime( stampNow )