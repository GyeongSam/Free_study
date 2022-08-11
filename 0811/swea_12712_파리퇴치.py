for T in range(1,int(input())+1):
    N,M=map(int,input().split())
    R=range(N)
    L=[list(map(int,input().split())) for _ in R]
    m=0
    for i in R:
        for j in R:
            S1,S2=0,0
            for d in range(-M+1,M):
                A,B,C=0<=i+d<N,0<=j+d<N,0<=j-d<N
                if A:S1+=L[i+d][j]
                if B:S1+=L[i][j+d]
                if A and B:S2+=L[i+d][j+d]
                if A and C:S2+=L[i+d][j-d]
            S1-=L[i][j]
            S2-=L[i][j]
            if S1>m:m=S1
            if S2>m:m=S2
    print(f'#{T} {m}')

