for T in range(1,int(input())+1):
    N=int(input())
    L=list(map(int,input().split()))
    V=0
    while True:
        m=max(L)
        i=L.index(m)
        V+=m*i-sum(L[:i])
        if i==len(L)-1:
            break
        L=L[i+1:]
        
    print(f'#{T} {V}')



    
        
