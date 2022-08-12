def l(M):
    le=0
    for I in range(1,11):
        for J in range(1,11):
            sub=0
            if P[I][J]==M:
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if P[I+di][J+dj]!=M:
                        sub+=1
            le+=sub
    return le

for T in range(1, int(input())+1):
    N = int(input())
    P = [[0]*12 for _ in range(12)]
    for p in range(N):
        L=list(map(int, input().split()))
        for i in range(L[0],L[2]+1):
            for j in range(L[1],L[3]+1):
                P[i+1][j+1]+=L[4]
    print(f'#{T} {l(1)+l(2)}')



