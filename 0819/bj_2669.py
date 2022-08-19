B=[[0]*101 for _ in '_'*101]
c=0
for _ in '_'*4:
    x1,y1,x2,y2=map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            if not B[x][y]:B[x][y]=1;c+=1
print(c)