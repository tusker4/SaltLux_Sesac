
# #  2번 문제
# N = int(input("정수입력 : "))
# total = 0
# for i in range(1, N+1):
#     if i % 2 == 0:
#         total+=1
#         continue
# print(total)

# # 3번 문제
# N= 2020
# M = 3030
# for year in range(N, M+1):
#     if year % 400 == 0 :
#         print('윤년')
#     elif year % 100 == 0 :
#         print('평년')
#     elif year % 4 == 0 :
#         print('윤년')
#     else:
#         print(f"{year} : 평년")

# # 4번 문제
# N = int(input('정수입력 : '))

# num_char = -1  # switch 기법, flag 기법
# for i in range(2, N):
#     if N % i ==0:
#         num_char=1
#         break

# print(num_char)

#  13번 문제
N = input()
print(len(N))

print(f"선두 : ")


