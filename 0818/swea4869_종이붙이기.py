L=[0,1,3]

def p():print(f'#{T} {L[N]}')

for T in range(1,int(input())+1):
    N=int(input())//10
    if N<len(L):p()
    else:
        for i in '_'*(N-len(L)+1):
            L.append(L[-1]+L[-2]*2)
        p()
        
    

