#!/usr/bin/python3

import platform, os

SYSTEM=platform.system()
MACHINE=platform.machine()
#작업폴더 설정
working_dir=os.getcwd()
if SYSTEM == "Windows":
    os.chdir("D:\개발_코딩연습\python_연습\데이터분석입문\ch3")
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


import ui_main, datetime
tmp=ui_main.ret_datetime()
print( 'you entered : ', tmp.strftime('%Y-%m-%d'))