import platform

print("시스템 정보 ==========")
print( 
"아키텍트 : ", platform.architecture(), '\n',    #bit, linkage 리턴.
#ELF (Executable and Linkable Format)
#유닉스 계열 시스템들의 표준 바이너리 파일로 실행 파일, 목적 #파일. 공유 라이브러리 그리고 코어 덤프를 위한 표준 파일 형식

"system  : ",            platform.machine(), '\n',        #시스템 유형
"node : ",            platform.node(), '\n', #네트윅 이름
"cpu  : ",            platform.processor(), '\n',    #시스템 cpu
"os  : ",            platform.system(), '\n',          #시스템 os
"rel : ",            platform.release(), '\n',        #시스템 release번호
"ver : ",            platform.version(), '\n',        #시스템 release 버전
"uname:",        platform.uname(), '\n',            
               
        )