def check(di,dj):
    for d in range(l):
        if A[i+di*d][j+dj*d]!=A[i+di*(M-1-d)][j+dj*(M-1-d)]:
            return 0
    return 1

for T in range(1,int(input())+1):
    N,M=map(int,input().split())
    l=M//2
    A=[input() for _ in '_'*N]
    R=range(N)
    for i in R:
        for j in R:
            if N-i>=M and check(1,0):
                print(f'#{T} ',*[A[i][j] for i in range(i,i+M)],sep='')
                break
            if N-j>=M and check(0,1):
                print(f'#{T} ',*[A[i][j] for j in range(j,j+M)],sep='')
                break
        else:continue
        break

