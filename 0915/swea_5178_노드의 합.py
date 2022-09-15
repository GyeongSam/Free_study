def C(n):
    if n>N:return 0
    if tree[n]:return tree[n]
    return C(2*n)+C(2*n+1)
for T in range(1,int(input())+1):
    tree=[0]*1001
    N,M,L=map(int,input().split())
    for _ in '_'*M:i,v=map(int,input().split());tree[i]=v
    print(f'#{T}',C(L))
