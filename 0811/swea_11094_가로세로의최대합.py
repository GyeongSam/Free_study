for T in range(1,int(input())+1):
    N=int(input());R=range(N)
    L=[list(map(int,input().split())) for _ in R]
    m=0
    for i in R:
        for j in R:
            S=-L[i][j]
            for d in R:
                S+=L[i-d][j]
                S+=L[i][j-d]
            if S>m:m=S
    print(f'#{T} {m}')
