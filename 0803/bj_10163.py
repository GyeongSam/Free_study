import sys
N=int(input())
cp=[]
max_x=0
max_y=0
for _ in range(N):
    x,y,xl,yl=map(int, sys.stdin.readline().split())
    cp.append([x,y,xl,yl])
    if x+xl>max_x:max_x=x+xl
    if y+yl>max_y:max_y=y+yl

cnt=[0]*N
arr=[[0 for x_ in range(max_x)] for y_ in range(max_y)]
sub=0
for paper in cp:
    sub+=1
    for X in range(paper[0],paper[0]+paper[2]):
        for Y in range(paper[1],paper[1]+paper[3]):
            if arr[Y][X]!=0:
                cnt[arr[Y][X]-1]-=1
            arr[Y][X]=sub
            cnt[arr[Y][X]-1]+=1
for i in cnt:
    print(i)

    

