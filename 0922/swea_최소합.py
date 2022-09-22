for t in range(1,int(input())+1):
    N=int(input())
    L=[list(map(int,input().split())) for _ in '_'*N]
    DP=[[0]*N for _ in '_'*N]
    for i in range(N):
        for j in range(N):
            sub=[]
            if i>0:sub.append(DP[i-1][j])
            if j>0:sub.append(DP[i][j-1])
            DP[i][j]=L[i][j]+(min(sub) if sub else 0)
    print(f'#{t}',DP[N-1][N-1])
