#!/usr/bin/python3

import os, platform

SYSTEM=platform.system()
MACHINE=platform.machine()
#작업폴더 설정
working_dir=os.getcwd()
if SYSTEM == "Windows":
    os.chdir("D:\개발_코딩연습\python_연습\GitHub\py3_phone-1\sample")
    pass
elif SYSTEM == "macOS":
    pass
elif SYSTEM== "Linux":
    if MACHINE == 'aarch64':    #smart phone
        os.chdir("/storage/emulated/0/Documents/py3_phone/sample/")
        
    pass
else:
    print('i have no idea what this system !!!')
    
print( 'working_dir : ', os.getcwd() )


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
'''
# the below is not working. 네가 생각하는 그런 iter가 아님.
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
print('start !!! _______')
for ele in range(1, 100):
    print(   next(tmp_fibo)  )
    if ele%10 == 0:
        print('####'*3)
        
