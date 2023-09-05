from random import *

count = 0
for index in range(50):
    time = randint(5, 50)

    if time >= 5 and  time <= 15:
        count += 1
        print(f"[0] {index}번째 손님 (소요시간 : {time})")
    else:
        print(f"[ ] {index}번째 손님 (소요시간 : {time})")
print( f"총 탑승객 : {count}명")
