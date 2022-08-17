P=[[1]]

def print_P(num):
    for n in P[:num]:
        print(*n)
    
for T in range(1,int(input())+1):
    N=int(input())
    print(f'#{T}')
    l=len(P)
    if l>=N:print_P(N)
    else:
        for i in '_'*(N-l):
            P.append([x+y for x,y in zip([0]+P[-1],P[-1]+[0])])
        print_P(N)

