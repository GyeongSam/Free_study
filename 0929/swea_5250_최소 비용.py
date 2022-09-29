M=1<<15
for t in range(1,int(input())+1):
    N=int(input());R=range(N)
    L=[list(map(int,input().split())) for _ in R]
    DP=[[M]*N for _ in R]
    for i in R:
        for j in R:
            if i==j==0:DP[0][0]=0;continue
            c1=(DP[i-1][j]+(L[i][j]-L[i-1][j]+1 if L[i][j]-L[i-1][j]>0 else 1) if i-1>=0 else M)
            c2=(DP[i][j-1]+(L[i][j]-L[i][j-1]+1 if L[i][j]-L[i][j-1]>0 else 1) if j-1>=0 else M)
            DP[i][j]=min(c1,c2)
    print(f'#{t}',DP[N-1][N-1])