import time
from multiPing_sub import *


# ipList 디렉토리 설정
LIST_DIR = 'ipList.txt'


# main 프로그램(run)
if __name__ == "__main__":

    # ip 정보 불러오기
    ipList = Create_IpList(LIST_DIR)

    # 프로세스 및 쓰레드 등록
    processList, threadList = Create_Process_Thread(ipList)

    # 프로세스 및 쓰레드 실행
    Execute_Process_Thread(threadList)

    # 30 초간 응답 대기
    time.sleep(30)

    # 응답 없는 프로세스 종료
    Exit_Process(processList)
    time.sleep(2)

