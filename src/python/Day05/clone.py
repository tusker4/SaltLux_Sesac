# 매일 오후 5시 30분에
# 알림을 출력하는 스레드를 작성해보세요
from datetime import datetime
import time
import threading


def work():
    print('작업을 실행합니다.')


def reserved():
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now == "17:30":
            work()
        time.sleep(1)
        
if __name__ == '__main__':
    threading.Thread(target=reserved).start()
    print("예약작업이 진행되었습니다.")
