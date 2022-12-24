import time, calendar
!
'''
ref)
https://www.daleseo.com/python-time/

stamp, struct_time and
        float(32) or nano(64) type compared.
'''

# 현재시간에 대한, gmt기준 즉 지역정보 없는,
# 시간스탬프, 시간구조체, 추출
stampUtcNow = time.time()
stampNsUtcNow = time.time_ns()

# float 출력
print( stampUtcNow , " : 현재시간 UTC 스탬프")
# 실수형 스탬프에서 정수/소수 분리
stampUtcNowReal, stampUtcNowDec = \
           divmod( stampUtcNow, 1.0 )
print( stampUtcNowReal, " : ", \
            stampUtcNowDec, ", float stamp"  )

#nano 출력
print( stampNsUtcNow , " : 현재 나노시간 UTC 스탬프")
#나노stamp에서 정수/소수 분리
stampNsUtcNowReal, stampNsUtcNowDecimal = \
            divmod( stampNsUtcNow, 1e9 )
print( stampNsUtcNowReal, " : ", \
            stampNsUtcNowDecimal / 1e9, ", nano stamp" )

print()


#human reading from stamps
print( time.ctime( stampUtcNow ), \
                   " float형 human reading"  )
# nano is too big, error.
#print( time.ctime( stampNsUtcNow ), "nano형"  )
print()


structUtcNow = time.gmtime( stampUtcNow )
print( structUtcNow , " : 현재시간 UTC 구조체")
## ns스탬프는 크기가 너무 커서 gmtime()호출 불가.
# ns는 struct매소드가 없나?r0
# structNsUtcNow = time.gmtime( stampNsUtcNow )
# print( structNsUtcNow , " : 현재 나노시간 UTC 구조체")
## to do...

