from random import * 

id = []
for i in range(1,21):
    id.append(i)
shuffle(id)
gotit = sample(id, 4)
chicken = gotit[0]
coffee = gotit[1:]
print(f"치킨당첨자 : {chicken} " )
print(f"치킨당첨자 : {coffee} " , )

# def printPerson(name = '홍길동', age = 20):
#     pass 

# print(printPerson('gd'))

# def func(name, *vars):
#     print(vars)
#     print('-=------')
    
# func('one', 'two', 'three', 'name')


# def func(**kwargs):
#     if 'name' in kwargs:
#         print(kwargs['name'])
#     else:
#         print("name 키가 없습니다.")
    

def func():
    return 10, 20
a, b =func()
print(a,b)
