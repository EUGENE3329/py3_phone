#!/usr/bin/python3
import decimal
from decimal import  Decimal

flot0="  3.333333    \
"
flot1="  4.444444    \
"
flot2="  5.555555    \
"
flot3="  6.666666    \
"
flotSet=[ flot0,flot1,flot2,flot3 ]
for  ele  in flotSet:
    for  attr in dir(decimal)[23:31]:
        print( str(attr),        \
        Decimal(ele).quantize(Decimal('.0001'), '\t'  ,\
                                                rounding=decimal.attr    )
        )
'''
print( 'ROUND_05UP : \t',    \
Decimal(flot0).quantize(Decimal('.0001'),    '\n',
Decimal(flot1).quantize(Decimal('.0001'),    '\n',
                                rounding=    \
                                decimal.ROUND_05UP    )
)
'''

'''
idx=0
#for  i  in  dir(decimal):
for  i  in  dir(decimal)[23:31]:
    print( idx, '\t', str(i))
    idx += 1
'''    
