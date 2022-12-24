#!/usr/bin/phthon3
'''

'''
####setting working directory.
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
####

####displaying menus.
def menu_list():
    desc = "               \n     \
        2) column pick\n     \
        1) datetime    \n     \
        0) done. . .       \n     \
    "
    print( desc )
    return 0
####


#### main
#import ui_datetimes

while True:
    menu_list()
    menu=input("select one menu,   " )

    
    if menu == '2':
        import ui_columnPick
        pass
        
    if menu == '1':
        import ui_datetimes        
        
    if menu=='0':
        print('done. . .')
        break
