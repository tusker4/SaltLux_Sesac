import sys

def convert(string):
    try:
        if int(string) > 10:
            raise Exception('10이상이 입력되었습니다.')  # raise : 에러를 명시
        return int(string)
    except Exception as e:
        raise (e)


a = input('정수입력 : ')
try:
    num = convert(a)
    print(f"{num}")
except Exception as e:
    print(e)


a, b = input('정수 두 개입력 : ').split()

try:
    a = int(a)
    b = int(b)
    c = a//b
    print(f"{a} // {b} = {c}")

    # 앞의 이름을  (A as B) B의이름으로 바꾼다
except ZeroDivisionError as e:
    print('0으로 나누기가 실행되었습니다.', e)
except (TypeError | NameError):
    print("정의되지 않은 변수를 참조하거나 올바르지 않은 타입을 참조")
except Exception as e:
    print(e, file=sys.stderr)
finally:
    print('프로그램 종료합니다')
