#!/urs/bin/python3
import random

#### from 1 to 46, 난수 한 개만 생성
i=random.randint(1,47)
print( " picking ONE : ", i )

#### 로또 흉내내기, imitation lottery
numlist=range(1,47)
s=random.sample(numlist,6)
print("1st lottery, not ordered \n ",  s )
s.sort()
print("1st lottery : \n ",  s )
print( type(s) )

#### 연금 복권 흉내내기, imitation pension lottery
# 6자리숫자 맞추기 + 1~5까지 조 맞추기
numlist=range(1,1000000)
digit_6=random.sample(numlist,1)
group=range(1, 6)
group_num=random.sample( group, 1 )
'''
print("2nd pension, not ordered \n ",  digit_6, " : ", group_num_select )
digit_6.sort()
'''
print("2nd pension : \n ",   digit_6, " : ", group_num)
