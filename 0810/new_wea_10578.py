def gap(x,y,dx,dy):
    sub=L[x+dx][y+dy]-L[x][y]
    return sub if sub>=0 else -sub

for tc in range(int(input())):
    N=int(input())
    L=[list(map(int,input().split())) for _ in range(N)]

    SUM=0
    for i in range(N):
        for j in range(N):
            if i!=N-1:
                SUM+=gap(i,j,1,0)*2
            if j!=N-1:
                SUM+=gap(i,j,0,1)*2
                
    print(SUM)
