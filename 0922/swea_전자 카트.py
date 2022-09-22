I=input

def BT(n,a,sum):
    global M
    if (n==0):
        if sum+L[a][0]<M:M=sum+L[a][0]
    elif sum>M:
        return
    else:
        for i in range(1,N):
            if not visit[i]:
                visit[i]=1
                BT(n-1,i,sum+L[a][i])
                visit[i]=0

for t in range(1,int(I())+1):
    N=int(I())
    L=[list(map(int,I().split())) for _ in '_'*N]
    visit=[0]*N
    M=1e10
    BT(N-1,0,0)
    print(f'#{t}',M)


