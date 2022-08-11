r=range(5)
def check(N):
    for x in r:
        for y in r:
            if L[x][y]==N:return x,y


def bingo(x,y,dx,dy):
    for c in r:
        print(x-c*dx,[y-c*dy])
        if L[x-c*dx][y-c*dy]!=0:
            return 0
    return 1 

        

L=[list(map(int,input().split())) for _ in r]
A=[list(map(int,input().split())) for _ in r]
cnt=0
for X in r:
    for Y in r:
        print(f'X:{X},Y:{Y}')
        x,y=check(A[X][Y])
        print(f'x:{x},y:{y}')
        L[x][y]=0
        if bingo(x,y,1,0)==1:cnt+=1
        print(f'cnt x:{cnt}')
        if bingo(x,y,0,1)==1:cnt+=1
        print(f'cnt y:{cnt}')
        if x==y and bingo(x,y,1,1)==1:cnt+=1
        print(f'cnt xy1:{cnt}')
        if x+y==4 and bingo(4,0,1,-1)==1:cnt+=1
        print(f'cnt xy2:{cnt}')
        print()
        if cnt>=3:break
        
    if cnt>=3:break

print((X)*5+Y+1)
        

        
