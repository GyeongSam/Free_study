C=[[0,1,2],[0,2,1],[1,2,0],[1,0,2],[2,1,0],[2,0,1]]
# C=[0,1,2]
def GO(I,n,F,cnt):
    sub=[]
    d=0
    for _ in range(n):
        while I-d>=1 or I+d<=N:
            if 0<I-d<=N and F[I-d]==0:d=-d;break
            if 0<I+d<=N and F[I+d]==0:d;break
            d+=1
        F[I+d]=1
        cnt+=abs(d)+1
        if _==n-1:break
        if d<0:d=-d
    if 0<I-d<=N and F[I-d]==0:
        sub.append(F[:])
        F[I+d]=0
        F[I-d]=1
        sub.append(F)
    else:sub.append(F)
    return sub,cnt

for T in range(1,int(input())+1):
    N=int(input())
    F=[1]+[0]*N
    L=[list(map(int,input().split())) for _ in '___']
    s=1000000
    for c in C:
        next=GO(L[c[0]][0],L[c[0]][1],F,0)
        for n in next[0]:
            sub=GO(L[c[1]][0],L[c[1]][1],n,next[1])
            for k in sub[0]:
                SUB=GO(L[c[2]][0],L[c[2]][1],k,sub[1])
                print(SUB,s)
                if SUB[1]<s:s=SUB[1]
    







