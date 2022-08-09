r=[4,3,1,2]
N=int(input())
L=[]
X,Y,S,m2=0,0,0,0
for i in range(6):
    s,d=map(int,input().split())
    if i!=0:
        if r[S-1]!=s:
            m1=d
            m2=L[-1]
    L+=[d]
    S=s
    if (s==1 or s==2) and d>X:X=d
    if (s==3 or s==4) and d>Y:Y=d
if m2==0:
    m1=L[0]
    m2=L[-1]
print(N*(X*Y-m1*m2))