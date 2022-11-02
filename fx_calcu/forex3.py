#!/usr/bin/python3

#pickle, decimal  연습

from forex_python.converter  import CurrencyRates
from  decimal  import  Decimal
from datetime import  datetime

ex_list=[]
date1 = datetime(2021, 10, 21, 15,15,15, 000000)

# if절에서 피클 파일 존재 확인.
choice=1

import os, pickle
#print( os.getcwd() )
#chd="/storage/emulated/0/Documents/py3_phone"
#os.chdir(chd)

if not os.path.isfile( 'tmp.pickle' ):
    a=100
    b="weAREtheWORLD"
    ex_list.append( a)
    ex_list.append(b)
    with open("tmp.pickle", "wb") as fw:
        pickle.dump(ex_list, fw)

elif choice == 0:
    print('file...ok !!!')
    with open( "tmp.pickle", "rb" ) as fr:
        ex_list = pickle.load( fr )
        a=ex_list[0]
        b=ex_list[1]
        
else:
    print( 'direct open !!!')
    with open( "tmp.pickle", "rb" ) as fr:
        ex_list = pickle.load( fr )
        a=ex_list[0]
        b=ex_list[1]

#피클 테스트
print(ex_list)

import decimal
floaT1=decimal.Decimal('1')
floaT2=decimal.Decimal('7')
floaTpi=decimal.Decimal('3.141592')
floaTe=decimal.Decimal('2.7182818')
floaTzeroPLUS=decimal.Decimal('+0')
floaTzeroMINUS=decimal.Decimal('-0')

decimal.getcontext().prec= 6
print( floaT1 / floaT2)
decimal.getcontext().prec= 28
print( floaT1 / floaT2)
#정밀도  기본은 28, 필요시 더 확장 가능
decimal.getcontext().prec= 29
print( floaT1 / floaT2)
print( decimal.getcontext() )
#정밀도 설정 비교
decimal.getcontext().prec= 6
print( "\n", decimal.getcontext() )
#정밀도 자리올림 등은 산술연산 결과에서 반영.
#decimal 객체 자신은 입력된 값으로 표현됨.
floaTnAn=Decimal('NaN')
print( 'nan ret: ', floaT2 / floaTnAn, floaTnAn / floaT1 )
floaTinfini=Decimal( 'Infinity')
#무한대는 양으로 발산, 음으로발산
print( '무한 ret: ', floaT2 / floaTinfini, '\t',    \
                                (-1)*floaTinfini / floaT2 )
# 0 또한 양에서 수렴 .
print( 'zero+-: ', floaTe + floaTzeroPLUS, '\t',
                               floaTe + floaTzeroMINUS  )
print( 'zero*: ', floaTe * floaTzeroPLUS, '\t',
                               floaTe * floaTzeroMINUS  )

#signal trapping
print('\nsignal : ')
tmp= decimal.getcontext() 
print( 'now : ', tmp )    #현재상태
print( tmp.traps.items() )    #트랩의 전체 옵션들
print( type(tmp.traps))    #트랩성질
from math import pi, e
print( 'math pi is : \n' ,Decimal(3.141592), '\n', floaTpi)
print( 'pi is : \n' ,Decimal(pi), '\n', floaTpi)
print(  'is same ? :', floaTpi == 3.141592 )    # ret False
# 연산 속성 변경
#tmp.traps[decimal.FloatOperation]=True
print('added : ' ,tmp )    #추가 후
#print( Decimal(3.141592), floaTpi)    
#floatOP 추가 후 에러발생, realNUM객체와 srt 객체 혼용시
# D(5.00)과 D('5.00')을 구별해야  함

print( 'is same ? :' ,floaTpi == 3.141592 )    # ret False

#부동소숫점 연습
data=list(    \
    map(Decimal, 
    '3.75 7.54 1.86 0.08 7.98 5.65'.split(' ') )
)
print( 'max is: ', max(data))
print( 'min is: ', min(data))
print( 'sorted :', sorted(data))
print( 'sum is: ', sum(data))
z1, z2, z3 = data[: 3]
print( 'z1 is: ', str(z1)) 
print( 'z2 round 1st: ', round(z2, 4)) 
print( 'data origin : ', data) 
print( 'z3 * 5: ', z3*5 , '\t', z3*Decimal('5'), '\t', 
z3*Decimal('5.00')
)
print( 'z1*z2 ', z1*z2 )
print( 'z1/z2 ', z1/z2 , 'z1%z2 ', z1%z2 )
#simple math fun()
decimal.getcontext().prec = 28
print( "2제곱근: ", Decimal('2').sqrt() )
print( "자연상수2승: ", Decimal(' 2 ').exp() )
print( "2제곱: ", Decimal('2')**2 )
print( "ln2: ",  Decimal('2').ln() )
#소숫점 자릿수  설정
print( 'e                  : ', e )
print( 'Decimal(e) : ' , Decimal(e)  )
print(  'e, ROUND_DOWN : ' ,         \
            Decimal(e).quantize(Decimal('.0001'),    \
                                rounding=decimal.ROUND_DOWN    )
            )
print(  'e, ROUND_UP ' ,         \
            Decimal(e).quantize(Decimal('.0001'),    \
                                rounding=decimal.ROUND_UP    )
            )

print(  'e, ROUND_HALF_DOWN : ' ,         \
            Decimal(e).quantize(Decimal('.0001'),    \
                                rounding=    \
                                decimal.ROUND_HALF_DOWN    )
            )

print(  'e, ROUND_HALF_UP : ' ,         \
            Decimal(e).quantize(Decimal('.0001'),    \
                                rounding=    \
                                decimal.ROUND_HALF_UP    )
            )
print(  'e, ROUND_HALF_EVEN : ' ,         \
            Decimal(e).quantize(Decimal('.0001'),    \
                                rounding=    \
                                decimal.ROUND_HALF_EVEN    )
            )
print(  'e, ROUND_FLOOR : ' ,         \
            Decimal(e).quantize(Decimal('.0001'),    \
                                rounding=    \
                                decimal.ROUND_FLOOR    )
            )
print(  'e, ROUND_CEILING : ' ,         \
            Decimal(e).quantize(Decimal('.0001'),    \
                                rounding=    \
                                decimal.ROUND_CEILING    )
            )
print(  'e, ROUND_05UP : ' ,         \
            Decimal(e).quantize(Decimal('.0001'),    \
                                rounding=    \
                                decimal.ROUND_05UP    )
            )












