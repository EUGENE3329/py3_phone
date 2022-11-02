#!/usr/bin/python3

from  decimal  import  Decimal
import decimal

from datetime import  datetime

decimal.getcontext().prec = 2

class Accounts():
    AMOUNT_KRW = Decimal('0.00')
    AMOUNT_USD = Decimal('0.00')


    def set( self, krw='0.00',        \
                                     usd='0.00'):
        self.AMOUNT_KRW=Decimal(krw)
        self.AMOUNT_USD=Decimal(usd)
        return 0


    def get(self):
        return self.AMOUNT_KRW(), self.AMOUNT_USD


#def init_accounts():
    

def view():
    
    while ctr:
        krw=Decimal(input('krw: '))
        usd=Decimal(input('usd: '))
        accounts_now(krw, usd)
        ctr=input('continue ?, ( exciting is 0    )  '  )
        if int(ctr) == 0:
            print('exiting ...')
            break
            
    return 0

    
if __name__ == "__main__":
    
    a=Accounts()
    
    view()
    check_accounts()
    
    
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
'''