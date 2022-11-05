#!/urs/bin/python3
import random

#### from 1 to 46
i=random.randint(1,47)
print( " picking ONE : ", i )

numlist=range(1,47)
s=random.sample(numlist,6)
print("1st lottery, not ordered \n ",  s )
s.sort()
print("1st lottery : \n ",  s )
print(type(s))
#
