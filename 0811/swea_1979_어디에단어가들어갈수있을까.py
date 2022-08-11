
def ck(di,dj):
    sub=0
    n=i if di==1 else j
    if n==0:
        if [S[i+c*di][j+c*dj] for c in range(K+1)]==s1:sub+=1
    elif n==N-K:
        if [S[i+c*di][j+c*dj] for c in range(K-1,-2,-1)]==s1:sub+=1
    elif 0<n<N-K:
        if [S[i+c*di][j+c*dj] for c in range(-1,K+1)]==s2:sub+=1
    return sub

I=lambda:map(int, input().split())
for T in range(1, int(input()) + 1):
    N, K=I();R=range(N)
    s1=[1]*K+[0]
    s2=[0]+[1]*K+[0]
    S=[list(I()) for _ in R]
    cnt=0
    for i in R:
        for j in R:
            cnt+=ck(1,0)+ck(0,1)
    print(f"#{T} {cnt}")            	
