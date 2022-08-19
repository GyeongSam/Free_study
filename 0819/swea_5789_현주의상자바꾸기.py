I=lambda:map(int,input().split())
for T in range(1,int(input())+1):
    N,Q=I()
    A=[0]*(N+1)
    for i in range(1,Q+1):
        l,r=I()
        A[l:r+1]=[i]*(r-l+1)
    print(*A[1:])
