I=lambda:map(int,input().split())
for T in range(1,int(input())+1):
    N,K=I()
    L=[list(I()) for _ in '_'*N]
    m=0
    for i in range(N):
        s=0
        J=i+K
        if J>=N:J=N
        for j in L[i][i:J]:s+=j
        if s>m:m=s
    print(f'#{T}',m)

