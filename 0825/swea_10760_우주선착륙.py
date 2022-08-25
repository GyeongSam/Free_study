d=[-1,0,1]
p=lambda:map(int,input().split())
for T in range(1,int(input())+1):
    N,M=p()
    H=[list(p()) for _ in '_'*N]
    ans=0
    for i in range(N):
        for j in range(M):
            h=H[i][j]
            sub=0
            for di in d:
                for dj in d:
                    if (di,dj)==(0,0):continue
                    I,J=i+di,j+dj
                    if 0<=I<N and 0<=J<M and H[I][J]<h:
                        sub+=1
            if sub>=4:ans+=1
    print(f'#{T}',ans)
