import subprocess
import threading


# ip 정보를 받아오는 IpList 생성
def Create_IpList(LIST_DIR):
    ipList = []
    with open(LIST_DIR) as f:
        for ip in f:
            ipList.append(ip.rstrip()) # rstrip  →  '\n' 제거

    return ipList


# 프로세스 및 쓰레드 등록
def Create_Process_Thread(ipList):
    processList = []
    threadList  = []
    for ip in ipList:

        # ping 명령을 실행할 프로세스 생성
        process = Execute_Process(ip)

        # 프로세스를 실행할 쓰레드 생성
        thread = threading.Thread(
            target=Execute_Thread,
            args=[process, ip]
        )

        # 프로세스 및 쓰레드 등록
        processList.append(process)
        threadList.append(thread)

    return processList, threadList


# 프로세스 및 쓰레드 실행
def Execute_Process_Thread(threadList):
    for thread in threadList:
        thread.daemon = True
        thread.start() # 쓰레드 내부에서 각각의 프로세스 실행


# 프로세스를 실행할 쓰레드 작업
def Execute_Thread(process, ip):
    process.stdout.readline()
    result = process.stdout.readline()

    success = str(result).__contains__('TTL')\
            | str(result).__contains__('ttl')

    if success == True:
        print(ip, 'SUCCESS')
    else:
        print(ip, 'FAIL')


# ping 명령을 실행할 프로세스 작업
def Execute_Process(ip):
    command = ['ping', ip]
    process = subprocess.Popen(
        command,
        shell=False,
        stdout=subprocess.PIPE
    )
    return process


# 응답 없는 프로세스 종료
def Exit_Process(processList):
    for process in processList:
        if process.poll() == None: # process 가 살아있는 경우
            process.kill()
