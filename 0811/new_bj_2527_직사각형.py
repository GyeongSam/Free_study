def p(i1,i2,I):
    if I==i1+i2:
        return 0
    elif I>i1+i2:
        return -1
    else:
        return 1
for T in range(4):
    L=list(map(int,input().split()))
    x1,x2,y1,y2=L[2]-L[0],L[6]-L[4],L[3]-L[1],L[7]-L[5]
    print(x1,x2,y1,y2)
    X=(L[6] if L[6]>=L[2] else L[2]) - (L[0] if L[0]<L[4] else L[4])
    Y=(L[7] if L[7]>=L[5] else L[5]) - (L[1] if L[1]<L[5] else L[5])
    print(X,Y)
    x=p(x1,x2,X)
    y=p(y1,y2,Y)
    if x==-1 or y==-1:
        print('d')
    elif x==0 and y==0:
        print('c')
    elif x==1 and y==1:
        print('a')
    else:
        print('b')