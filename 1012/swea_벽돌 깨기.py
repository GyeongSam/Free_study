
def dfs(n,bricks):
    global ans
    if n==N:
        cnt=0
        for i in RH:
            for j in RW:
                if bricks[i][j]:cnt+=1
        if cnt<ans:ans=cnt
    else:
        for choice in RW:
            next_bricks=[b[:] for b in bricks]
            flag=0
            S=[]
            for i in RH:
                if next_bricks[i][choice]:
                    if next_bricks[i][choice]>1:S.append((i,choice,next_bricks[i][choice]));flag=1
                    next_bricks[i][choice]=0
                    break
            while(S):
                i,j,c=S.pop()
                for d in range(-c+1,c):
                    if 0<=i+d<H:
                        if next_bricks[i+d][j]>1:
                            S.append((i+d,j,next_bricks[i+d][j]))
                        next_bricks[i+d][j]=0
                    if 0<=j+d<W:
                        if next_bricks[i][j+d]>1:
                            S.append((i,j+d,next_bricks[i][j+d]))
                        next_bricks[i][j+d]=0
            if flag:
                for j in RW:
                    i1=H-1
                    while(1):
                        while(i1>=0 and next_bricks[i1][j]):i1-=1
                        i2=i1-1
                        while(i2>=0 and next_bricks[i2][j]==0):i2-=1
                        if i1>=0 and i2>=0:
                            next_bricks[i1][j]=next_bricks[i2][j]
                            next_bricks[i2][j]=0
                            i1-=1;i2-=1
                        else: break
            dfs(n+1,next_bricks)
            
for t in range(1,1+int(input())):
    N,W,H=map(int,input().split())
    RW=range(W);RH=range(H);ans=181
    bricks=[list(map(int,input().split())) for _ in '_'*H]

    dfs(0,bricks)
    print(f'#{t}',ans)

