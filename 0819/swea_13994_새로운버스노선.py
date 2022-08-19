def st(R):
    global M
    for j in R:
        B[j]+=1
        if B[j]>M:M=B[j]
for T in range(1,int(input())+1):
    N=int(input())
    B=[0]*1001
    M=0
    for i in '_'*N:
        s,l,r=map(int,input().split())
        if s==3 and l%2:
            st([i for i in range(l,r) if not i%3 and i%10]+[r])
        elif s==3:
            st([i for i in range(l,r) if not i%4]+[r])        
        else:
            st([i for i in range(l,r,s)]+[r])
    print(f'#{T} {M}')


