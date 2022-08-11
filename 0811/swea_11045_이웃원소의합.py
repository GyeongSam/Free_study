for T in range(1,int(input())+1):
    N=int(input())
    R=range(1,N+1)
    L=[[0]*(N+2)]+[[0]+list(map(int,input().split()))+[0] for _ in R]+[[0]*(N+2)]
    M=0
    for i in R:
        for j in R:
            S=L[i+1][j]+L[i][j+1]+L[i-1][j]+L[i][j-1]
            if S>M:M=S
    print(f'#{T} {M}')



