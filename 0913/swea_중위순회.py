p=print
def in_order(n):
    
    if 0<n<=N:
        in_order(n*2)
        p(tree[n],end='')
        in_order(n*2+1)


for T in range(1,11):
    tree=[0]
    N=int(input())
    for _ in '_'*N:tree.append(input().split()[1])
    p(f'#{T}',end=' ')
    in_order(1)
    p()

    

    

    

        
    
        
    