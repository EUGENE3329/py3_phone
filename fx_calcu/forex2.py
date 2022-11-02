from forex_python.converter  import CurrencyRates
from  decimal  import  Decimal
from datetime import  datetime

ex_list=[]
date1 = datetime(2021, 10, 21, 15,15,15, 000000)

dst_f="forex_obj_test.pickle"
choice=1
# if절에서 피클 파일 존재 확인.
import os, pickle
if not os.path.isfile( dst_f ):
    tmp_rate= CurrencyRates()
    tmp_rate1 = CurrencyRates( force_decimal=True )
    ex_list.append( tmp_rate)
    ex_list.append(tmp_rate1)
    with open(dst_f, "wb") as fw:
        pickle.dump(ex_list, fw)

elif choice == 0:
    print('file...ok !!!')
    with open( dst_f, "rb" ) as fr:
        ex_list = pickle.load( fr )
        tmp_rate=ex_list[0]
        tmp_rate1=ex_list[1]
        
#피클에 저장 안됨. 어떻게 할까?
else:
        with open( dst_f, "rb" ) as fr:
            ex_list = pickle.load( fr )
            tmp_rate=ex_list[0]
            
            tmp_rate1=ex_list[1]

#print(ex_list)
#CurrencyRates객체에서 통신하는 듯
#그래서, 피클에 저장하는 의미가 없다.
print(  tmp_rate.convert( 'USD', 'KRW', 10, date1 )  )
print( tmp_rate1.convert( 'USD', 'KRW',                \
                                                  Decimal('10.456')       )    )
#객체에서 데이터추출 후 파일에 저장해야...             
                                                  
                                                                                                
                                                                                                                                                                                            