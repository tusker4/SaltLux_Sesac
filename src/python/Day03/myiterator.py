numbers = [1, 2, 3, 4, 5]


class NumberIterator:  # iterator 소모성
    def __init__(self, values) -> None:
        self.__values = list
        self.__current = 0  # 내부 반복자

    def __iter__(self):
        return self

    def __next__(self):  # 메서드가 호출되면 현재 반복값이 반환된다.
        if self.__current >= len(self.__values):
            raise StopIteration
        self.__current += 1
        return self.__values[self.__current - 1]


def next(iter):
    return iter.__next__()

def get(self, index):
    if index >= len(self.__values):
        raise Exception('잘못된 인덱스 참조입니다.')
    else:
        return self.__values[index]
    
def seek(self): # 다시 시작하는 것
    self.__current = 0


it = NumberIterator(numbers)
for _ in range(0, 5):
    num = next(it)
    print(num)
num = next(it)
it.seek()

for i in it:
    print(i)


while True:
    num = it.__next__()  # next(it)
    print(num)
print("프로그램을 종료합니다.")



