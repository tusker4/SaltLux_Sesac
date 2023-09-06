N, M = input('지급액과 동전 액면가 : ').split()
N = int(N)
M = int(M)

# 4
    
print((N // M) if (N // M)== 0 else (N // M) + 1 )