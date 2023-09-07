numbers = [1, 2, 3, 4, 5]


class NumberIterator:
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


it = NumberIterator(numbers)
while True:
    num = it.__next__()  # next(it)
    print(num)
print("프로그램을 종료합니다.")
