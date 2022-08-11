def ck(z1,z2,z3):
    if z1==z3 or z1==z3:
        return 0
    elif z1<z3<z2:
        return 1
    else:
        return -1

for T in range(4):
    L=list(map(int,input().split()))
    if L[2]-L[0]>=L[6]-L[4]:
        sub1=ck(L[0],L[2],L[4])
        sub2=ck(L[0],L[2],L[6])
        if sub1==1 or sub2==1 or (sub1==0 and sub2==0):
            X=1
        elif (sub1==0 and sub2==-1) or (sub1==-1 and sub2==0):
            X=0
        else: 
            X=-1
    else:
        sub1=ck(L[4],L[6],L[0])
        sub2=ck(L[4],L[6],L[2])
        if sub1==1 or sub2==1 or (sub1==0 and sub2==0):
            X=1
        elif (sub1==0 and sub2==-1) or (sub1==-1 and sub2==0):
            X=0
        else: 
            X=-1
    if L[3]-L[1]>=L[7]-L[5]:
        sub1=ck(L[1],L[3],L[5])
        sub2=ck(L[1],L[3],L[7])
        if sub1==1 or sub2==1 or (sub1==0 and sub2==0):
            Y=1
        elif (sub1==0 and sub2==-1) or (sub1==-1 and sub2==0):
            Y=0
        else: 
            Y=-1
    else:
        sub1=ck(L[5],L[7],L[1])
        sub2=ck(L[5],L[7],L[3])
        if sub1==1 or sub2==1 or (sub1==0 and sub2==0):
            Y=1
        elif (sub1==0 and sub2==-1) or (sub1==-1 and sub2==0):
            Y=0
        else: 
            Y=-1
    
    if Y==-1 or X==-1:
        print('d')
    elif Y==0 and X==0:
        print('c')
    elif (Y==1 and X==0) or (Y==0 and X==1):
        print('b')
    else:
        print('a')