for tc in range(1,int(input())+1):
    R=range(int(input()))
    L=[list(map(int,input().split())) for _ in R]
    MAX=0
    for i in R:
        for j in R:
            if L[i][j]==1:
                L[i]
                di,dj=0,0
                while L[i+di][j]==1:di+=1
                while L[i][j+dj]==1:dj+=1
                if di*dj>MAX:MAX=di*dj
                for x in range(di):
                    for y in range(dj):
                        L[i+x][j+y]=2
    print(f'#{tc} {MAX}')
