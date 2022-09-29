def FP(x,P):
    while x!=P[x]:
        x=P[x]
    return x
def U(x,y,P):
    P[FP(y,P)]=FP(x,P)
for t in range(1,int(input())+1):
    N,E=map(int,input().split())
    L=[list(map(int,input().split())) for _ in '_'*E]
    L.sort(key=lambda x:x[2]);P=[i for i in range(N+1)]
    sum=cnt=0
    for i in range(len(L)):
        if FP(L[i][0],P)==FP(L[i][1],P):continue
        cnt+=1;sum+=L[i][2]
        U(L[i][0],L[i][1],P)
        if cnt==N:break
    print(f'#{t}',sum)