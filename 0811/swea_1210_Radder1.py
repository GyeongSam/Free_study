def mv(j,d):
    while True:
        if 0<=j+d<=99 and L[i][j+d]==1:
            j+=d
        else:
            return j

for T in range(1,11):
    N=input()
    R=range(100)
    L=[list(map(int,input().split()))for _ in R]
    for j in R:
        if L[-1][j]==2:break
    for i in range(99,-1,-1):
        if j>0 and L[i][j-1]==1:j=mv(j,-1)
        elif j<99 and L[i][j+1]==1:j=mv(j,1)
    print(f'#{T} {j}')


