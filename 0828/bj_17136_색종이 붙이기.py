import pprint


def Box():
    for D in range(1,12):
        I=i+D-1
        J=j+D-1
        if I>9 or J>9:return D-1
        for d in range(D):
            jd=j+d
            id=i+d
            if jd<10 and L[I][jd]!=1:return D-1
            if id<10 and L[id][J]!=1:return D-1

def wax(i,j,n):
    for di in range(n):
        I=i+di
        for dj in range(n):
            J=j+dj
            L[I][J]=0

R=range(10)
L=[list(map(int,input().split())) for _ in R]

P=[0,5,5,5,5,5]

pprint.pprint(L)

cnt=0
for i in R:
    for j in R:
        if L[i][j]:
            L[i][j]=Box()
            if L[i][j]>5:
                if L[i][j]%2:
                    cnt=-1
                    break
                else:
                    wax(L[i][j])
                    P[L[i][j]]-=4
                    break
    else:continue
    break

if cnt!=-1:
    for n in range(5,0):
        for i in R:
            for j in R:
                if L[i][j]==n:




pprint.pprint(L)