chicken =10
waiting = 1


try:
    while True:
        print(f"남은치킨 : {chicken} ")
        order = int(input("몇마리를 주문?"))
        if order > chicken:
            print("재료가 부족하니다.")
        else:
            print(f"대기번호 : {waiting}, {order}마리를 주문했습니다.")
            waiting += 1
            chicken -= order
        if chicken <= 0:
            break    
        
except ValueError as e:
    print(e.__traceback__)
    print("값을 잘못 입력하였습니다.")
except:
    if input()> 10:
        print("에러")
