p=print
def Turn(L):
    T=tuple(L[-i] for i in range(1,N+1))
    return list(zip(*T))

for T in range(1,int(input())+1):
    N=int(input())
    L=[list(input().split()) for _ in '_'*N]
    R1=Turn(L)
    R2=Turn(R1)
    R3=Turn(R2)
    p(f'#{T}')
    for i in range(N):p(*R1[i],' ',*R2[i]," ",*R3[i],sep='')
