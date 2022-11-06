#!/usr/bin/python3

import os

os.chdir("/storage/emulated/0/Documents/py3_phone/sample/")

# ex, iterable class
class  get_odds:
    def  __init__(  self, max ):
        self.n = 3
        self.max = max
    def  __iter__(  self  ):    
        return self
    def  next(self):
        if self.n <= self.max:
            ret = self.n 
            self.n += 2    # 리턴값을 설정한 후 2를 더한다. 
            return ret    # 그래야 else에서 반복에러를 발생가능.
        else:    # 최대값을 초과하면
            raise StopIteration

a=get_odds(10)
b=get_odds(10)
c=b                         # swallow copy
print(  a.next()  )
print(  a.next()  )
print(  b.next()  )
print(  c.next()  )
'''# the below is not working.
for ele in b:
    print( b )
'''

def  get_odds_generator():
    n=1
    
    n += 2
    print('1111'*5)
    yield  n
    
    n += 2
    print('2222'*5)
    yield n
    
    n+=2
    print('3333'*5)
    yield n
    
print("======"*2)
c=get_odds_generator()    # gen
print(  next(c)  )
print(  next(c)  )
print(  next(c)  )

def  fibonacci():
    n1=1
    n2=2
    while True:
        yield n1
        n1, n2 = n2, n1+n2
    #end of line of fibonacci.

tmp_fibo=fibonacci()
for ele in range(1, 100):
    print(   next(tmp_fibo)  )
    if ele%10 == 0:
        print('####'*3)
        
