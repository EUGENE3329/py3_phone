#!/usr/bin/pyghon3

''' 
struct_time 구조,
struct_time to stamp, reverse함수
    용어, 
        정수부.소수부 == integer_part.decimal_part
        .
        
'''

import  time, calendar

# source setting
stampUtcNow = time.time()
stampNsUtcNow = time.time_ns()
####
# printing the local time.
print( "utc human reading : \n",  \
                     time.ctime(stampUtcNow)  )

## float 스템프 -> 시간 구조체
structUtcNow = time.gmtime( stampUtcNow )
structLocalNow = time.localtime( stampUtcNow )
print( "utc 값 : ========\n", structUtcNow )
print( "loc  값 : ========\n", structLocalNow )
# 시간구조체 분해, 총 9개의 성분이 있음.
for i  in structUtcNow:
    print( i )
    
#런타임의 시간구조체 성분 추출
print( "==== UTC 런타임  성분")
for  i  in  range(0,9):
    print( time.gmtime()[ i ] )


# miss-printing, nested localization. 
# 지역화 중복, 중복계산
stampLocalNow = calendar.timegm( structLocalNow )
print( "localized human reading : \n",  \
                     time.ctime( stampLocalNow ) )
print( " ==== wrong return.")

# comp utc  vs   local
print("  debug : ")
print( stampLocalNow, " : stamp  local")
print( stampLocalNow - 32400, " back to utc")
print( stampUtcNow, " : stamp  utc")






## 나노초 스템프 -> 시간 구조체
# 에러, 나노값이 너무 큼.
# structNsUtcNow = time.gmtime( stampNsUtcNow )

## to do...
# 시간구조체에서  dst  flag 는 당연히 0인가?












'''

structUtcNow = time.gmtime( stampUtcNow )
print( structUtcNow , " : 현재시간 UTC 구조체")
## ns스탬프는 크기가 너무 커서 gmtime()호출 불가.
# ns는 struct매소드가 없나?r0
# structNsUtcNow = time.gmtime( stampNsUtcNow )
# print( structNsUtcNow , " : 현재 나노시간 UTC 구조체")
## to do...


# 시스템의 지역/시간대 설정 정보
print( " timezone, 시간대 ': ", time.timezone )
print( " tzname, : ", " \t"*2, time.tzname )

# 스탬프 값에는 지역화 정보는 없다. 
# 모든 시스템의 스탬프는 같은 값이다.
structSeoulNow= time.localtime( stampUtcNow )
#stampFromStruct = time.time( structUtcNow )
print( structSeoulNow, " : 현재 서울 구조체.")


print( "\n :::: " )
# epoch 최초 값 객체 만들기.
# 1970, 1월, 1일, 0시0분0초
epoch_start = time.gmtime( 0 )    # key obj
print( type(epoch_start), " : type struct_time 구조체" )
print( epoch_start, " : epoch value")
#print( dir(epoch_start), " : dir(epoch_start)" )


#시간 구조체 
print('chan연습=================')
# getting epoch name.
epoch_name= dir(epoch_start)
print( epoch_name, " : epoch_name")


print('===== 속성 추출============')
for ele in epoch_start:
    print(ele, " : ", )






# 역-스탬프 
R_stampUtcNow= calendar.timegm( structUtcNow )
print( R_stampUtcNow, " : 역-스탬프 from struct_utc .")
print( stampUtcNow, " : 스탬프UtcNow 소스")
print( "역함수는 소수점 이하는 버린다.\n")


'''








# R_stampNs = calendar.timegm( structNsUtcNow )
#structNsUtcNow = time.gmtime( stampNsUtcNow )
# 역-스탬프 
# R_stamp= calendar.timegm( structUtcNow )
# print( R_stamp, " : 역-스탬프 from struct_utc .")
# print( stampUtcNow, " : source stamp_utc, not ns")