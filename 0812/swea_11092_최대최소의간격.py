for T in range(1,int(input())+1):
    N=int(input())
    L=list(map(int,input().split()))
    M,A,a=(0,)*3;m=11
    for i in range(N):
        if L[i]>=M:M=L[i];A=i
        if L[i]<m:m=L[i];a=i
    print(f'#{T} {A-a if A>a else a-A}')
