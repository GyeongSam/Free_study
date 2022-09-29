def FP(x,P):
    while x!=P[x]:
        x=P[x]
    return x
def U(x,y,P):
    P[FP(y,P)]=FP(x,P)
for t in range(1,int(input())+1):
    N,M=map(int,input().split())
    L=list(map(int,input().split()))
    P=[i for i in range(N+1)]
    for i in range(M):U(L[2*i],L[2*i+1],P)
    S=set()
    for i in range(1,N+1):
        S.add(FP(i,P))
    print(f'#{t}',len(S))