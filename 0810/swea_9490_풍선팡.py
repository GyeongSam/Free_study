for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    L=[list(map(int,input().split())) for _ in range(N)]
    MAX=0
    for i in range(N):
        for j in range(M):
            sum=0
            n=L[i][j]
            for d in range(-n,n+1):
                if 0<=i+d<N:sum+=L[i+d][j]
                if 0<=j+d<M:sum+=L[i][j+d]
            sum-=n
            if sum>MAX:MAX=sum
    print(f'#{tc} {MAX}')
