from collections.abc import Callable, Iterable, Mapping
import threading
import time
from typing import Any


class Account:
    # 공유 객체 동시접근 문제 해결 : 상호배제
    lock = threading.Lock()

    def __init__(self, money=0):
        self.money = 0

    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        if self.money >= money:
            self.money -= money
            return money
        return 0


def depositor(acc):
    for i in range(10):
        acc.deposit(1000)
        print("1000 입금완료, 통장잔고", acc.money)
        # account.lock.release()


def withdrawal(acc):
    account.lock.acquire()
    for i in range(10):
        money = acc.withdraw(1000)
        if money:
            print("1000 출금 완료, 통장잔고 : ", acc.money, end=", ")
            account.lock.release()
        else:
            print("잔액이 부족하여 출금에 실패하였습니다.")
        account.lock.release()
        return money


account = Account()
threading.Thread(target=depositor, args=(account,)).start()  # ,를 써야 튜플로 인식
threading.Thread(target=withdrawal, args=(account, )).start()
