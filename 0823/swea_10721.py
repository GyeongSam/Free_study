def MIN(L): #마지막 값+ 마지막값의 행,렬을 제외한 행렬의 최소값을 재귀하는 함수
    l=len(L)
    R=range(l)
    if l==2:
        return min(L[0][0]+L[1][1],L[1][0]+L[0][1])
    else:
        return min([L[-1][x]+MIN([[L[i][j] for j in R if j!=x] for i in range(l-1)]) for x in R])

for T in range(1,int(input())+1):
    N=int(input())
    R=range(N)
    L=[list(map(int,input().split())) for _ in '_'*N]
    print(f'#{T} {MIN(L)}')











