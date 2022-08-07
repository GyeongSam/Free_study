

X,Y=map(int, input().split())
N=int(input())
L=[list(map(int,input().split())) for _ in range(N+1)]

for n,i in enumerate(L):
    if i[0]==1:
        L[n][0]=1
    elif i[0]==2:
        L[n][0]=-1
        L[n][1]+=Y
    elif i[0]==3:
        L[n][0]=-1
    else:
        L[n][0]=1
        L[n][1]+=X

sum=0
for a in L[:-1]:
    sum+=min(abs(a[1]*a[0]-L[-1][0]*L[-1][1]),2*(X+Y)-abs(a[1]*a[0]-L[-1][0]*L[-1][1]))
print(sum)




