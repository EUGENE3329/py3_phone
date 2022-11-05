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
print(type(s))
#
