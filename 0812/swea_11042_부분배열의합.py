I=lambda :map(int,input().split())
for T in range(1,int(input())+1):
    N,n,m=I()
    L=[list(I()) for _ in range(N)]
    M=0
    for i in range(0,N-n+1):
        for j in range(0,N-m+1):
            s=0
            for k in range(n):
                for l in range(m):
                    s+=L[i+k][j+l]
            if s>M:M=s
    print(f'#{T} {M}')

