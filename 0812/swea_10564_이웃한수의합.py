for T in range(1,int(input())+1):
    N=int(input())
    L=list(map(int,input().split()))
    M,m=0,L[0]+L[1]
    for i in range(N-1):
        s=L[i]+L[i+1]
        if s>M:M=s
        if s<m:m=s
    print(f'#{T} {M} {m}')