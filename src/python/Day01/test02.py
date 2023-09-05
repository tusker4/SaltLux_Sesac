import pickle;


def deposit(balance, money):
    print(f"{balance}원을 입금했습니다. 잔액은 {money}원 입니다.")
    return balance+money
    
deposit(5000, 2000)

def withdraw(balance, money):
    
    if money > balance:
        money -= balance
        print(f"{balance}원을 출금했습니다. 잔액은 {money}원 입니다.")
        return money
    else:
        print("출금할수없습니다.")
withdraw(1000,5000)

def profile(name, age, lang):
    print(f"이름 : {name}  나이 : {age}  언어 : {lang} ")
profile('남성희', 32, "python")

def weight(height, gender):
    if gender == "남자":
        std_weight = round(height * height * 22, 2)
    else:
        std_weight = round(height * height * 21, 2)
    print(f"키 {height*100 }cm {gender}의 표준 체중은 {std_weight}kg 입니다.")
weight(1.72 , '남자')

for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))
    
print("{0:.2f}".format(5/3))

s = open("data3.txt", "r", encoding="utf8")
print(s.read())
s.close()

with open("data34.txt", "r" , encoding="utf8") as file :
    print(file.read())