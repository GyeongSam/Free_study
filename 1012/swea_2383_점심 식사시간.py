
for tc in range(1,int(input())+1):
    N=int(input())
    L=[list(map(int,input().split())) for _ in '_'*N]
    R=range(N);M=0
    P=[];S=[]
    for i in R:
        for j in R:
            if L[i][j]:S.append((i,j,L[i][j])) if L[i][j]>1 else P.append((i,j))
    for pi,pj in P:
        t=min([abs(S[x][0]-pi)+abs(S[x][1]-pj)+S[x][2] for x in (0,1)])
        if t>M:M=t
    print(f'#{tc}',M)





