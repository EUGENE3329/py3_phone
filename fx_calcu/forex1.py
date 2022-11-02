#!/usr/bin/python3

from  decimal  import  Decimal
from datetime import  datetime

'''
#무료 환율 서비스 https://theforexapi.com/
#유럽중앙은행,ecb,에서 매일 오후3시 CET에 정보를 가져온다.
#중앙유럽 표준시(CET, Central European Time)는 협정 세계시보다 1시간 빠르다.  UTC+1
'''
from forex_python.converter  import CurrencyRates

# if절에서 피클 파일 존재 확인.
import os
if not os.path.isfile( 'ex_obj.pickle' ):
    tmp_rate= CurrencyRates()
    tmp_rate1 = CurrencyRates( force_decimal=True )


usd_dic=tmp_rate.get_rates('USD') 

print( usd_dic.keys())    # 'KRW'
print("'KRW'  is :", usd_dic[ 'KRW' ] )

date1 = datetime(2021, 10, 21, 15,15,15, 000000)
print( date1 )

#return type is  float.
# 구글에서 21,10,21 15시15분 환율은 1177.61
print(  tmp_rate.get_rates('USD', date1)['KRW']  )
# usd에서 krw로 변환
print(  tmp_rate.get_rate('USD' , 'KRW')  )
#4번 21,10,21 15시 usd > krw 환율
print( tmp_rate.get_rate('USD', 'KRW', date1)  ) 
#5번 총액  환전 10달러  usd > krw
print(  tmp_rate.convert( 'USD', 'KRW', amount= 10  )  )
#6th 21,10,21 15시 환율로 총액 10달러 환전
print(  tmp_rate.convert( 'USD', 'KRW', 10, date1 )  )

#decimal사용하기. 10.456달러 환전.
tmp_rate1 = CurrencyRates( force_decimal=True )
print( tmp_rate1.convert( 'USD', 'KRW',                \
                                                  Decimal('10.456')  )    )

ex_list=[tmp_rate, tmp_rate1]

import pickle
with open("ex_obj.pickle", "wb") as fw:
    pickle.dump(ex_list, fw)

'''
#loading
with open( "ex_obj.pickle", "rb" ) as fr:
    ex_list_fromFR = pickle.load( fr )
    
print( ex_list_fromFR )
'''


'''
1,
매매기준율==기준환율==고시환율
basic_rate_of_exchange==basic_exchange_rate ==
exchange_rate

2,
현찰팔때  현찰매도율 기준+(1.75%), 
현찰살때 현찰매입률 기준-(1.76%), 그리고
스프레드는 위 1.75%, 현찰스프레드라고도 함.
송금할때, 송금받을때, 전신환스프레드 보통 달러당 1%

'''
#deposit=input('deposit: ')
#exchange_rate=input('EX rate: ')

#1, 거래일지작성기 만들기
# 최신기록은 파일 맨 끝에  누적기록


'''
객체종류
    계좌 ( 입금, 출금, 잔액, 거래일시, 단위)  
        계좌원화, 
        계좌달러, 
        
    환전 (거래일시, 기준환률, 매수환률, 매도환률,  단위)
'''

'''
거래일 22/9/7
기준환율 0000.000                    ₩/$
매매환율 1390.800                   ₩/$
환차손익 0.000
매입원액 4997839.000           ₩
매입달러 3593.499                   $
'''

'''
거래일 22/9/19
기준환율 0000.000                    ₩/$
매매환율 1393.100                   ₩/$
환차손익 0.000
매입원액 4999835.000           ₩
매입달러 3589.000                   $

용어정리

'''