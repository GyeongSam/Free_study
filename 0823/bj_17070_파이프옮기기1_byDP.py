import sys
N=int(input())
Room=[[1]*(N+2)]+[[1]+list(map(int,sys.stdin.readline().split()))+[1] for _ in '_'*N]+[[1]*(N+2)]
sub=[[[0,0,0]]*(N+2) for _ in '_'*(N+2)]
sub[1][2]=[1,0,0]
for i in range(1,N+1):
    for j in range(3,N+1):
        if Room[i][j]==1:
            continue
        fr1=sub[i][j-1]
        fr2=sub[i-1][j-1]
        fr3=sub[i-1][j]
        SUB1=fr1[1]+fr1[0] if Room[i][j-1]!=1 else 0
        SUB2=fr2[0]+fr2[1]+fr2[2] if Room[i-1][j-1]!=1 and Room[i-1][j]!=1 and Room[i][j-1]!=1 else 0
        SUB3=fr3[1]+fr3[2] if Room[i-1][j]!=1 else 0
        sub[i][j]=[SUB1,SUB2,SUB3]
print(sum(sub[N][N]))


